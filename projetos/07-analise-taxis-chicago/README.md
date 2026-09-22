# Chicago | Análise de corridas e clima

**Sprint 7 · Ciência de Dados · TripleTen**

Análise exploratória de empresas e destinos, com teste de hipótese sobre duração de viagens.

[Voltar ao portfólio](../../README.md) · [Guia de reprodução](../../docs/REPRODUCAO.md)

## Problema de negócio

Entender a distribuição das corridas de táxi em Chicago e investigar a diferença de duração da rota Loop–O’Hare entre sábados com bom tempo e chuvosos.

## Método

1. Leitura de três arquivos com resultados de consultas SQL fornecidos ao exercício.
2. Verificação de tipos e valores ausentes, com visualização das empresas e bairros mais relevantes.
3. Teste de Levene para avaliar evidência de heterogeneidade de variâncias.
4. Teste t para comparar médias de duração entre os dois grupos de clima.

## Resultados

O teste t registrado apresenta estatística **t = 6,9462** e p-valor abaixo de 0,05, levando à rejeição da hipótese de médias iguais no recorte analisado. O valor exibido como `0.0000` é arredondamento, não probabilidade exatamente zero.

**Origem das métricas:** Saídas das células 13 e 14 de `sprint7.ipynb`. Os números são históricos, preservados nos arquivos recebidos; os modelos não foram retreinados na preparação deste portfólio.

## Interpretação

Os resultados indicam associação entre condições de clima e duração das viagens nessa rota, além de concentração de demanda em algumas empresas e bairros.

## Arquivos

- [sprint7.ipynb](sprint7.ipynb)

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

- `project_sql_result_01.csv`
- `project_sql_result_04.csv`
- `project_sql_result_07.csv`

Substitua os três prefixos `/datasets/` por `data/`.

Depois de configurar os caminhos, execute as células na ordem. Para apenas ler os resultados, abra o notebook no GitHub, sem instalar dependências.

## Limitações e próximos passos

- As consultas SQL originais não estão nesta pasta; o notebook trabalha com os CSVs resultantes.
- Não rejeitar a hipótese do teste de Levene não prova igualdade das variâncias.
- O estudo é observacional e não identifica, isoladamente, um efeito causal da chuva.

## Tecnologias

Python, Jupyter e pandas, matplotlib, scipy.

## Contexto

Projeto educacional desenvolvido por **Lucas Maia Orenga** durante a formação em Ciência de Dados da TripleTen. Enunciados, marcas e dados dos estudos de caso pertencem aos respectivos titulares. O notebook original foi preservado, incluindo comentários, saídas e referências do curso.
