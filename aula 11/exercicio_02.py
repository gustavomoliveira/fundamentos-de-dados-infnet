""" Faça um programa em Python para gerenciamento de funcionários usando o MySQL.
Ele permite cadastrar funcionários, atualizar informações, listar dados e calcular
os salários com base em suas jornadas de trabalho e valor por hora. """

import mysql.connector
from mysql.connector import Error

def conectar_mysql():
    return mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='exercicio_pb'
    )

def inserir_funcionario(nome, cargo, horas_trabalhadas, valor_hora):
    try:
        conn = conectar_mysql()
        cursor = conn.cursor()
        query = 'INSERT INTO funcionarios (nome, cargo, horas_trabalhadas, valor_hora) VALUES (%s, %s, %s, %s)'
        cursor.execute(query, (nome, cargo, horas_trabalhadas, valor_hora))
        conn.commit()
        print(f'Funcionário {nome} inserido com sucesso.')
    except Error as e:
        print(f'Erro ao inserir funcionário: {e}')
    finally:
        if(conn.is_connected()):
            cursor.close()
            conn.close()

def atualizar_funcionario(id_funcionario, cargo=None, horas_trabalhadas=None, valor_hora=None):
    try:
        conn = conectar_mysql()
        cursor = conn.cursor()
        updates = []
        valores = []

        if cargo:
            updates.append('cargo = %s')
            valores.append(cargo)
        if horas_trabalhadas is not None:
            updates.append('horas_trabalhadas = %s')
            valores.append(horas_trabalhadas)
        if valor_hora is not None:
            updates.append('valor_hora = %s')
            valores.append(valor_hora)

        valores.append(id_funcionario)
        query = f'UPDATE funcionarios SET {", ".join(updates)} WHERE id = %s'
        cursor.execute(query, tuple(valores))
        conn.commit( )
        print(f'Funcionário com ID {id_funcionario} atualizado com sucesso!')
    except Error as e:
        print(f'Erro ao atualizar funcionário: {e}')
    finally:
        if(conn.is_connected()):
            cursor.close()
            conn.close()

def listar_funcionarios():
    try:
        conn = conectar_mysql()
        cursor = conn.cursor()
        cursor.execute('SELECT id, nome, cargo, horas_trabalhadas, valor_hora FROM funcionarios')
        funcionarios = cursor.fetchall()

        print('\nLista de Funcionários:')
        print('-' * 60)
        for funcionario in funcionarios:
            print(f"ID: {funcionario[0]} | Nome: {funcionario[1]} | Cargo: {funcionario[2]} |"
                f"Horas Trabalhadas: {funcionario[3]} | Valor/Hora: R${funcionario[4]:.2f}")
    except Error as e:
        print(f"Erro ao listar funcionários: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn. close()

def calcular_salario():
    try:
        conn = conectar_mysql()
        cursor = conn.cursor()
        query = 'SELECT * FROM exercicio_pb.funcionarios'
        cursor.execute(query)
        funcionarios = cursor.fetchall()

        print('\nCálculo de Salários:')
        print('-' * 60)

        for funcionario in funcionarios:
            id, nome, cargo, horas_trabalhadas, valor_hora = funcionario
            salario = (horas_trabalhadas * valor_hora) * 4
            print(f'Id: {id} - Nome: {nome} | Cargo: {cargo} | Salário: R${salario:.2f}')
    except Error as e:
        print(f'Erro ao calcular os salários: {e}')
    finally:
        if(conn.is_connected()):
            cursor.close()
            conn.close()

if (__name__ == '__main__'):
    inserir_funcionario('João da Silva', 'Dev', 40, 10)
    inserir_funcionario('Maria Oliveira', 'Dev', 40, 12.5)
    inserir_funcionario('Márcio de Freitas', 'Supervisor', 44, 13)
    inserir_funcionario('Patrícia Torres', 'Marketing', 44, 8)
    inserir_funcionario('Glauco Moraes', 'Gerente de Produto', 44, 10)
    inserir_funcionario('Júlia dos Anjos', 'Marketing', 44, 8)
    inserir_funcionario('Marcos Linhares', 'Gerente de TI', 44, 15)
    listar_funcionarios()
    atualizar_funcionario(1, horas_trabalhadas=41.25)
    listar_funcionarios()
    calcular_salario()

