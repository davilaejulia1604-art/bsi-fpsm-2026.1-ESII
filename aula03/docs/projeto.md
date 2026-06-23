# Documento de Projeto
## Sistema de Check-in — Academia FitPará

**Versão:** 1.0

## 1. Estrutura atual (v1.0)
```
aula03/
└── academia.py    ← uma única classe faz regra + tela + notificação; dados em dicts
```

## 2. Decisão pendente
A v1.0 amontoa **três responsabilidades** numa classe só (regra de negócio, tela e
notificação). A decisão desta aula é aplicar o **SRP** (Princípio da Responsabilidade
Única): separar cada responsabilidade em um componente próprio, e trocar os
dicionários soltos por **dataclasses** tipadas.

O esqueleto para você **extrair o Notificador** (o primeiro passo do SRP) está em `template/`.
