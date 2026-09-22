# Lucas Maia Orenga | Portfólio de Ciência de Dados

**Projetos TripleTen · Python · Machine Learning · Análise de negócios**

Portfólio com **10 estudos de caso, 11 notebooks e uma apresentação executiva**, cobrindo análise exploratória, testes estatísticos, classificação, regressão, séries temporais, processamento de linguagem natural e visão computacional.

Meu foco nestes projetos é conectar o problema de negócio à análise dos dados, comparar modelos com referências simples e explicar o que os resultados permitem concluir.

[Perfil no GitHub](https://github.com/lutmaia) · [Todos os projetos](#todos-os-projetos) · [Como reproduzir](docs/REPRODUCAO.md)

## Comece por estes projetos

### 1. Steelproof — temperatura do aço

**Integração de dados industriais, validação temporal e apoio à decisão.**

Sete fontes de dados são combinadas para prever a temperatura final de lotes de aço. A solução recorta os atributos no instante em que a previsão seria usada e compara o modelo com a regra de repetir a última leitura disponível.

**Resultado registrado:** CatBoost com **MAE de 3,91 °C**, frente a **5,07 °C** da referência; redução de **22,92%** no erro. A apresentação traduz o desempenho em uma proposta de piloto assistido.

[Ver estudo completo](projetos/17-steelproof-temperatura-aco/) · [Abrir modelagem](projetos/17-steelproof-temperatura-aco/Sprint17_2.ipynb) · [Apresentação executiva](projetos/17-steelproof-temperatura-aco/Sprint17_3.pptx)

### 2. Previsão de demanda de táxis

**Séries temporais, engenharia de atributos e avaliação cronológica.**

Previsão dos pedidos da próxima hora com sazonalidade, defasagens e média móvel. A escolha dos hiperparâmetros usa `TimeSeriesSplit`, respeitando a ordem dos registros.

**Resultado registrado:** LightGBM com **RMSE de 39,07 pedidos**, abaixo da meta de 48 e da referência da hora anterior, de 58,86.

[Ver estudo completo](projetos/13-previsao-demanda-taxis/) · [Abrir notebook](projetos/13-previsao-demanda-taxis/sprint13.ipynb)

### 3. Film Junky Union — sentimentos em resenhas

**Processamento de texto e escolha de uma solução simples.**

Classificação de resenhas em inglês com TF-IDF, regressão logística e comparação com lematização e boosting.

**Resultado disponível nas saídas:** F1 de aproximadamente **0,88** para TF-IDF com regressão logística, acima da meta de 0,85. O README distingue as saídas salvas dos valores relatados apenas na conclusão.

[Ver estudo completo](projetos/14-sentimentos-resenhas-filmes/) · [Abrir notebook](projetos/14-sentimentos-resenhas-filmes/sprint14.ipynb)

### 4. Boa Semente — visão computacional

**Transferência de aprendizado com ResNet50 e análise de generalização.**

Estimativa de idade a partir de fotografias. O estudo combina análise da distribuição etária, aumento de dados e interpretação do treinamento.

**Resultado registrado no log:** MAE de **7,31 anos na validação**. A avaliação evidencia sobreajuste e limites de uso; não foi apresentado um teste independente dessa validação.

[Ver estudo completo](projetos/15-visao-computacional-idade/) · [Abrir notebook](projetos/15-visao-computacional-idade/sprint15.ipynb)

## Todos os projetos

| Sprint | Projeto | Competências demonstradas |
|---|---|---|
| 7 | [Chicago | Análise de corridas e clima](projetos/07-analise-taxis-chicago/) | Análise exploratória de empresas e destinos, com teste de hipótese sobre duração de viagens. |
| 8 | [Telecom | Recomendação de planos](projetos/08-recomendacao-planos/) | Classificação supervisionada para recomendar planos a partir do comportamento de uso. |
| 9 | [Beta Bank | Previsão de churn](projetos/09-churn-bancario/) | Classificação desbalanceada para identificar clientes com maior propensão a deixar o banco. |
| 10 | [OilyGiant | Seleção de região e risco](projetos/10-petroleo-risco-investimento/) | Estudo de regressão e simulação de retorno para seleção de poços de petróleo. |
| 11 | [Seguros | Similaridade e álgebra linear](projetos/11-seguros-algebra-linear/) | Busca de clientes semelhantes, classificação kNN, regressão linear e transformação matricial de atributos. |
| 12 | [Rusty Bargain | Preços de carros usados](projetos/12-precos-carros-usados/) | Regressão tabular com comparação de erro, tempo de treinamento e tempo de previsão. |
| 13 | [Táxis | Previsão de demanda por hora](projetos/13-previsao-demanda-taxis/) | Previsão de séries temporais com atributos de calendário, defasagens e validação cronológica. |
| 14 | [Film Junky Union | Análise de sentimentos](projetos/14-sentimentos-resenhas-filmes/) | Classificação de resenhas em inglês com TF-IDF e comparação entre modelos lineares e boosting. |
| 15 | [Boa Semente | Estimativa de idade em imagens](projetos/15-visao-computacional-idade/) | Transferência de aprendizado com ResNet50, análise das imagens e interpretação das curvas de treinamento. |
| 17 | [Steelproof | Previsão da temperatura do aço](projetos/17-steelproof-temperatura-aco/) | Modelagem industrial com integração de sete fontes, recorte temporal de atributos e tradução dos resultados para a operação. |

## Ferramentas e competências

- **Análise e estatística:** pandas, NumPy, SciPy, visualização e testes de hipóteses.
- **Machine learning:** scikit-learn, LightGBM, CatBoost, baselines e seleção de hiperparâmetros.
- **Séries temporais:** decomposição, defasagens e validação temporal.
- **Texto:** TF-IDF, NLTK, spaCy e análise de sentimentos.
- **Imagens:** TensorFlow/Keras e transferência de aprendizado com ResNet50.
- **Comunicação:** interpretação de métricas, limites dos experimentos e apresentação de conclusões de negócio.

## Como explorar

Cada pasta contém um README com problema, método, resultados, limitações e instruções de execução, além dos notebooks originais e de sua lista de dependências.

Para conhecer o trabalho, basta abrir os notebooks pelo GitHub: as saídas e os gráficos existentes foram preservados. Para executar, siga o [guia de reprodução](docs/REPRODUCAO.md) e o README do projeto escolhido.

## Dados e resultados

Os datasets não estavam junto aos arquivos recebidos e não estão incluídos no repositório. As métricas vêm das saídas ou dos relatos identificados nos notebooks. **OilyGiant foi corrigido e reexecutado em 22/09/2026**, com os datasets do curso, resultados atualizados e quatro testes de regressão. Os demais modelos não foram retreinados na organização deste portfólio.

As limitações metodológicas observadas estão descritas nos READMEs. Os destaques consideram completude, diversidade de técnicas e clareza da ligação com o negócio.

Os estudos são educacionais. Estimativas de retorno ou economia representam cenários dos exercícios, sem comprovação de impacto em produção. Enunciados, dados e marcas pertencem aos respectivos titulares.

## Autor

**Lucas Maia Orenga** · [@lutmaia](https://github.com/lutmaia)

Projetos desenvolvidos durante a formação em Ciência de Dados da TripleTen.
