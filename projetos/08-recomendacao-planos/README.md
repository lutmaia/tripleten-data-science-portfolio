# Telecom | Recomendação de planos

**Sprint 8 · Ciência de Dados · TripleTen**

Classificação supervisionada para recomendar planos a partir do comportamento de uso.

[Voltar ao portfólio](../../README.md) · [Guia de reprodução](../../docs/REPRODUCAO.md)

## Problema de negócio

Prever a classe `is_ultra` com dados de utilização do serviço e comparar o modelo com a escolha da classe mais frequente.

## Método

1. Separação dos dados em 60% treino, 20% validação e 20% teste.
2. Busca de profundidade de árvore e de parâmetros da floresta aleatória.
3. Comparação com regressão logística.
4. Retreinamento da floresta selecionada em treino + validação e avaliação contra DummyClassifier.

## Resultados

| Modelo no teste | Acurácia |
|---|---:|
| **Random Forest** | **78,54%** |
| Classe mais frequente | 66,41% |

Ganho observado: **12,13 pontos percentuais**. A floresta escolhida usa 30 árvores e profundidade máxima 9.

**Origem das métricas:** Saídas das células 5 e 6 de `sprint8.ipynb`. Os números são históricos, preservados nos arquivos recebidos; os modelos não foram retreinados na preparação deste portfólio.

## Interpretação

O classificador supera a referência majoritária na partição de teste e ilustra um fluxo simples de seleção e avaliação de modelos.

## Arquivos

- [sprint8.ipynb](sprint8.ipynb)

## Como executar

Abra um terminal nesta pasta e use um ambiente Python compatível com as dependências do projeto:

```bash
python -m venv .venv
```

Ative com `.venv\Scripts\activate.bat` no Prompt de Comando do Windows ou `source .venv/bin/activate` no Linux/macOS. Em seguida:

```bash
python -m pip install -r requirements.txt
python -m jupyterlab
```

Os dados originais **não acompanham o repositório**. Obtenha-os no material do curso, se tiver acesso, e coloque os seguintes itens em `data/`:

- `users_behavior.csv`

Substitua `/datasets/users_behavior.csv` por `data/users_behavior.csv`.

Depois de configurar os caminhos, execute as células na ordem. Para apenas ler os resultados, abra o notebook no GitHub, sem instalar dependências.

## Limitações e próximos passos

- O alvo representa uma classe de plano; não mede satisfação, adequação comercial ou efeito de uma recomendação.
- O ganho de acurácia é descritivo; não foi realizado um teste de significância para a diferença.

## Tecnologias

Python, Jupyter e pandas, scikit-learn.

## Contexto

Projeto educacional desenvolvido por **Lucas Maia Orenga** durante a formação em Ciência de Dados da TripleTen. Enunciados, marcas e dados dos estudos de caso pertencem aos respectivos titulares. O notebook original foi preservado, incluindo comentários, saídas e referências do curso.
