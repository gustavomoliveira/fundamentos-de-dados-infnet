# faça um programa em python que o usa o mysql para gerenciar alunos,
# calcular médias e gerar um relatório indicando se eles foram
# aprovados, recuperação ou reprovados

import mysql.connector
from mysql.connector import Error

# função para conectar ao BD. retorna a conexão ativa com o BD

def conectar_mysql():
    return mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='exercicio_pb'
    )

# função para cadastro de alunos
def inserir_aluno(nome, nota1, nota2, nota3):
    try:
        conn = conectar_mysql()
        cursor = conn.cursor() # cria o cursor
        query = 'INSERT INTO alunos (nome, nota1, nota2, nota3) VALUES (%s, %s, %s, %s)' # cria a query
        cursor.execute(query, (nome, nota1, nota2, nota3)) # executa a query
        conn.commit() # realiza o commit
        print(f'Aluno {nome} inserido com sucesso!')
    except Error as e:
        print(f'Erro ao inserir o aluno: {e}')
    finally:
        if(conn.is_connected()):
            cursor.close()
            conn.close()

# função para calcular situação do aluno e sua média
def gerar_relatorio():
    try:
        conn = conectar_mysql()
        cursor = conn.cursor()
        query = 'SELECT * FROM exercicio_pb.alunos'
        cursor.execute(query)
        alunos = cursor.fetchall() # retorna o resultado para a memória
        
        print('\nRelatório de Alunos:')
        print('-' * 50)
        
        for aluno in alunos:
            id, nome, nota1, nota2, nota3 = aluno # destructuring, mesmo de JS
            media = (nota1 + nota2 + nota3) / 3
            situacao = ''
            if media >= 7.0:
                situacao = 'Aprovado'
            elif 5.0 <= media < 7.0:
                situacao = 'Recuperação'
            else:
                situacao = 'Reprovado'
            print(f'Id: {id} - Nome: {nome} | Média: {media:.2f} | Situação: {situacao}')
    except Error as e:
        print(f'Erro ao gerar o relatório: {e}')
    finally:
        if(conn.is_connected()):
            cursor.close()
            conn.close()

# main
if (__name__ == '__main__'):
    inserir_aluno('João Silva', 8.0, 7.5, 9.0)
    inserir_aluno('Maria Souza', 6.0, 5.5, 6.5)
    inserir_aluno('Carlos Santos', 4.0, 5.0, 4.5)
    gerar_relatorio()