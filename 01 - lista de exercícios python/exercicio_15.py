"""
15 - Escreva um programa que solicite ao usuário um número inteiro positivo e,
em seguida, aplique a sequência de Collatz (ou conjectura de Collatz)
até o número se tornar 1. Exiba cada valor da sequência e o número total de passos necessários para alcançar 1.
"""

def validar_numero(texto):
    while True:
        try:
            numero = int(input(texto))
            if numero > 0:
                return numero
            else:
                print('Digite um número inteiro positivo.')
        except ValueError:
            print('ERRO: Digite um número.')

def sequencia_collatz(numero):
    sequencia = []
    passos = 0
    while numero != 1:
        if numero % 2 == 0:
            numero = numero // 2
            sequencia.append(numero)
            passos += 1
        else:
            numero = (3 * numero) + 1
            sequencia.append(numero)
            passos += 1
    return sequencia, passos

numero = validar_numero('Digite um número: ')
sequencia, passos = sequencia_collatz(numero)
print(f"""
A sequência de Collatz com o número {numero} é:

{sequencia}.

Ela possui {passos} passos até chegar em 1.
""")

