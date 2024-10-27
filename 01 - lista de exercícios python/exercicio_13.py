"""
13 - Escreva um programa que solicite ao usuário uma palavra
e conte quantas vogais (a, e, i, o, u) existem na palavra.
"""

def validar_palavra(texto):
    while True:
        try:
            palavra = input(texto)
            if all(letra.isalpha() or letra.isspace() for letra in palavra):
                return palavra
            else:
                print('Todos os caracteres devem ser letras.')
        except ValueError:
            print('ERRO: Digite uma palavra válida.')

def contar_vogais(palavra):
    vogais = ('a', 'e', 'i', 'o', 'u')
    return sum(1 for letra in palavra.lower() if letra in vogais)

palavra = validar_palavra('Digite uma palavra: ')
contador = contar_vogais(palavra)
print(f'A palavra {palavra.title()} possui {contador} vogais.')
