# Boa Semente | Estimativa de idade em imagens

**Sprint 15 · Ciência de Dados · TripleTen**

Transferência de aprendizado com ResNet50, análise das imagens e interpretação das curvas de treinamento.

[Voltar ao portfólio](../../README.md) · [Guia de reprodução](../../docs/REPRODUCAO.md)

## Problema de negócio

Estimar idade a partir de fotografias e avaliar os limites dessa previsão como apoio ao atendimento no varejo.

## Método

1. Análise da distribuição etária e inspeção de imagens.
2. ResNet50 com pesos ImageNet, GlobalAveragePooling2D e saída de regressão.
3. Redimensionamento para 224 × 224, normalização e aumento de dados por espelhamento no treino.
4. Treinamento por 20 épocas e análise do desvio entre erro de treino e validação.

## Resultados

| Indicador do log de treinamento | Valor |
|---|---:|
| MAE de validação na última época | **7,31 anos** |
| Meta do exercício | até 8 anos |
| Imagens de treinamento | 5.694 |
| Imagens de validação | 1.897 |

O notebook chama essa partição de teste em alguns trechos, mas `load_test()` usa `subset="validation"` e o conjunto acompanha o treinamento. O valor é apresentado aqui como **validação**, não como um teste final independente.

**Origem das métricas:** Log copiado na célula Markdown 36 e funções `load_train` e `load_test` de `sprint15.ipynb`. Os números são históricos, preservados nos arquivos recebidos; os modelos não foram retreinados na preparação deste portfólio.

## Interpretação

O exercício demonstra transferência de aprendizado e análise de sobreajuste. O erro observado não sustenta decisões automáticas de verificação de idade.

## Arquivos

- [sprint15.ipynb](sprint15.ipynb)

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

- `faces/labels.csv`
- `faces/final_files/`

Mantenha a estrutura `data/faces/labels.csv` e `data/faces/final_files/`. Ajuste `caminho` e o `path` dentro de `run_str` para `data/faces/`. O notebook define funções e gera `run_model_on_gpu.py`; o treinamento é executado separadamente nesse script. Pesos ImageNet são baixados na primeira execução. O fluxo original foi preparado para uma plataforma com GPU.

Depois de configurar os caminhos, execute as células na ordem. Para apenas ler os resultados, abra o notebook no GitHub, sem instalar dependências.

## Limitações e próximos passos

- O log de GPU foi incorporado ao notebook como texto; não há pesos treinados nesta entrega.
- A partição de validação é consultada durante o treinamento; falta uma avaliação final independente.
- Há desequilíbrio etário e distância relevante entre erro de treino e validação.

## Tecnologias

Python, Jupyter e numpy, pandas, matplotlib, pillow, tensorflow.

## Contexto

Projeto educacional desenvolvido por **Lucas Maia Orenga** durante a formação em Ciência de Dados da TripleTen. Enunciados, marcas e dados dos estudos de caso pertencem aos respectivos titulares. O notebook original foi preservado, incluindo comentários, saídas e referências do curso.
