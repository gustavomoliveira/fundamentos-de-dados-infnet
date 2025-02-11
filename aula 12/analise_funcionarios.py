# lib matplotlib para gráficos. trabalha junto de pandas

import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns

# conectar a base de dados
conn = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='empresa'
)

# consulta SQL para obter todos os funcionários da base
query = 'SELECT id, nome, salario_base, departamento FROM empresa.funcionarios'

# criando um dataframe para consulta
df = pd.read_sql(query, conn)

# fechar conexão
conn.close()

# head exibe as primeiras linhas (20, no caso)
print(df.head(20))

""" # gráfico 1: quantidade de funcionários alocados por departamentos
plt.subplot(1, 2, 1) # param: a partir da linha 1, coluna 2, e index 1
sns.countplot(x='departamento', data = df, palette='viridis') # agrupamento e contagem

plt.title('Quantidade de Funcionaários por Departamento')
plt.xlabel('Departamento')
plt.ylabel('Número de Funcionários')
plt.show() """

""" # gráfico 2: média salarial por departamento
plt.subplot(1, 2, 1)
salario_medio = df.groupby('departamento')['salario_base'].mean().sort_values()
sns.barplot(x=salario_medio.values, y=salario_medio.index)
plt.title('Média Salarial por Departamento')
plt.xlabel('Salário Médio')
plt.ylabel('Departamento')
plt.show() """

""" # gráfico 3: histograma
plt.figure(figsize=(10,5))
sns.histplot(x=df['salario_base'], bins=10, kde=True, color='blue')
plt.title('Distribuição de Salários')
plt.xlabel('Salário')
plt.ylabel('Frequência')
plt.show() """

# gráfico 4: dispersão
plt.figure(figsize=(10,5))
sns.scatterplot(x=df['departamento'], y=df['salario_base'], hue=df['nome'], palette='Set1', s=100)
plt.title('Departamento x Salário Base por Nome')
plt.xlabel('Departamento')
plt.ylabel('Salário Base')
plt.legend(title='Nome')
plt.show()