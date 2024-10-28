"""
16 - Escreva um programa que solicite ao usuário uma palavra ou frase e verifique
se é um palíndromo (ou seja, se lê da mesma forma de trás para frente, ignorando espaços e pontuações).
Use loops e condições para realizar a verificação.
"""

def validar_mensagem(msg):
    while True:
        try:
            msg = input(msg).lower()
            if all(letra.isalpha() or letra.isspace() for letra in msg):
                return msg.replace(' ', '')
            else:
                print('Digite um texto contendo apenas letras.')
        except ValueError:
            print('ERRO: Digite uma palavra ou texto válidos.')

def testar_palindromo(texto):
    if texto == texto[::-1]:
        print(f'{texto} é palíndromo! {texto[::-1]}.')
    else:
        print(f'{texto} não é palíndromo.')

texto = validar_mensagem('Digite uma palavra ou frase: ')
testar_palindromo(texto)