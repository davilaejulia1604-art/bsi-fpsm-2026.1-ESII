# Documento de Requisitos
## Sistema de Check-in — Academia FitPará (UFRA São Miguel)

**Versão:** 1.0

## 1. Requisitos Funcionais
- **RF01 — Matricular aluno:** registrar um aluno com nome e plano.
- **RF02 — Check-in:** registrar a entrada de um aluno já matriculado.
- **RF03 — Avisar o aluno:** enviar uma mensagem (boas-vindas na matrícula;
  confirmação no check-in).
- **RF04 — Listar alunos:** exibir os alunos com plano, valor da mensalidade e
  total de check-ins.

### Regras de negócio
- **RN01:** o valor da mensalidade depende do plano — Mensal R$100; Trimestral R$90; Anual R$80.
- **RN02:** só faz check-in quem já está matriculado.

## 2. Requisitos Não Funcionais (RNF)

> Estes RNF são o **critério para avaliar o projeto desta aula** (aplicar o SRP).

- **RNF01 — Desempenho:** responder a qualquer operação em menos de 1 segundo.
- **RNF02 — Usabilidade:** menu textual claro, mensagens de erro descritivas.
- **RNF03 — Manutenibilidade:** trocar o texto ou o canal do aviso
  (WhatsApp → SMS → e-mail) não deve obrigar a mexer na regra de negócio nem na tela.
  > **Observação do analista:** não atendido na v1.0 (a notificação está grudada na regra e na tela).
- **RNF04 — Testabilidade:** a regra (ex.: o valor do plano) deve poder ser testada
  sem depender do `input()` nem do envio da mensagem.
  > **Observação do analista:** não atendido na v1.0 (a regra está dentro do `input()` e junto do "envio").
- **RNF05 — Extensibilidade:** adicionar um novo tipo de aviso (ex.: e-mail, relatório)
  não deve exigir mexer em todo o sistema.
  > **Observação do analista:** não atendido na v1.0 (uma classe só faz tudo).
