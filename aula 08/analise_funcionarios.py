import pandas as pd

df = pd.read_csv('funcionarios.csv')

# exibir as primeiras linhas do dataframe
#print(df.head(3)) # em ti, head sempre se refere ao início do arquivo, normalmente as 5 primeiras linhas
#print(df.tail()) # tail é o inverso, printa o final do arquivo

# filtragem por departamento: filtre os funcionários que trabalham no departamento de TI
print(df)
ti = df[df['Departamento'].str.contains('TI')]
# ou
ti2 = df[df['Departamento'] == 'TI']
#print(ti)
#print(ti2)

# departamento e se trabalha remoto
verificacao = df[(df['Departamento'] == 'TI') & (df['Home_Office'] == 1)]
print(verificacao)

# média salarial por departamento: calcule a média do salário dos funcionários para cada departamento.
media_salarial = df.groupby('Departamento')['Salário'].mean().round(2) # palavra 'por' sempre é para agrupar
#print(media_salarial)

# funcionários com mais de 5 anos na empresa: liste os funcionários com mais de 5 anos de empresa.
funcionarios = df[df['Tempo_Empresa'] > 5]
#print(funcionarios)

# funcionários em home office: filtre apenas os funcionários que trabalham em home office.
home_office = df[df['Home_Office'] == 1]
#print(home_office)

# funcionário mais bem pago: quem é o funcionário com o maior salário?
maior_salario = df[df['Salário'] == df['Salário'].max()]
#print(maior_salario)

# salário total da empresa: qual é a soma total dos salários dos funcionários?
soma_salarios = df['Salário'].sum()
#print(soma_salarios)

""" distribuição por idade: quantos funcionários estão nas faixas etárias de:
Menos de 30 anos
Entre 30 e 40 anos
Mais de 40 anos """
menor_que_30 = df[df['Idade'] < 30].shape[0]
#print(menor_que_30)

entre_30_e_40 = df[(df['Idade'] >= 30) & (df['Idade'] <= 40)].shape[0]
#print(entre_30_e_40)

maior_que_40 = df[df['Idade'] > 40].shape[0]
#print(maior_que_40)

# aumento salarial: adicione uma coluna chamada Novo_Salário, considerando um aumento de 10%.
df['Novo_Salário'] = df['Salário'] * 1.10
#print(df)

# correlação entre tempo de empresa e salário: existe alguma relação entre o tempo de empresa e o salário dos funcionários?
correlacao = df['Tempo_Empresa'].corr(df['Salário'])
print(correlacao)

# ou
correlacao_2 = ['Tempo_Empresa', 'Salário']
print(df[correlacao_2].corr())