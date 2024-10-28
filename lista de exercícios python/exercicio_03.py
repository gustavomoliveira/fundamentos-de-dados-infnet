"""
Exercício 3: Calculadora de Notas
Escreva um programa que peça ao usuário para digitar três notas (entre 0 e 10) de um aluno.
O programa deve calcular a média e determinar a situação do aluno:
Média maior ou igual a 7: "Aprovado."
Média entre 5 e 6.9: "Recuperação."
Média abaixo de 5: "Reprovado."
"""

todas_as_notas = []

def valida_nota():
    cont = 1
    while len(todas_as_notas) < 3:
        try:
            nota = int(input(f'Digite a nota n˚{cont}: '))
            if 0 <= nota <= 10:
                todas_as_notas.append(nota)
                cont += 1
            else:
                print('Digite uma nota entre 0 e 10.')
        except ValueError:
            print('ERRO: Digite um número válido.')
    return todas_as_notas

def calcula_media(notas):
    total_notas = sum(todas_as_notas)
    media = total_notas / len(notas)
    print(f'A média do aluno é {media:.2f}.')

    if media >= 7:
        print('Aprovado.')
    elif 5 <= media <= 6.9:
        print('Recuperação.')
    else:
        print('Reprovado.')

todas_as_notas = valida_nota()

if len(todas_as_notas) == 3:
    calcula_media(todas_as_notas)
