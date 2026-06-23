# notificador.py — componente com UMA só responsabilidade: enviar avisos.
# Hoje, na academia.py (v1.0), a mensagem é mostrada com print() no meio da regra
# e da tela. Sua tarefa é trazer esse "enviar" para CÁ, para um lugar só.


class Notificador:
    """Cuida apenas de enviar notificações ao aluno."""

    def enviar(self, destinatario, mensagem):
        # TODO: mostre a notificação SEMPRE no mesmo formato:
        #   [WhatsApp para <destinatario>] <mensagem>
        # Dica: um único print(f"...") com {destinatario} e {mensagem} resolve.
        ...
