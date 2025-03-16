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

def gravar_json(query, arq):
    try:
        conn = conectar_bd()
        df = pd.read_sql(query, conn)
        df.to_json(arq, orient='records', indent=4, force_ascii=False)
        print(f'Arquivo {arq} criado com sucesso.')
    except Error as e:
        print(f'Erro na criação do arquivo: {e}.')
    finally:
        if conn.is_connected():
            conn.close()

if (__name__ == '__main__'):
    arquivo_entrada = definir_arquivo('dados_criminalidade.csv')
    df_criminalidade = criar_df(arquivo_entrada)
    criar_tabela()
    #inserir_dados(df_criminalidade)
    
    query_1 = """ SELECT COUNT(id) AS total_crimes_mes_marco
            FROM tp4_projeto_bloco.dados_criminalidade
            WHERE MONTH(data) = 03; """
    json_1 = definir_arquivo('questao_1.json')
    gravar_json(query_1, json_1)
    
    query_2 = """ SELECT
    tipo_crime AS tipo_crime_mais_frequente,
    localizacao,
    COUNT(tipo_crime) AS quantidade
    FROM tp4_projeto_bloco.dados_criminalidade
    WHERE localizacao = 'Vieira'
    GROUP BY tipo_crime, localizacao
    ORDER BY quantidade DESC
    LIMIT 1; """
    json_2 = definir_arquivo('questao_2.json')
    gravar_json(query_2, json_2)

    query_3 = """ SELECT
	COUNT(id) AS crimes_concluidos
    FROM tp4_projeto_bloco.dados_criminalidade
    WHERE status_investigacao = 'Concluído'; """
    json_3 = definir_arquivo('questao_3.json')
    gravar_json(query_3, json_3)

    query_4 = """ SELECT
	CAST(idade_suspeito AS UNSIGNED) AS idade_mais_comum,
    COUNT(*) AS repeticoes
    FROM tp4_projeto_bloco.dados_criminalidade
    WHERE idade_suspeito REGEXP '^[0-9]+$'
    GROUP BY idade_mais_comum
    ORDER BY repeticoes DESC
    LIMIT 1; """
    json_4 = definir_arquivo('questao_4.json')
    gravar_json(query_4, json_4)

    query_5 = """ SELECT
	tipo_crime,
    CASE
		WHEN HOUR(hora) BETWEEN 0 AND 5 THEN 'Madrugada'
        WHEN HOUR(hora) BETWEEN 6 AND 11 THEN 'Manhã'
        WHEN HOUR(hora) BETWEEN 12 AND 17 THEN 'Tarde'
        WHEN HOUR(hora) BETWEEN 18 AND 23 THEN 'Noite'
	END AS periodo_dia,
    COUNT(*) AS quantidade_crimes
    FROM tp4_projeto_bloco.dados_criminalidade
    WHERE hora IS NOT NULL
    GROUP BY tipo_crime, periodo_dia
    ORDER BY quantidade_crimes DESC; """
    json_5 = definir_arquivo('questao_5.json')
    gravar_json(query_5, json_5)

    query_6 = """ SELECT
	CASE
		WHEN gravidade = 'Leve' THEN 'Não Violento'
		WHEN gravidade = 'Moderada' THEN 'Violento'
        WHEN gravidade = 'Grave' THEN 'Violento'
        WHEN gravidade = 'Crítica' THEN 'Violento'
	END AS gravidade_crime,
    CONCAT(ROUND((COUNT(*) / (SELECT COUNT(*) FROM tp4_projeto_bloco.dados_criminalidade) * 100), 2), '%') AS percentual
    FROM tp4_projeto_bloco.dados_criminalidade
    GROUP BY gravidade_crime; """
    json_6 = definir_arquivo('questao_6.json')
    gravar_json(query_6, json_6)