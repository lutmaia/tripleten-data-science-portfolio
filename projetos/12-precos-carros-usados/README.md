# Rusty Bargain | Preços de carros usados

**Sprint 12 · Ciência de Dados · TripleTen**

Regressão tabular com comparação de erro, tempo de treinamento e tempo de previsão.

[Voltar ao portfólio](../../README.md) · [Guia de reprodução](../../docs/REPRODUCAO.md)

## Problema de negócio

Estimar o valor de mercado de automóveis usados considerando qualidade da previsão e custo de processamento.

## Método

1. Tratamento de valores ausentes e filtragem de preço, potência e ano de registro.
2. Codificação de categorias para modelos tradicionais e categorias nativas no LightGBM.
3. Comparação de regressão linear, árvore, Random Forest e diferentes configurações de LightGBM.
4. Registro do RMSE e dos tempos de treinamento e previsão.

## Resultados

| Modelo | RMSE registrado | Treinamento |
|---|---:|---:|
| **LightGBM: 500 estimadores** | **1.536,34** | 9,31 s |
| Random Forest: 80 árvores | 1.636,20 | 13,52 s |
| Regressão linear | 2.953,27 | 0,04 s |

Tempos relativos ao ambiente da execução original; não são benchmarks desta máquina.

**Origem das métricas:** Tabela salva na célula 24 de `sprint12.ipynb`. Os números são históricos, preservados nos arquivos recebidos; os modelos não foram retreinados na preparação deste portfólio.

## Interpretação

O LightGBM teve o menor erro na comparação registrada, com treinamento mais rápido que a floresta de 80 árvores.

## Arquivos

- [sprint12.ipynb](sprint12.ipynb)

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

- `car_data.csv`

Na leitura dos dados, substitua `/datasets/car_data.csv` por `data/car_data.csv`.

Depois de configurar os caminhos, execute as células na ordem. Para apenas ler os resultados, abra o notebook no GitHub, sem instalar dependências.

## Limitações e próximos passos

- O mesmo conjunto chamado de teste foi usado para comparar várias configurações; o valor não é uma estimativa final independente da seleção.
- Os filtros removem carros fora das faixas escolhidas; o resultado não representa todos os anúncios.
- O tempo depende de hardware, versões e tamanho da base.

## Tecnologias

Python, Jupyter e numpy, pandas, scikit-learn, lightgbm.

## Contexto

Projeto educacional desenvolvido por **Lucas Maia Orenga** durante a formação em Ciência de Dados da TripleTen. Enunciados, marcas e dados dos estudos de caso pertencem aos respectivos titulares. O notebook original foi preservado, incluindo comentários, saídas e referências do curso.
