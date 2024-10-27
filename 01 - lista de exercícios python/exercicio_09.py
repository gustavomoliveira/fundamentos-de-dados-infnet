"""
Exercício 9: Jogo de Adivinhação
Escreva um programa que escolha aleatoriamente um número entre 1 e 10.
O usuário deve tentar adivinhar o número, e o programa deve fornecer dicas
se o palpite for maior ou menor que o número.
Quando o usuário acertar, exiba uma mensagem de parabéns.
"""
import random

def validar_input(texto):
    while True:
        try:
            palpite = int(input(texto))
            if 1 <= palpite <= 10:
                return palpite
            else:
                print('Digite um número entre 1 e 10.')
        except ValueError:
            print('ERRO: Digite um número válido.')
        

def verificar_chute(numero):
    while True:
        palpite = validar_input('Digite um número entre 1 e 10 para iniciar: ')
        
        if palpite == numero:
            print(f'Você acertou! O número aleatório é {numero}.')
            break
        elif palpite < numero:
            print(f'O número é MAIOR que {palpite}.')
        else:
            print(f'O número é MENOR que {palpite}.')

numero_aleatorio = random.randint(1, 10)
verificar_chute(numero_aleatorio)