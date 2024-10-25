"""
Exercício 5: Calculadora Simples
Escreva um programa que solicite ao usuário dois números e uma operação (adição, subtração, multiplicação ou divisão).
O programa deve executar a operação correspondente e exibir o resultado.
Se o usuário escolher uma operação inválida, exiba uma mensagem de erro.
"""

def valida_inputs(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
            return numero
        except ValueError:
            print('ERRO: Digite um número válido.')

def valida_operacao(mensagem):
    while True:
        try:
            operacao = int(input(mensagem))
            if 0 <= operacao <= 4:
                return operacao
            else:
                print('Operação inválida. Escolha uma operação no Menu.')
        except ValueError:
            print('ERRO: Digite um número válido.')

def adicao(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        print('ERRO: Divisão por 0.')

def executa_operacao(num1, num2, operacao):
        match operacao:
            case 1:
                print(f'O resultado da soma é {adicao(num1, num2)}')
            case 2:
                print(f'O resultado da subtração é {subtracao(num1, num2)}')
            case 3:
                print(f'O resultado da multiplicação é {multiplicacao(num1, num2)}')
            case 4:
                result = divisao(num1, num2)
                if result is not None:
                    print(f'O resultado da divisão é {result}')
            case _:
                print('Operação inválida.')

def menu():
    while True:
        menu = """
    ------- MENU -------
    [1] - Adição
    [2] - Subtração
    [3] - Miltiplicação
    [4] - Divisão
    [0] - Sair
    --------------------
    """
        print(menu)
        operacao = valida_operacao('Escolha qual operação realizar:')

        if operacao == 0:
            print('Menu encerrado. Obrigado!')
            break

        num_1 = valida_inputs('Digite o primeiro número: ')
        num_2 = valida_inputs('Digite o segundo número: ')
        executa_operacao(num_1, num_2, operacao)

menu()


