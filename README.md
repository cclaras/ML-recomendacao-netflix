#  Sistema de Recomendação Netflix com K-Nearest Neighbors

Um pipeline de dados automatizado que processa o catálogo da Netflix e recomenda títulos semelhantes com base em características de gênero, tipo e classificação indicativa utilizando Machine Learning.

##  Tecnologias Utilizadas
* **Python (Pandas & Scikit-Learn):** Tratamento de dados, binarização de variáveis (One-Hot Encoding) e treinamento do algoritmo KNN.
* **Apache Airflow:** Orquestração do pipeline de extração e transformação dos dados.
* **Docker:** Conteinerização da infraestrutura, garantindo um ambiente padronizado para o servidor web, agendador e bancos de dados.
* **PostgreSQL & Redis:** Bancos de dados de suporte para o ecossistema do Airflow.

## Como a Inteligência Funciona
O modelo foi treinado localmente utilizando o algoritmo **K-Nearest Neighbors (KNN)** com a métrica de distância por cosseno (`cosine`). Em vez de recomendar títulos por popularidade, o sistema transforma as características dos filmes em vetores matemáticos e calcula a proximidade entre eles no espaço multidimensional, sugerindo os 3 "vizinhos mais próximos" do título escolhido pelo usuário.

## ⚙️ Arquitetura do Projeto
1. **Extração e Carga:** O Airflow lê o arquivo original `netflix_titles.csv`.
2. **Transformação (EDA):** Limpeza de valores nulos e estruturação das variáveis categóricas.
3. **Treinamento:** Geração da matriz de características e salvamento do modelo em um arquivo `.pkl` físico utilizando a biblioteca `joblib`.

## Como Executar Localmente

### Pré-requisitos
* Docker e Docker Compose instalados.
* Git para clonar o repositório.

### Passo a Passo
1. Clone este repositório:
   ```bash
   git clone [https://github.com/cclaras/ML-recomendacao-netflix.git](https://github.com/cclaras/ML-recomendacao-netflix.git)
   cd ML-recomendacao-netflix

2. Suba a infraestrutura em segundo plano:
   ```bash
   docker compose up -d
   
3. Acesse a interface do Airflow:
```bash
   Abra o navegador em http://localhost:8080
   Usuário: airflow | Senha: airflow
````

4. Para desligar o ecossistema após o uso:
````Bash
   docker compose down
````

*Desenvolvido por Clara Porto. Conecte-se comigo no [LinkedIn](https://www.linkedin.com/in/clara-porto-0333b9302/).*



