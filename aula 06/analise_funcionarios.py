import pandas as pd

# carregar os arquivos
df = pd.read_csv('copia_base.csv')

# print das primiras 20 linhas
#print(df.head(20))

# analisando a coluna 'states' do csv
states = df['states'].value_counts()
print(states)
