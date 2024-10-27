"""
Exercício 10: Conversor de Notas para Letras
Escreva um programa que solicite ao usuário uma nota numérica (de 0 a 100)
e converta essa nota em uma letra conforme a seguinte tabela:
90 a 100: "A"
80 a 89: "B"
70 a 79: "C"
60 a 69: "D"
Abaixo de 60: "F"
"""

def validar_nota(texto):
    while True:
        try:
            nota = int(input(texto))
            if nota == -1:
                return -1
            elif 0 <= nota <= 100:
                return nota
            else:
                print('Digite um número entre 0 e 100')
        except ValueError:
            print('ERRO: Digite um número inteiro.')

def converter_nota():
    while True:
        nota = validar_nota('Digite um número entre 0 e 100: ')
        if nota == -1:
            print("Programa encerrado.")
            break
        elif 90 <= nota <= 100:
            print(f'{nota} --> A')
        elif 80 <= nota <= 89:
            print(f'{nota} --> B')
        elif 70 <= nota <= 79:
            print(f'{nota} --> C')
        elif 60 <= nota <= 69:
            print(f'{nota} --> D')
        else:
            print(f'{nota} --> F')

converter_nota()