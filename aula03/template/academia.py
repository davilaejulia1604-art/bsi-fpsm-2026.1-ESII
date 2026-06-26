# academia.py (template) — sua tarefa: TIRAR a notificação de dentro desta classe.
# A classe Notificador já existe (vazia) em notificador.py e já vem injetada aqui
# no __init__. Onde havia um print de MENSAGEM AO ALUNO, troque por uma chamada
# ao notificador. Os prints de confirmação na tela ("matriculado", "registrado")
# são TELA — esses ficam.

from notificador import Notificador


class Academia:
    def __init__(self):
        self.alunos = []
        self.proximo_id = 1
        self.notificador = Notificador()   # <- o componente de aviso, pronto para usar

    def matricular(self):
        nome = input("Nome do aluno: ")
        print("Planos: 1-Mensal  2-Trimestral  3-Anual")
        plano = input("Plano: ")

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

        # TODO: troque o aviso de boas-vindas por uma chamada ao notificador.
        #   self.notificador.enviar( <para quem>, <a MESMA mensagem de boas-vindas da v1.0> )
        self.notificador.enviar(nome, f"Bem-vindo, {nome}! Sua matrícula foi realizada com sucesso.")

        print(f"Aluno {aluno['id']} matriculado.")   # TELA: este fica

    def check_in(self):
        nome = input("Nome do aluno: ")
        aluno = None
        for a in self.alunos:
            if a["nome"] == nome:
                aluno = a
                break
        if aluno is None:
            print("Aluno não encontrado.")
            return
        aluno["checkins"] += 1

        # TODO: troque o aviso de confirmação por uma chamada ao notificador.
        #   self.notificador.enviar( <para quem>, <a MESMA mensagem de check-in da v1.0> )
        ...

        print(f"Check-in de {nome} registrado. Total: {aluno['checkins']}.")   # TELA: este fica

    def listar(self):
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
