import os, pandas as pd
import mysql.connector
from mysql.connector import Error

def definir_arquivo(nome_arquivo):
    diretorio_corrente = os.path.dirname(__file__)
    arq = os.path.join(diretorio_corrente, nome_arquivo)
    return arq

def criar_df(arq):
    df_criminalidade = None
    try:
        df_criminalidade = pd.read_csv(arq, sep=';', encoding='UTF-8')
    except Exception as ex:
        print(f'Erro na leitura do arquivo: {ex}.')
        exit()
    return df_criminalidade

def conectar_bd():
    return mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='tp4_projeto_bloco'
    )

def criar_tabela():
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS tp4_projeto_bloco.dados_criminalidade (
                id INT AUTO_INCREMENT PRIMARY KEY,
                data DATE NOT NULL,
                tipo_crime VARCHAR(50) NOT NULL,
                localizacao VARCHAR(100),
                hora TIME,
                gravidade VARCHAR(15),
                sexo_suspeito VARCHAR(25),
                idade_suspeito VARCHAR(25),
                status_investigacao VARCHAR(15)                       
            ) 
    """)
        conn.commit()
        print('Tabela criada com sucesso')
    except Error as e:
        print(f'Erro na criação da tabela: {e}.')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def inserir_dados(df_criminalidade):
    try:
        conn = conectar_bd()
        cursor = conn.cursor()
        df_criminalidade = df_criminalidade.drop(columns=['ID'])
        dados = []

        for valores in df_criminalidade.values:
            dados.append(tuple(valores))

        query = 'INSERT INTO tp4_projeto_bloco.dados_criminalidade (data, tipo_crime, localizacao, hora, gravidade, sexo_suspeito, idade_suspeito, status_investigacao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
        cursor.executemany(query, dados)
        conn.commit()
        print('Valores inseridos com sucesso.')
    except Error as e:
        print(f'Erro na inserção dos dados: {e}.')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


if (__name__ == '__main__'):
    arquivo_entrada = definir_arquivo('dados_criminalidade.csv')
    df_criminalidade = criar_df(arquivo_entrada)
    criar_tabela()
    inserir_dados(df_criminalidade)