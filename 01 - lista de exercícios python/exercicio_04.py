"""
Exercício 4: Classificação de Temperatura
Escreva um programa que peça ao usuário a temperatura atual em graus Celsius e exiba uma mensagem:
Abaixo de 0 graus: "Muito frio."
Entre 0 e 20 graus: "Frio."
Entre 21 e 30 graus: "Agradável."
Acima de 30 graus: "Quente."
"""

def valida_temperatura(mensagem):
    while True:
        try:
            temperatura = int(input(mensagem))
            return temperatura
        except ValueError:
            print('ERRO: Digite um número válido.')

def termometro(temperatura):
    if temperatura < 0:
        print('Muito frio!')
    elif 0 <= temperatura <= 20:
        print('Frio.')
    elif 21 <= temperatura <= 30:
        print('Agradável.')
    else: 
        print('Quente.')

temperatura = valida_temperatura('Digite o valor da temperatura atual(graus Celsius): ')
termometro(temperatura)