"""
Exercício 8: Verificação de Triângulo
Escreva um programa que peça ao usuário três comprimentos de lados e verifique
se eles podem formar um triângulo.
Se puderem, determine se o triângulo é equilátero, isósceles ou escaleno.
"""

def validar_numero(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            return numero
        except ValueError:
            print('ERRO: Digite um número válido.')

def verificar_se_triangulo(num1, num2, num3):
    if num1 < (num2 + num3) and num2 < (num1 + num3) and num3 < (num1 + num2):
        return True
    else:
        print('Não é possível formar um triângulo com os números fornecidos.')
        return False


def tipo_de_triangulo(num1, num2, num3):
    if num1 == num2 == num3:
        print('Triângulo Equilátero.')
    elif num1 == num2 or num1 == num3 or num2 == num3:
        print('Triângulo Isósceles.')
    else:
        print('Triângulo Escaleno.')

num1 = validar_numero('Digite o primeiro número: ')
num2 = validar_numero('Digite o segundo número: ')
num3 = validar_numero('Digite o terceiro número: ')

if verificar_se_triangulo(num1, num2, num3):
    tipo_de_triangulo(num1, num2, num3)