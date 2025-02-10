import mysql.connector
from mysql.connector import Error
from tabulate import tabulate

def conectar_mysql():
    return mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='empresa'
    )

def consultar_nome_salario():
    try:
        conn = conectar_mysql()
        cursor = conn.cursor()
        cursor.execute('SELECT nome, salario_base FROM empresa.funcionarios')
        funcionarios = cursor.fetchall()
        chaves = ['nome', 'salario_base']
        valores = [[], []]

        for nome, salario in funcionarios:
            valores[0].append(nome)
            valores[1].append(salario)

        dados = dict(zip(chaves, valores))
        return dados
    except Error as e:
        print(f'Erro na seleção: {e}')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def calcular_desconto_inss():
    descontos_inss = []
    for salario_base in dados['salario_base']:
        inss = 0
        faixas = [
            (1412.00, 0.075),
            (2666.68, 0.09),
            (4000.03, 0.12),
            (float('inf'), 0.14)
        ]
        teto_anterior = 0
        for teto, aliquota in faixas:
            if salario_base > teto:
                inss += (teto - teto_anterior) * aliquota
            else:
                inss += (salario_base - teto_anterior) * aliquota
                break
            teto_anterior = teto
        descontos_inss.append(round(inss, 2))
    dados['desconto_inss'] = descontos_inss

def calcular_desconto_ir():
    desconto_ir = []
    ir = 0
    for salario, desconto in zip(dados['salario_base'], dados['desconto_inss']):
        salario_reduzido = salario - desconto
        ir = 0
        if salario <= 2112.00:
            ir = 0
        elif 2112.01 <= salario_reduzido <= 2826.65:
            ir = (salario_reduzido * 0.075) - 158.40
        elif 2826.66 <= salario_reduzido <= 3751.05:
            ir = (salario_reduzido * 0.15) - 370.40
        elif 3751.06 <= salario_reduzido <= 4664.68:
            ir = (salario_reduzido * 0.225) - 651.73
        else:
            ir = (salario_reduzido * 0.275) - 884.96
        desconto_ir.append(round(ir, 2))
    dados['desconto_ir'] = desconto_ir

def calcular_salario_liquido():
    salarios_descontados = []
    for salario, inss, ir in zip(dados['salario_base'], dados['desconto_inss'], dados['desconto_ir']):
        salario_liquido = salario - inss - ir
        salarios_descontados.append(round(salario_liquido, 2))
    dados['salario_liquido'] = salarios_descontados

def inserir_colunas():
    try:
        conn = conectar_mysql()
        cursor = conn.cursor()
        query = 'ALTER TABLE funcionarios ADD COLUMN desconto_inss FLOAT, ADD COLUMN desconto_ir FLOAT, ADD COLUMN salario_liquido FLOAT'
        cursor.execute(query)
        conn.commit()
        print('Colunas adicionadas com sucesso.')
    except Error as e:
        print(f'Colunas já existem: {e}')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def inserir_valores():
    try:
        conn = conectar_mysql()
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM empresa.funcionarios')
        ids = cursor.fetchall()
        lista_ids = []
        for id in ids:
            lista_ids.append(id[0])

        if len(dados['desconto_inss']) == len(dados['desconto_ir']) == len(dados['salario_liquido']) == len(lista_ids):
            valores = list(zip(dados['desconto_inss'], dados['desconto_ir'], dados['salario_liquido'], lista_ids))
            update = f'UPDATE empresa.funcionarios SET desconto_inss = %s, desconto_ir = %s, salario_liquido = %s WHERE id = %s'
            cursor.executemany(update, valores)
            conn.commit()
            print('Dados inserido com sucesso.')
        else:
            print('As colunas não possuem o mesmo número de valores.')
    except Error as e:
        print(f'Erro ao inserir dados: {e}')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def exibir_relatorio():
    try: 
        conn = conectar_mysql()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM empresa.funcionarios ORDER BY salario_liquido DESC')
        todos_dados = cursor.fetchall()
        dados_tabela = []
        colunas_ordenadas = [0, 1, 2, 3, 5, 4, 6, 7, 8]
        
        for dado in todos_dados:
            linhas_ordenadas = []
            for i in colunas_ordenadas:
                linhas_ordenadas.append(dado[i])
            dados_tabela.append(linhas_ordenadas)
        
        print(tabulate(dados_tabela, headers=['ID', 'Nome', 'Cargo', 'Departamento', 'Data de Admissão', 'Salário Base', 'Desc. INSS', 'Desc. IR', 'Salário Líquido'], tablefmt='rounded_outline', stralign='center', numalign='center'))
    except Error as e:
        print(f'Erro ao exibir os dados: {e}')
    finally:
        if(conn.is_connected()):
            cursor.close()
            conn.close()
     
if (__name__ == '__main__'):
    dados = consultar_nome_salario()
    calcular_desconto_inss()
    calcular_desconto_ir()
    calcular_salario_liquido()
    inserir_colunas()
    inserir_valores()
    exibir_relatorio()
