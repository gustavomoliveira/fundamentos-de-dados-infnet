import mysql.connector

def conectar_mysql():
    return mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='tp5_pb'
    )