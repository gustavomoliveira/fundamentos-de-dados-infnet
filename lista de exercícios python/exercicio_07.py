"""
Exercício 7: Classificação de Peso
Escreva um programa que solicite o peso e a altura do usuário e calcule o índice de massa corporal (IMC).
Com base no IMC, classifique o usuário em:
Abaixo de 18.5: "Abaixo do peso."
Entre 18.5 e 24.9: "Peso normal."
Entre 25 e 29.9: "Sobrepeso."
30 ou acima: "Obesidade."
"""

def valida_input(texto):
    while True:
        try:
            valor = float(input(texto))
            return valor
        except ValueError:
            print('ERRO: Digite um número válido.')

def imc(peso, altura):      
    imc = peso / (altura * altura)

    if imc < 18.5:
        print('Abaixo do peso.')
    elif 18.5 <= imc <= 24.9:
        print('Peso normal.')
    elif 25 <= imc <= 29.9:
        print('Sobrepeso.')
    else:
        print('Obesidade.')

peso = valida_input('Digite o seu peso: ')
altura = valida_input('Digite a sua altura: ')
imc(peso, altura)