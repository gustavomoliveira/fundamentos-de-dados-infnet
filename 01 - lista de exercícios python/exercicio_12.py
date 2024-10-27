"""
12 - Escreva um programa que solicite ao usuário a quantidade de notas que deseja informar,
em seguida, use um loop para solicitar essas notas.
O programa deve calcular e exibir a média das notas.
"""

def validar_input(texto):
    while True:
        try:
            qtde_notas = int(input(texto))
            if qtde_notas > 0:
                return qtde_notas
            else:
                print('Digite um número maior do que 0.')
        except ValueError:
            print('ERRO: Digite um número inteiro.')

def solitar_notas(qtde):
    total_notas = []
    for nota in range(qtde):
        nota = validar_input(f'Digite a nota {nota + 1}: ')
        total_notas.append(nota)
    return total_notas

def media_de_notas(total):
    media = (sum(total)) / len(total)
    return media

qtde_notas = validar_input('Quantas notas você deseja informar? ')
total_notas = solitar_notas(qtde_notas)
media = media_de_notas(total_notas)
print(f'A media total de {qtde_notas} notas é {media}.')