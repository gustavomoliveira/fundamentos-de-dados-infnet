import mysql.connector
import datetime

def conectar_banco():
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='tp5_pb'
    )
    return conn

def criar_tabela(query_sql):
    try:
        conn = conectar_banco()
        cursor = conn.cursor()
        cursor.execute(query_sql)
        conn.commit()
        print('Tabela criada com sucesso!')
    except Exception as erro:
        print(f'Erro ao criar tabela: {erro}')
    finally:
        cursor.close()
        conn.close()

def tabela_esta_vazia(nome_tabela):
    try:
        conn = conectar_banco()
        cursor = conn.cursor()
        cursor.execute(f'SELECT COUNT(*) FROM {nome_tabela}')
        resultado = cursor.fetchone()
        return resultado[0] == 0
    except Exception as erro:
        print(f'Erro ao verificar tabela: {erro}')
        return False
    finally:
        cursor.close()
        conn.close()

def salvar_dados_ibge(dataframe, url):
    try:
        conn = conectar_banco()
        cursor = conn.cursor()
        
        data = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        for linha in dataframe.to_dict('records'):
            query = "INSERT INTO tp5_pb.tabela_ibge (url_acessada, data_acesso, serial, descritivo, ano) VALUES (%s, %s, %s, %s, %s)"
            valores = (url, data, linha['serial'], linha['descritivo'], linha['ano'])
            cursor.execute(query, valores)
            
        conn.commit()
        print(f'Dados IBGE salvos com sucesso! {len(dataframe)} registros inseridos.')
    except Exception as erro:
        print(f'Erro ao salvar dados do IBGE: {erro}')
    finally:
        cursor.close()
        conn.close()

def salvar_metadados_ibge(metadados):
    try:
        conn = conectar_banco()
        cursor = conn.cursor()
        
        query = 'INSERT INTO tp5_pb.metadados_ibge (url_acessada, status_code, data_acesso, content_type, content_length) VALUES (%s, %s, %s, %s, %s)'
        valores = (
            metadados['url'],
            metadados['status_code'],
            metadados['data_acesso'],
            metadados['content_type'],
            metadados['content_length']
        )
        cursor.execute(query, valores)
        conn.commit()
        print('Metadados do IBGE salvos com sucesso!')
    except Exception as erro:
        print(f'Erro ao salvar metadados do IBGE: {erro}')
    finally:
        cursor.close()
        conn.close()

def registrar_erro_ibge(mensagem, url=None):
    try:
        conn = conectar_banco()
        cursor = conn.cursor()
        
        data = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query = 'INSERT INTO tp5_pb.erros_ibge (url_acessada, erro, data_erro) VALUES (%s, %s, %s)'
        valores = (url, mensagem, data)
        
        cursor.execute(query, valores)
        conn.commit()
        print('Erro do IBGE registrado com sucesso!')
    except Exception as erro:
        print(f'Falha ao registrar erro do IBGE: {erro}')
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'conn' in locals() and conn:
            conn.close()

def salvar_noticias_bbc(dataframe, url):
    try:
        conn = conectar_banco()
        cursor = conn.cursor()
        
        data = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        for linha in dataframe.to_dict('records'):
            query = "INSERT INTO tp5_pb.noticias_bbc (url_acessada, data_acesso, titulo, link) VALUES (%s, %s, %s, %s)"
            valores = (url, data, linha['titulo'], linha['link'])
            cursor.execute(query, valores)
            
        conn.commit()
        print(f'Notícias da BBC salvas com sucesso! {len(dataframe)} notícias inseridas.')
    except Exception as erro:
        print(f'Erro ao salvar notícias da BBC: {erro}')
    finally:
        cursor.close()
        conn.close()

def salvar_metadados_bbc(metadados):
    try:
        conn = conectar_banco()
        cursor = conn.cursor()
        
        query = 'INSERT INTO tp5_pb.metadados_bbc (url_acessada, status_code, data_acesso, content_type, content_length) VALUES (%s, %s, %s, %s, %s)'
        valores = (
            metadados['url'],
            metadados['status_code'],
            metadados['data_acesso'],
            metadados['content_type'],
            metadados['content_length']
        )
        cursor.execute(query, valores)
        conn.commit()
        print('Metadados da BBC salvos com sucesso!')
    except Exception as erro:
        print(f'Erro ao salvar metadados da BBC: {erro}')
    finally:
        cursor.close()
        conn.close()

def registrar_erro_bbc(mensagem, url=None):
    try:
        conn = conectar_banco()
        cursor = conn.cursor()
        
        data = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query = 'INSERT INTO tp5_pb.erros_bbc (url_acessada, erro, data_erro) VALUES (%s, %s, %s)'
        valores = (url, mensagem, data)
        
        cursor.execute(query, valores)
        conn.commit()
        print('Erro da BBC registrado com sucesso!')
    except Exception as erro:
        print(f'Falha ao registrar erro da BBC: {erro}')
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'conn' in locals() and conn:
            conn.close()