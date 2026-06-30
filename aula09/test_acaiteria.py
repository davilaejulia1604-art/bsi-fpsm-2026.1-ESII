# test_acaiteria.py — testes do sistema da açaiteria
#
# Os testes provam que cada padrão faz o que promete. Rode todos com:  pytest
import pytest
from acaiteria import (
    EntregaMoto, Retirada, criar_entrega,
    Acaiteria, Observador,
)


# ---------- STRATEGY: cada entrega calcula o seu preço ----------
def test_moto_cobra_taxa_fixa_mais_por_km():
    assert EntregaMoto().preco(2) == 9.0        # 5 + 2*2


def test_retirada_e_de_graca():
    assert Retirada().preco(10) == 0.0          # não importa a distância


# ---------- FACTORY: traduz um nome na estratégia certa ----------
def test_factory_cria_a_estrategia_certa():
    assert isinstance(criar_entrega("moto"), EntregaMoto)


def test_factory_reclama_de_nome_desconhecido():
    with pytest.raises(ValueError):
        criar_entrega("teleporte")              # não existe -> erro claro


# ---------- FACADE + STRATEGY via FACTORY: o total do pedido ----------
def test_total_soma_subtotal_e_entrega():
    loja = Acaiteria()
    total = loja.finalizar("Ana", [10.0, 5.0], "moto", distancia_km=2)
    assert total == 24.0                        # 15 de açaí + 9 de moto


# ---------- OBSERVER: um observador novo é avisado ----------
def test_observador_inscrito_recebe_o_evento():
    loja = Acaiteria()

    class Espiao(Observador):                   # um observador de teste
        def __init__(self):
            self.recebido = None
        def atualizar(self, evento):
            self.recebido = evento

    espiao = Espiao()
    loja.inscrever(espiao)
    loja.finalizar("Bia", [20.0], "retirada", distancia_km=0)

    assert espiao.recebido["cliente"] == "Bia"
    assert espiao.recebido["total"] == 20.0


# ------------------------------------------------------------------
# TODO (Parte B): adicione uma forma de entrega nova — o DRONE.
#
#   1. Em acaiteria.py, crie a estratégia (taxa fixa 8 + 3 por km):
#
#          class EntregaDrone(Entrega):
#              def preco(self, distancia_km):
#                  return 8.0 + 3.0 * distancia_km
#
#   2. Registre o drone na fábrica criar_entrega (UMA linha no dicionário):
#
#          "drone": EntregaDrone,
#
#   3. Escreva aqui o teste do drone e rode pytest (deve passar):
#
#          def test_drone_cobra_taxa_fixa_mais_por_km():
#              from acaiteria import EntregaDrone
#              assert EntregaDrone().preco(2) == 14.0      # 8 + 3*2
# ------------------------------------------------------------------
