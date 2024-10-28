"""
Exercício 2: Verificador de Par ou Ímpar
Escreva um programa que solicite um número ao usuário e verifique
se o número é par ou ímpar. Exiba a mensagem correspondente.
"""

def verifica_numero(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            return numero
        except ValueError:
            print('Erro: Digite um número válido.')

def par_ou_impar(numero):
    if numero % 2 == 0:
        print(f'O número {numero} é par.')
    else:
        print(f'O número {numero} é ímpar.')

numero = verifica_numero('Digite um número: ')
par_ou_impar(numero)
