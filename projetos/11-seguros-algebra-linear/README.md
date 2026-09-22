# Seguros | Similaridade e álgebra linear

**Sprint 11 · Ciência de Dados · TripleTen**

Busca de clientes semelhantes, classificação kNN, regressão linear e transformação matricial de atributos.

[Voltar ao portfólio](../../README.md) · [Guia de reprodução](../../docs/REPRODUCAO.md)

## Problema de negócio

Avaliar quatro tarefas de uma seguradora: similaridade de clientes, ocorrência de benefício, número de pagamentos e preservação das previsões após transformação dos atributos.

## Método

1. Comparação de vizinhos com distâncias euclidiana e Manhattan, antes e depois do escalonamento.
2. Classificação kNN para diferentes valores de k e comparação com previsões aleatórias.
3. Implementação de regressão linear usando operações matriciais.
4. Demonstração de equivalência das previsões após multiplicação por uma matriz invertível.

## Resultados

| Experimento registrado | Resultado |
|---|---:|
| kNN, k=1, com escala | F1 = 0,966 |
| kNN, k=1, sem escala | F1 = 0,607 |
| Regressão linear | RMSE = 0,34 |

Os valores de k foram comparados na mesma partição. O melhor F1 é resultado exploratório de seleção, não avaliação independente.

**Origem das métricas:** Saídas das células 45, 46, 54 e 55 de `sprint11.ipynb`. Os números são históricos, preservados nos arquivos recebidos; os modelos não foram retreinados na preparação deste portfólio.

## Interpretação

A escala muda fortemente os resultados da busca por vizinhos. A parte matricial demonstra por que uma transformação invertível pode preservar a solução de regressão.

## Arquivos

- [sprint11.ipynb](sprint11.ipynb)

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

- `insurance_us.csv`

Substitua `/datasets/insurance_us.csv` por `data/insurance_us.csv`.

Depois de configurar os caminhos, execute as células na ordem. Para apenas ler os resultados, abra o notebook no GitHub, sem instalar dependências.

## Limitações e próximos passos

- A transformação é reversível e não oferece garantia de anonimização ou segurança criptográfica.
- A função `eval_regressor` aplica raiz quadrada ao R²; a saída rotulada como R2 não deve ser interpretada como o coeficiente R² padrão.
- Seleção de k e ajuste do pré-processamento precisam ser isolados da avaliação final em uma próxima versão.

## Tecnologias

Python, Jupyter e numpy, pandas, seaborn, scikit-learn.

## Contexto

Projeto educacional desenvolvido por **Lucas Maia Orenga** durante a formação em Ciência de Dados da TripleTen. Enunciados, marcas e dados dos estudos de caso pertencem aos respectivos titulares. O notebook original foi preservado, incluindo comentários, saídas e referências do curso.
