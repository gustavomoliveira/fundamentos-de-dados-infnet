""" 
Exercício 1: Verificação de Idade
Escreva um programa que solicite ao usuário sua idade e verifique:
	
Se ele tem menos de 18 anos, exiba "Você é menor de idade."
Se ele tem entre 18 e 65 anos, exiba "Você é adulto."
Se ele tem mais de 65 anos, exiba "Você é idoso."
"""
def valida_idade(mensagem):
    while True:
        try:
            idade_usuario = int(input(mensagem))
            if idade_usuario <= 0:
                print('Idade inválida.')
            else:
                return idade_usuario
        except ValueError:
            print('Erro: Digite um número válido')

def verifica_idade(idade):
    if idade < 18:
        print('Você é menor de idade.')
    elif 18 <= idade <= 65:
        print('Você é adulto.')
    else:
        print('Você é idoso.')

idade_usuario = valida_idade('Digite sua idade: ')
verifica_idade(idade_usuario)


