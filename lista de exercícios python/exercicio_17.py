"""
17 - Escreva um programa que solicite ao usuário um número N de notas e seus respectivos pesos.
O programa deve calcular e exibir a média ponderada das notas.
Utilize loops para processar as entradas e realizar o cálculo.
"""

def validar_entradas(texto):
    while True:
        try:
            entrada = int(input(texto))
            if entrada >= 0 or entrada == -1:
                return entrada
            else:
                print('Não existe nota negativa.')
        except ValueError:
            print('ERRO: Digite um número válido.')

def entradas():
    notas = []
    peso_notas = []
    while True:
        entrada_notas = validar_entradas('Digite uma nota (ou -1 para encerrar): ')
        if entrada_notas == -1:
            print('Entradas finalizadas.')
            break
        entrada_pesos = validar_entradas('Digite o peso da nota: ')
        notas.append(entrada_notas)
        peso_notas.append(entrada_pesos)
    return notas, peso_notas


def calcular_media_ponderada(notas, peso):
    numerador = sum(nota * p for nota, p in zip(notas, peso)) 
    denominador = sum(peso)
    media_ponderada = numerador / denominador
    return media_ponderada

notas, peso_notas = entradas()
media_ponderada = calcular_media_ponderada(notas, peso_notas)
print(f'A média ponderada é: {media_ponderada:.2f}')