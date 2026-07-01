# test_estacionamento.py — a rede de segurança do estacionamento.
#
# Estes testes PASSAM. Eles são o que deixa você refatorar o código sujo
# com segurança: depois de cada mudança, rode "pytest" e veja tudo verde.
import pytest
from estacionamento import (
    TarifaCarro, TarifaMoto, TarifaCaminhao, criar_tarifa,
    Estacionamento, Observador,
)


# --- Tarifa (Strategy) ---
def test_tarifa_carro():
    assert TarifaCarro().valor(2) == 11.0        # 5 + 3*2

def test_tarifa_moto():
    assert TarifaMoto().valor(2) == 6.0          # 3 + 1.5*2

def test_tarifa_caminhao():
    assert TarifaCaminhao().valor(2) == 20.0     # 10 + 5*2


# --- Fábrica da tarifa ---
def test_criar_tarifa_certa():
    assert isinstance(criar_tarifa("moto"), TarifaMoto)

def test_criar_tarifa_desconhecida():
    with pytest.raises(ValueError):
        criar_tarifa("aviao")


# --- Entrar e sair ---
def test_entrar_conta_os_carros():
    e = Estacionamento()
    e.entrar("AAA0000", "carro", 8)
    assert e.n == 1

def test_saida_cobra_e_libera_a_vaga():
    e = Estacionamento()
    e.entrar("AAA0000", "carro", 8)
    total = e.processar_saida("AAA0000", 11)     # 3 horas -> 5 + 3*3 = 14
    assert total == 14.0
    assert e.n == 0
    assert "AAA0000" not in e.d

def test_saida_cobra_no_minimo_uma_hora():
    e = Estacionamento()
    e.entrar("BBB1111", "moto", 9)
    total = e.processar_saida("BBB1111", 9)      # 0 horas -> piso de 1 -> 3 + 1.5 = 4.5
    assert total == 4.5


# --- Prévia (não tira o carro) ---
def test_previa_nao_remove_o_carro():
    e = Estacionamento()
    e.entrar("CCC2222", "carro", 8)
    assert e.previa("CCC2222", 10) == 11.0       # 2 horas -> 5 + 3*2
    assert e.n == 1


# --- Observer ---
def test_observador_recebe_o_evento():
    e = Estacionamento()

    class Espiao(Observador):
        def __init__(self):
            self.evento = None
        def atualizar(self, evento):
            self.evento = evento

    espiao = Espiao()
    e.obs.append(espiao)
    e.entrar("DDD3333", "carro", 8)
    e.processar_saida("DDD3333", 9)              # 1 hora -> 5 + 3 = 8

    assert espiao.evento["placa"] == "DDD3333"
    assert espiao.evento["valor"] == 8.0

def test_avisos_saem_no_terminal(capsys):
    e = Estacionamento()
    e.entrar("EEE4444", "carro", 8)
    e.processar_saida("EEE4444", 9)
    saida = capsys.readouterr().out
    assert "[CANCELA]" in saida
    assert "[CAIXA]" in saida
    assert "[PAINEL]" in saida
