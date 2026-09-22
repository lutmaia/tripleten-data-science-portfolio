# Beta Bank | Previsão de churn

**Sprint 9 · Ciência de Dados · TripleTen**

Classificação desbalanceada para identificar clientes com maior propensão a deixar o banco.

[Voltar ao portfólio](../../README.md) · [Guia de reprodução](../../docs/REPRODUCAO.md)

## Problema de negócio

Prever a saída de clientes, com meta de F1 de pelo menos 0,59 e avaliação adicional por ROC AUC.

## Método

1. Exploração dos dados, tratamento de Tenure e remoção de identificadores.
2. Separação estratificada em treino, validação e teste, com padronização ajustada no treino.
3. Comparação de árvores, Random Forest e regressão logística.
4. Avaliação de upsampling e pesos de classe, seguida de análise de importância das variáveis.

## Resultados

| Métrica no teste | Resultado registrado |
|---|---:|
| **F1** | **0,5985** |
| ROC AUC | 0,8474 |

Configuração selecionada: Random Forest, 50 árvores, profundidade máxima 10 e upsampling com fator 5.

**Origem das métricas:** Saída da célula 40 de `sprint9.ipynb`. Os números são históricos, preservados nos arquivos recebidos; os modelos não foram retreinados na preparação deste portfólio.

## Interpretação

O resultado supera o limiar de F1 do exercício e demonstra o uso de métricas adequadas a classes desbalanceadas. Uma aplicação de retenção ainda precisaria considerar custos de contato e de falsos positivos.

## Arquivos

- [sprint9.ipynb](sprint9.ipynb)

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

- `Churn.csv`

Substitua `/datasets/Churn.csv` por `data/Churn.csv`, preservando a inicial maiúscula do nome.

Depois de configurar os caminhos, execute as células na ordem. Para apenas ler os resultados, abra o notebook no GitHub, sem instalar dependências.

## Limitações e próximos passos

- A mediana de Tenure é calculada antes da divisão da base. Para uma avaliação estritamente isolada, a imputação deve ser ajustada apenas no treino e o experimento reexecutado.
- Não há avaliação financeira de campanha de retenção ou teste em produção.

## Tecnologias

Python, Jupyter e numpy, pandas, matplotlib, seaborn, scikit-learn.

## Contexto

Projeto educacional desenvolvido por **Lucas Maia Orenga** durante a formação em Ciência de Dados da TripleTen. Enunciados, marcas e dados dos estudos de caso pertencem aos respectivos titulares. O notebook original foi preservado, incluindo comentários, saídas e referências do curso.
