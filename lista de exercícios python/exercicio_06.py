"""
Exercício 6: Verificador de Ano Bissexto
Escreva um programa que peça ao usuário um ano e verifique se é um ano bissexto.
Um ano é bissexto se for divisível por 4, exceto se for divisível por 100, a menos que seja divisível por 400.
"""

def valida_ano(texto):
    while True:
        try:
            ano = int(input(texto))
            return ano
        except ValueError:
            print('ERRO: Valor incorreto.')

def ano_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f'O ano {ano} é bissexto.')
    else:
        print(f'O ano {ano} NÃO é bissexto.')

ano = valida_ano('Digite um ano qualquer: ')
ano_bissexto(ano)