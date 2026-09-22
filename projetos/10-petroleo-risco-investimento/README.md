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

Resultados recalculados em **22/09/2026**, após corrigir a seleção de ocorrências no bootstrap:

| Região | Lucro médio (US$) | Intervalo percentil de 95% (US$) | Risco de prejuízo | Risco abaixo de 2,5%? |
|---|---:|---:|---:|---|
| 0 | 3.961.649,85 | −1.112.155,46 a 9.097.669,42 | 6,9% | Não |
| **1** | **4.560.451,06** | **338.205,09 a 8.522.894,54** | **1,5%** | **Sim** |
| 2 | 4.044.038,67 | −1.633.504,13 a 9.503.595,75 | 7,6% | Não |

**Origem das métricas:** saídas das células 21–22 de `sprint10.ipynb` (índices começando em zero), após execução completa das células de código com os três datasets do curso. O experimento mantém a divisão 75:25, a semente 12345 e as 1.000 reamostragens da versão anterior.

## Correção e validação

A seleção anterior usava os rótulos dos índices para somar as reservas. Como o bootstrap sorteia com reposição, um rótulo podia aparecer várias vezes e expandir novamente a seleção: no teste mínimo, duas ocorrências de volume 100 somavam 400 em vez de 200.

A função agora seleciona por **posição**, mantendo o pareamento entre valor real e previsão. Repetições legitimamente sorteadas permanecem na amostra, mas cada ocorrência selecionada é contabilizada uma única vez.

Foram executados quatro testes de regressão e todas as 13 células de código do notebook. Para conferir a origem dos dados, a função antiga também foi executada sobre as mesmas previsões e reproduziu os lucros e riscos anteriores nas casas publicadas. As versões das dependências e os hashes SHA-256 dos CSVs estão registrados nos metadados do notebook.

## Interpretação

O principal aprendizado é ligar erro preditivo a uma decisão com restrição de risco. A **região 1** é a única que atende ao limite de prejuízo abaixo de 2,5%, além de apresentar o maior lucro médio simulado. A recomendação permanece, mas agora com estimativas corrigidas; as regiões 0 e 2 são descartadas pelo critério de risco.

## Arquivos

- [sprint10.ipynb](sprint10.ipynb)
- [Testes de regressão](tests/test_bootstrap.py)
- [Versões usadas na reexecução](requirements-reproducao.txt)

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

Os dados **não acompanham o repositório**. Baixe-os pelos [links do material do curso](data/README.md) e coloque os seguintes itens em `data/`:

- `geo_data_0.csv`
- `geo_data_1.csv`
- `geo_data_2.csv`

Execute o notebook a partir desta pasta. Ele procura primeiro em `data/` e, na ausência dos arquivos locais, usa `/datasets/`, o caminho da plataforma do curso. O ambiente numérico validado usa Python 3.12.14 e as versões fixadas em `requirements-reproducao.txt`, incluídas por `requirements.txt`.

Execute as células na ordem. Para apenas ler os resultados, abra o notebook no GitHub, sem instalar dependências. Os testes não precisam dos CSVs:

```bash
python -m unittest discover -s tests -v
```

## Limitações e próximos passos

- Lucro e risco são estimativas de simulação condicionadas aos dados, ao modelo e às premissas do exercício; não são resultados observados de uma operação real.
- O exercício usa receitas e custos fixos, sem modelar outras incertezas operacionais.

## Tecnologias

Python, Jupyter e numpy, pandas, scikit-learn.

## Contexto

Projeto educacional desenvolvido por **Lucas Maia Orenga** durante a formação em Ciência de Dados da TripleTen. Enunciados, marcas e dados dos estudos de caso pertencem aos respectivos titulares. Esta versão corrige o bootstrap e atualiza as saídas e a conclusão; a versão anterior permanece no histórico do Git.
