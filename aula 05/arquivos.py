""" Manipulação de Arquivos """

# dicas:
# \\ uso de duas contra-barras, no windows, para dizer ao python que não queremos executar um comando(\), apenas imprimir

# ler todo o arquivo
with open('./arquivos csv/actions_under_antiquities_act - actions_under_antiquities_act (1).csv', 'r') as file:
    arquivo = file.read()
    print(arquivo)

# ler linha a linha
with open('./arquivos csv/actions_under_antiquities_act - actions_under_antiquities_act (1).csv', 'r') as file:
    for linha in file:
        print(linha)

# criar e escrever em novo arquivo
with open('novo_arquivo.csv', 'w') as file:
    for i in range(1, 20):
        file.write(f'Testando novas linhas {i}\n')

# adicionando mais linhas ao arquivo criado
with open('novo_arquivo.csv', 'a') as file:
    for i in range(20, 31):
        file.write(f'Testando novas linhas {i}\n')

# caso seja utilizado o comando 'w' em um arquivo já existente, ele irá apagar todo o conteúdo e sobrescrever com o novo conteúdo passado
with open('novo_arquivo.csv', 'w') as file:
    for i in range(1, 11):
        file.write(f'Sobrescrevendo novas linhas {i}\n')

# criando uma cópia da base desejada
with open('./arquivos csv/actions_under_antiquities_act - actions_under_antiquities_act (1).csv', 'r') as origem:
    texto = origem.read()
    with open('copia_base.csv', 'w') as alvo:
        alvo.write(texto)

# todas as vezes que utilizamos um arquivo, é necessário fecha-lo. reseta a memória.
# seria o .close()
# com o uso do with garante o fechamento do arquivo automaticamente

# lendo arquivos grandes, acima de 1GB, por exemplo. boa prática.
with open('./arquivos csv/actions_under_antiquities_act - actions_under_antiquities_act (1).csv', 'r') as file:
    while(linha := file.readline()): # comando := enquanto existir linha a ser lida, o while continua. joga cada linha lida para a variável 'linha'.
        print(linha)