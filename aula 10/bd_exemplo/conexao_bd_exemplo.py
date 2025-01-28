# importar a lib de conexão com o banco de dados

import mysql.connector
from mysql.connector import Error

# fórmula de conexão:
# 1 - conectar com o banco de dados
# 2 - executar queries utilizando o cursor
# 3 - fechar conexão

conn = None
# tentando conectar com o banco de dados

try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='python_db'
    )

    if conn.is_connected():
        print('Conexão com o banco foi estabelecida!')
# executando queries (SQL)

    cursor = conn.cursor() # o cursor é um canal que perite a comunicação

# criando a tabela
    cursor.execute(""" 
                    CREATE TABLE IF NOT EXISTS alunos (
                    id int AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(100) NOT NULL,
                    idade INT NOT NULL DEFAULT 0
                   )
 """)
    
    print('Tabela criada com sucesso.')

    insert_query = 'INSERT INTO alunos(nome, idade) VALUES(%s, %s)' # % condicionais que serão substituídas por qualquer tipo de dado
    dados = [
        ('João da Silva', 20),
        ('Maria Oliveira', 22),
        ('Samus Aaran', 19)
    ]

    cursor.executemany(insert_query, dados) # executemany tem a mesma função, nesse caso, de um forEach()
    conn.commit() # acabou de executar é necessário gravar os dados de uma forma final. impossível voltar atrás
    print(f'{cursor.rowcount} registros inseridos com sucesso.')

    cursor.execute('SELECT * FROM ALUNOS')
    registros = cursor.fetchall()
    print('\n Registros da tabela "alunos": ')
    for registro in registros:
        print(registro)

except Error as e:
    print(f'Erro ao conectar no banco de dados: {e}.')
finally:
    if conn.is_connected():
        conn.close()
        print('Desconexão com o banco de dados realizada com sucesso.')
