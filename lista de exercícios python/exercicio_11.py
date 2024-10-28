"""
11 - Escreva um programa que solicite ao usuário um número inteiro
positivo e exiba os primeiros N termos da sequência de Fibonacci.
"""

def valida_numero(texto):
    while True:
        try:
            numero = int(input(texto))
            if numero > 0:
                return numero
            else:
                print('Digite um número inteiro positivo.')
        except ValueError:
            print('ERRO: Digite um número.')

def fibonacci(numero, num1, num2):
    for _ in range(numero):
        num3 = num2 + num1
        print(num3, end=' ')
        num1, num2 = num2, num3

num1, num2 = 0, 1
numero = valida_numero('Digite um número inteiro positivo: ')
fibonacci(numero, num1, num2)

