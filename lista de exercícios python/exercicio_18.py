"""
19 - Escreva um programa que solicite ao usuário um número inteiro positivo e verifique
se ele é um número perfeito. Um número perfeito é um número que é igual à soma de
seus divisores próprios (excluindo ele mesmo). O programa deve listar todos os divisores e exibir o resultado da verificação.
"""

# Um número se diz perfeito se é igual à soma de seus divisores próprios.
# Divisores próprios de um número positivo N são todos os divisores inteiros positivos de N exceto o próprio N.
# Por exemplo, o número 6, seus divisores próprios são 1, 2 e 3, cuja soma é igual à 6.

def validar_numero(texto):
    while True:
        try:
            numero = int(input(texto))
            if numero > 0:
                return numero
            else:
                print('Digite um número inteiro positivo.')
        except ValueError:
            print('ERRO: Digite um número válido.')

def procurar_divisores(numero):
    lista_divisores = []
    for divisor in range(1, numero): # range percorre de start até stop -1
        if numero % divisor == 0:
            lista_divisores.append(divisor)
    return lista_divisores

def procurar_numero_perfeito(divisores, numero):
    if sum(divisores) == numero:
        return f'O número {numero} é perfeito. A soma de seus divisores {divisores} resulta no próprio número {numero}.'
    else:
        return f'O número {numero} NÃO é perfeito.'


numero = validar_numero('Digite um número inteiro positivo: ')
lista_divisores = procurar_divisores(numero)
resultado = procurar_numero_perfeito(lista_divisores, numero)
print(resultado)

