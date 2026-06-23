# Documento de Visão
## Sistema de Check-in — Academia FitPará (UFRA São Miguel)

**Versão:** 1.0

## 1. Problema
A recepção controla matrículas e entradas num caderno: perde aluno, erra o valor
do plano e avisa cada pessoa na mão, uma a uma.

## 2. Solução proposta
Um sistema de linha de comando (CLI) para matricular alunos (com o valor do plano),
registrar check-ins, avisar o aluno por mensagem e listar os alunos do dia.

## 3. Escopo (v1.0)
- Matrícula com plano; check-in; aviso ao aluno; listagem.
- **Fora do escopo:** pagamento, catraca/biometria, vários professores, relatórios.

## 4. Premissas
- Dados em memória (não há persistência entre execuções na v1.0).
- Planos fixos no código: Mensal, Trimestral e Anual.
