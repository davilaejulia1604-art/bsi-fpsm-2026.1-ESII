# estacionamento.py — sistema de um estacionamento (Aula 10)
#
# Este código FUNCIONA e TEM TESTES (rode: pytest). Mas ele está cheio de
# "code smells" — sinais de código mal cuidado. O trabalho da aula é
# RECONHECER esses smells e REFATORAR com segurança (os testes te protegem).
#
# Aqui já moram dois padrões da Aula 9: uma Tarifa (Strategy) e avisos quando
# um carro sai (Observer). O evento dos avisos ainda é um dict "solto".


# ---------- Tarifa por tipo de veículo (Strategy) ----------
class Tarifa:
    def valor(self, horas):
        raise NotImplementedError


class TarifaCarro(Tarifa):
    def valor(self, horas):
        return 5.0 + 3.0 * horas


class TarifaMoto(Tarifa):
    def valor(self, horas):
        return 3.0 + 1.5 * horas


class TarifaCaminhao(Tarifa):
    def valor(self, horas):
        return 10.0 + 5.0 * horas


def criar_tarifa(tipo):
    tabela = {"carro": TarifaCarro, "moto": TarifaMoto, "caminhao": TarifaCaminhao}
    if tipo not in tabela:
        raise ValueError(f"tipo de veículo desconhecido: {tipo!r}")
    return tabela[tipo]()


# ---------- Avisos quando um carro sai (Observer) ----------
class Observador:
    def atualizar(self, evento):
        raise NotImplementedError


class Cancela(Observador):
    def atualizar(self, evento):
        print(f"[CANCELA] abrindo para {evento['placa']}")


class Caixa(Observador):
    def atualizar(self, evento):
        print(f"[CAIXA] cobrar R$ {evento['valor']:.2f} de {evento['placa']}")


class Painel(Observador):
    def atualizar(self, evento):
        print(f"[PAINEL] vaga liberada (placa {evento['placa']})")


# ---------- O sistema ----------
class Estacionamento:
    def __init__(self):
        self.obs = [Cancela(), Caixa(), Painel()]
        self.d = {}
        self.n = 0

    def entrar(self, placa, tipo, hora_entrada):
        self.d[placa] = (tipo, hora_entrada)
        self.n = self.n + 1

    def processar_saida(self, placa, hora_saida):
        t = self.d[placa][0]
        he = self.d[placa][1]
        h = hora_saida - he
        if h <= 0:
            h = 1
        x = criar_tarifa(t)
        v = x.valor(h)
        evento = {"placa": placa, "tipo": t, "horas": h, "valor": v}
        for o in self.obs:
            o.atualizar(evento)
        del self.d[placa]
        self.n = self.n - 1
        return v

    def previa(self, placa, hora_atual):
        he = self.d[placa][1]
        h = hora_atual - he
        if h <= 0:
            h = 1
        t = self.d[placa][0]
        return criar_tarifa(t).valor(h)


if __name__ == "__main__":
    e = Estacionamento()
    e.entrar("ABC1234", "carro", hora_entrada=8)
    print("prévia às 10h:", e.previa("ABC1234", 10))
    print("--- saída às 11h ---")
    total = e.processar_saida("ABC1234", 11)
    print(f"=> cobrado: R$ {total:.2f}  | carros dentro: {e.n}")
