# OilyGiant | Seleção de região e risco

**Sprint 10 · Ciência de Dados · TripleTen**

Estudo de regressão e simulação de retorno para seleção de poços de petróleo.

[Voltar ao portfólio](../../README.md) · [Guia de reprodução](../../docs/REPRODUCAO.md)

## Problema de negócio

Comparar três regiões para selecionar 200 poços, considerando orçamento de US$ 100 milhões e limite de risco de prejuízo de 2,5%.

## Método

1. Regressão linear por região com separação entre treino e validação.
2. Cálculo do volume de equilíbrio e seleção por reservas previstas.
3. Simulação de 1.000 amostras de 500 pontos com reposição.
4. Comparação de lucro médio, intervalo percentil de 95% e frequência de prejuízo.

## Resultados

O notebook recomenda a região 1 e registra lucro médio de US$ 6,65 milhões e risco de 0,3%. **Esses números precisam ser recalculados antes de serem usados como resultado validado de portfólio.**

Na implementação atual, a amostragem com reposição mantém índices duplicados e `target[indices_top]` seleciona por rótulo. Isso pode repetir registros além das ocorrências sorteadas e distorcer os lucros. Os valores originais foram preservados como histórico do exercício.

**Origem das métricas:** Funções `calcular_lucro` e `bootstrap_lucro` e saídas das células 21–22 de `sprint10.ipynb`. Os números são históricos, preservados nos arquivos recebidos; os modelos não foram retreinados na preparação deste portfólio.

## Interpretação

O principal aprendizado é ligar erro preditivo a uma decisão com restrição de risco. Antes de sustentar a escolha de região, é necessário corrigir o alinhamento posicional das amostras e repetir a simulação com os dados originais.

## Arquivos

- [sprint10.ipynb](sprint10.ipynb)

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

- `geo_data_0.csv`
- `geo_data_1.csv`
- `geo_data_2.csv`

Troque os três prefixos `/datasets/` por `data/`. Para uma nova análise, revise a seleção do bootstrap de modo que cada ocorrência sorteada tenha uma posição única e mantenha o pareamento entre valor real e previsão.

Depois de configurar os caminhos, execute as células na ordem. Para apenas ler os resultados, abra o notebook no GitHub, sem instalar dependências.

## Limitações e próximos passos

- Revisão pendente da seleção com índices duplicados no bootstrap; resultados financeiros históricos não foram validados nesta organização.
- O exercício usa receitas e custos fixos, sem modelar outras incertezas operacionais.

## Tecnologias

Python, Jupyter e numpy, pandas, scikit-learn.

## Contexto

Projeto educacional desenvolvido por **Lucas Maia Orenga** durante a formação em Ciência de Dados da TripleTen. Enunciados, marcas e dados dos estudos de caso pertencem aos respectivos titulares. O notebook original foi preservado, incluindo comentários, saídas e referências do curso.
