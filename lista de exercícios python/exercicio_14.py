"""
15 - Escreva um programa que solicite ao usuário um número inteiro positivo
e exiba o número na ordem inversa (exemplo: entrada 1234, saída 4321).
"""

def validar_numero(texto):
    while True:
        try:
            numero = int(input(texto))
            if numero > 0:
                return numero
            else:
                print('Digite um número maior do que 0.')
        except ValueError:
            print('Digite um número válido.')

def reverter_numero(numero):
    numero_reverso = str(numero)[::-1]
    return numero_reverso

numero = validar_numero('Digite um número: ')
numero_reverso = reverter_numero(numero)
print(f'A ordem inversa de {numero} é {numero_reverso}.')

