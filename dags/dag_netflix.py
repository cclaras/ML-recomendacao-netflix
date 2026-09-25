from airflow.decorators import dag, task # o airflow serve para agendar o código
from datetime import datetime
import pandas as pd

# 1. definir as regras de funcionamento
@dag(
    schedule_interval='@daily', # rode 1x no dia
    start_date=datetime(2024, 1, 1), # rode a partir de
    catchup=False, # trava para nao contar literalmente desde 2024
    tags=['netflix', 'limpeza'] 
)
def pipeline_netflix():

    # 2. colocar o EDA (só oq vou usar)
    @task
    def processar_dados():
        print("Iniciando a leitura dos dados...")
        
        # O docker mapeia a dags para este caminho:
        caminho_origem = '/opt/airflow/dags/netflix_titles.csv'
        caminho_destino = '/opt/airflow/dags/netflix_modelo.csv'
        
        # lê o arquivo
        df = pd.read_csv(caminho_origem)

        print("Limpando os dados...")
        # limpeza de nulos e drop
        df = df.set_index('show_id')
        df = df.drop(columns=['description'])
        df['director'] = df['director'].fillna('Unknown')
        df['cast'] = df['cast'].fillna('Unknown')
        df['country'] = df['country'].fillna('Unknown')
        df['rating'] = df['rating'].fillna('Unknown')

        # limpeza de data
        df = df.dropna(subset=['date_added'])
        df['date_added'] = df['date_added'].str.strip()
        df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

        # correção da duração (usando mask)
        mask = df['rating'].str.contains('min', na=False)
        df.loc[mask, 'duration'] = df.loc[mask, 'rating']
        df.loc[mask, 'rating'] = 'Unknown'

        print("Aplicando Engenharia de Variáveis (Binarização)...")
        # transformando type em binário
        df['is_movie'] = df['type'].apply(lambda x: 1 if x == 'Movie' else 0)
        
        # binarizando gêneros (one hot encoding)
        df_generos_binarios = df['listed_in'].str.get_dummies(sep=', ')
        
        # juntando a tabela final
        df_modelo = pd.concat([df[['title', 'is_movie']], df_generos_binarios], axis=1)

        # salvando o resultado final
        df_modelo.to_csv(caminho_destino, index=False)
        print("Sucesso! Tabela salva e pronta para o Machine Learning.")

    # 3. executar a tarefa
    processar_dados()

# 4. airflow
dag_netflix = pipeline_netflix()
