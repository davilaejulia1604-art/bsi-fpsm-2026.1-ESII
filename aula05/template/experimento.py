# experimento.py — prove que da para "testar" sem mandar e-mail de verdade
#
# Parte B: complete a classe FakeEmail abaixo (um e-mail "de mentira").
from repositorio.assinantes import RepositorioAssinantes
from servico.newsletter import ServicoNewsletter


# TODO: complete a classe FakeEmail
#   - no __init__:  self.enviados = []
#   - em enviar(self, para, texto):  self.enviados.append(para)
class FakeEmail:
    def __init__(self):
        self.enviados = []

    def enviar(self, para, texto):
        self.enviados.append(para)
    pass   # <- apague o "pass" e escreva o __init__ e o enviar()


if __name__ == "__main__":
    repo = RepositorioAssinantes()
    enviador = FakeEmail()                     # de mentira, no lugar do SMTP
    servico = ServicoNewsletter(repo, enviador)  # injeta o fake
    servico.enviar_edicao("Edicao teste")

    print("Quem receberia:", enviador.enviados)
    # esperado: ['ana@exemplo.com', 'bia@exemplo.com'] — sem e-mail de verdade!
