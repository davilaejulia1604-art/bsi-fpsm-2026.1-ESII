# academia.py — Sistema da Academia FitPará (v1.0) — TUDO numa classe só
# A classe Academia faz, ao mesmo tempo, TRÊS coisas diferentes:
#   (1) REGRA DE NEGÓCIO — calcular o valor do plano e contar os check-ins
#   (2) TELA (interface)  — menu, ler o que o usuário digita, mostrar o resultado
#   (3) NOTIFICAÇÃO       — "enviar" o aviso de WhatsApp ao aluno
# Funciona — mas tudo está grudado, e os dados são dicionários soltos.


class Academia:
    def __init__(self):
        self.alunos = []        # cada aluno é um dicionário solto
        self.proximo_id = 1

    def matricular(self):
        # (2) TELA: lê os dados digitados
        nome = input("Nome do aluno: ")
        print("Planos: 1-Mensal  2-Trimestral  3-Anual")
        plano = input("Plano: ")

        # (1) REGRA DE NEGÓCIO: o valor da mensalidade depende do tipo de plano
        if plano == "1":
            valor = 100.0
        elif plano == "2":
            valor = 90.0
        elif plano == "3":
            valor = 80.0
        else:
            print("Plano inválido.")
            return

        aluno = {"id": self.proximo_id, "nome": nome, "plano": plano, "checkins": 0}
        self.alunos.append(aluno)
        self.proximo_id += 1

        # (3) NOTIFICAÇÃO: envia o aviso de boas-vindas
        print(f"[WhatsApp para {nome}] Bem-vindo(a) à FitPará! Mensalidade: R${valor:.2f}.")

        # (2) TELA: confirma na tela
        print(f"Aluno {aluno['id']} matriculado.")

    def check_in(self):
        # (2) TELA
        nome = input("Nome do aluno: ")
        # (1) REGRA: encontra o aluno e conta o check-in
        aluno = None
        for a in self.alunos:
            if a["nome"] == nome:
                aluno = a
                break
        if aluno is None:
            print("Aluno não encontrado.")
            return
        aluno["checkins"] += 1
        # (3) NOTIFICAÇÃO
        print(f"[WhatsApp para {nome}] Check-in confirmado! Bom treino.")
        # (2) TELA
        print(f"Check-in de {nome} registrado. Total: {aluno['checkins']}.")

    def listar(self):
        # (2) TELA + (1) REGRA recalculada AQUI de novo (duplicada!)
        print("--- Alunos ---")
        for a in self.alunos:
            if a["plano"] == "1":
                valor = 100.0
            elif a["plano"] == "2":
                valor = 90.0
            else:
                valor = 80.0
            print(f"{a['id']}- {a['nome']}  (R${valor:.2f}/mês, {a['checkins']} check-ins)")


def main():
    app = Academia()
    while True:
        print("\n1-Matricular  2-Check-in  3-Listar  0-Sair")
        op = input("Opção: ")
        if op == "1":   app.matricular()
        elif op == "2": app.check_in()
        elif op == "3": app.listar()
        elif op == "0": break


if __name__ == "__main__":
    main()
