# Aula 10 — Refactoring, Code Smells e CI/CD

Sistema de hoje: um **estacionamento** 🅿️. A **teoria** está nos slides e a **atividade** está no **SIGAA**.

Este código **funciona e tem testes** — mas está cheio de **code smells** (sinais de código mal cuidado): nomes ruins, um método longo, código duplicado e um **evento como `dict` solto**. O trabalho da aula é **reconhecer** esses smells e **refatorar com segurança** — os testes são a sua rede (Aulas 7–8).

> **Refactoring** = mudar a **estrutura interna** do código por **passos pequenos** que **preservam o comportamento** (Fowler). Regra de ouro: **nunca refatore sem testes**.

## O que tem aqui
```
aula10/
├── estacionamento.py       ← o sistema (funciona, mas cheio de smells p/ refatorar)
├── test_estacionamento.py  ← 11 testes que passam — a sua rede de segurança
├── pyproject.toml          ← config do linter (ruff)
└── ci.yml                  ← o pipeline de CI (copie p/ .github/workflows/ no seu fork)
```
Rode `python estacionamento.py` para ver um carro entrar e sair.

## Como rodar (no Codespaces)
```bash
cd aula10
pytest                       # 11 passed
ruff check .                 # All checks passed  (estilo ok…)
pytest --cov=estacionamento --cov-report=term-missing --cov-fail-under=80
```
O `ruff` fica **verde** — mas o código **ainda cheira mal**: o linter pega **estilo**, não *smells de design*. Esses só o **olho humano** (e o refactoring) resolvem.

## Os smells que moram aqui (você vai caçá-los)
- **Mysterious Name** — nomes que não dizem nada (`obs`, `d`, `n`, `t`, `h`, `x`, `v`).
- **Long Method** — `processar_saida` faz coisa demais (calcula horas, tarifa, monta evento, avisa, mexe no estado).
- **Duplicated Code** — o cálculo das horas (com piso de 1) aparece em dois lugares.
- **Primitive Obsession** — o `evento` é um `dict` solto → vira uma `@dataclass Evento`.
- *Falso positivo:* as subclasses `TarifaCarro/Moto/Caminhao` **parecem** "Data Class", mas são o **custo do Strategy** — essas **não** se refatoram.

## A tarefa (resumo)
**Reconhecer os smells** e aplicar alguns refactorings **com a suíte sempre verde** (renomear, extrair função, e trocar o `dict` por `@dataclass Evento`), e **rodar o pipeline de CI**. O passo a passo está na **atividade** (SIGAA).
