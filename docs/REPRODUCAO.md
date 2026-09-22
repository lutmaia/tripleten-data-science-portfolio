# Reprodução dos projetos

[Voltar ao portfólio](../README.md)

## Leitura sem instalação

Os notebooks mantêm os gráficos, tabelas, logs e textos originais. Eles podem ser lidos pelo GitHub. A apresentação em PowerPoint está na pasta do projeto Steelproof.

## Execução local

1. Baixe ou clone o repositório e entre na pasta do projeto escolhido.
2. Crie um ambiente Python separado para esse projeto, ative-o e instale seu `requirements.txt`.
3. Obtenha os dados originais pelo material do curso, se tiver acesso. Coloque-os na pasta `data/` do projeto, seguindo os nomes do README.
4. Ajuste os caminhos de leitura indicados no README. Os notebooks preservam caminhos da plataforma, como `/datasets/`; eles não são portáveis automaticamente.
5. Inicie `python -m jupyterlab`, selecione o ambiente e execute as células na ordem. Reinicie o kernel antes de uma execução completa.

No Prompt de Comando do Windows:

```bat
python -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
python -m jupyterlab
```

No Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m jupyterlab
```

Os metadados dos notebooks registram Python 3.9.23 no ambiente original. Não foi fornecido um arquivo de versões das bibliotecas. Os `requirements.txt` listam dependências identificadas no código; não fixam um ambiente reproduzido e não garantem compatibilidade com todas as versões atuais. Para repetir exatamente o experimento, recupere as versões do ambiente original e registre-as após uma execução bem-sucedida.

## Requisitos específicos

- **NLP:** baixe `en_core_web_sm` com `python -m spacy download en_core_web_sm`. O notebook solicita stopwords do NLTK e grava cache de lematização.
- **Visão computacional:** o notebook gera um script para treinamento separado. Ajuste também o caminho dentro de `run_str` e execute o script no ambiente de treinamento. É necessário baixar os pesos ImageNet na primeira execução; a execução original usou a plataforma GPU do curso.
- **Steelproof:** os dois notebooks usam os mesmos sete CSVs, mas definem os caminhos de formas diferentes. Ajuste ambos antes de executar.

## Escopo da preparação do portfólio

Os notebooks e a apresentação foram copiados sem alteração de conteúdo. Foram acrescentados READMEs, listas de dependências, pastas de dados documentadas e imagens extraídas de saídas existentes. O PDF pessoal e o compêndio de estudos da pasta de origem não fazem parte dos projetos publicados.

A validação desta preparação cobre estrutura dos notebooks, sintaxe das células Python (com tratamento de magias do Jupyter), correspondência das cópias, links locais da documentação e evidências das métricas citadas. Ela não substitui a execução dos modelos.

## Melhorias para uma próxima versão

- Reexecutar os projetos com dados originais e gerar um arquivo de versões por ambiente.
- Recalcular o bootstrap de OilyGiant com seleção posicional das ocorrências sorteadas.
- Ajustar a imputação de churn exclusivamente no conjunto de treino.
- Separar validação de hiperparâmetros e teste final em preços de carros e kNN de seguros.
- Corrigir o cálculo exibido como R² no projeto de seguros.
- Persistir as saídas finais do estudo de NLP e adicionar teste independente no projeto de imagens.

Esses pontos estão documentados como próximos passos; as métricas antigas não foram substituídas por números de execuções que não ocorreram.

## Contribuições

Sugestões podem ser abertas como issues. Ao propor mudanças nos modelos, informe dados, ambiente, divisão de avaliação e resultados antes/depois. Não inclua credenciais ou datasets sem permissão de redistribuição.
