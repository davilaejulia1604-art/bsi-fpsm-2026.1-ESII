# Aula 9 — Padrões de Projeto

Sistema de hoje: uma **açaiteria de delivery** 🍧. A **teoria** (apostila) e a **atividade** completas estão no **SIGAA** — esta aula é **assíncrona**.

Um **padrão de projeto** é uma **solução nomeada para um problema que se repete**. Aqui, UM sistema só reúne quatro deles:

- **Strategy** — cada forma de **entrega** (moto, bicicleta, retirada) é uma classe que calcula o seu preço.
- **Factory** — `criar_entrega("moto")` traduz um texto na estratégia certa, num lugar só.
- **Observer** — ao confirmar o pedido, vários **avisos** disparam (cliente, cozinha, vendas) sem o emissor conhecê-los um a um.
- **Facade** — a classe `Acaiteria` é a **porta única**: monta as peças e expõe uma operação simples, `finalizar(...)`.

## O que tem aqui
```
aula09/
├── acaiteria.py       ← o sistema com os 4 padrões (Strategy/Factory/Observer/Facade)
└── test_acaiteria.py  ← 6 testes (um por peça) + um # TODO (a sua tarefa, Parte B)
```

Rode `python acaiteria.py` para ver um pedido acontecer de ponta a ponta (o total e os avisos no terminal).

## Como rodar os testes
No terminal do Codespaces (o `pytest` já vem instalado):
```bash
cd aula09
pytest
```
Você verá **`6 passed`**. Depois de completar a Parte B (a entrega por **drone**), verá **`7 passed`**.

## A tarefa (resumo)
Adicione **uma forma de entrega nova** — o **drone** — seguindo o molde das outras: crie a classe `EntregaDrone` (Strategy), registre-a em `criar_entrega` (Factory) e escreva **um teste** para ela. O passo a passo está na **Parte B** (SIGAA).
