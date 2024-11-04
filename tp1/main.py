"""
Você irá desenvolver um sistema de gestão de tarefas que permita ao usuário adicionar,
listar, marcar como concluída e remover tarefas.
O programa utilizará loops, manipulação de listas e funções para realizar essas operações.

As tarefas a serem utilizadas poderão ter diferentes metadados: ID da tarefa,
descrição, data de criação, status, prazo final, urgência, entre outros atributos... 

Funcionalidades do Programa:

Adicionar Tarefa: Permitir ao usuário adicionar uma nova tarefa à lista de tarefas pendentes.
Listar Tarefas: Mostrar todas as tarefas pendentes na lista, enumerando-as.
Marcar Tarefa como Concluída: Permitir ao usuário marcar uma tarefa específica como concluída.
Remover Tarefa: Dar ao usuário a opção de remover uma tarefa da lista.

Detalhes da Implementação:

Utilize loops (for e/ou while) para apresentar um menu de opções ao usuário e realizar operações repetidas.
Manipule uma lista para armazenar e gerenciar as tarefas, incluindo adicionar,
listar, marcar como concluída e remover tarefas.
Crie funções para cada funcionalidade do sistema (adicionar, listar, marcar como concluída,
remover), utilizando argumentos, parâmetros por palavra-chave, parâmetros padrão e retorno de valores.
Documente cada função utilizando DocStrings para descrever seu propósito, uso e parâmetros.
"""

from datetime import date
import re

def validar_descricao(txt):
    while True:
        entrada = input(txt)
        if entrada == '0':
            return entrada
        elif all(letra.isalpha() or letra.isspace() for letra in entrada):
            return entrada
        else:
            print('Digite apenas letras/caracteres para a palavra ou frase.')

def validar_urgencia(num):
    while True:
        try:
            urgencia = int(input(num))
            if urgencia == 1:
                return 'Urgente'
            elif urgencia == 2:
                return 'Mediana'
            elif urgencia == 3:
                return 'Sem Urgência'
            else:
                print('ERRO: Digite uma opção entre 1 e 3.')
        except ValueError:
            print('ERRO: Digite apenas números válidos entre as opções apresentadas.')

def validar_opcao_numero(txt):
    while True:
        try:
            numero = int(input(txt))
            return numero
        except ValueError:
            print('ERRO: Digite um número de Id.')

def validar_prazo_final(txt):
    data_atual = gerar_data()
    while True:
        prazo_final = input(txt)
        if not re.fullmatch(r"\d{2}/\d{2}", prazo_final):
            print("ERRO: Formato inválido. Use dd/mm.")
            continue

        dia = int(prazo_final[:2])
        mes = int(prazo_final[3:])

        if not (1 <= dia <= 31 and 1 <= mes <= 12):
            print("ERRO: Dia ou mês inválidos.")
            continue

        if prazo_final < data_atual:
            print('ERRO: A data do prazo final não pode ser anterior à data atual.')
            continue

        return prazo_final

def gerar_id(tarefas):
    id = len(tarefas) + 1
    for index in tarefas:
        if id == index[0]:
            id += 1
    return id

def gerar_data():
    hoje = date.today()
    dia = hoje.day
    mes = hoje.month
    return f'{dia:02d}/{mes:02d}'

def menu(tarefas):
    while True:
        opcao_menu = validar_opcao_numero(
            '====== Gerenciador de Tarefas ======\n'
            '[1] - Adicionar Tarefa\n'
            '[2] - Listar Tarefas Pendentes\n'
            '[3] - Listar Todas as Tarefas (Pendentes e Concluídas)\n'
            '[4] - Marcar Tarefas como Concluídas\n'
            '[5] - Remover Tarefas\n'
            '[0] - Sair\n'
            '====================================\n\n'
            'Digite a opção desejada abaixo:\n'
        )
        match opcao_menu:
            case 1:
                adicionar_tarefa(tarefas)
            case 2:
                listar_tarefas_pendentes(tarefas)
            case 3:
                listar_todas_tarefas(tarefas)
            case 4:
                marcar_conclusao(tarefas)
            case 5:
                remover_tarefa(tarefas)
            case 0:
                print('\nGerenciador de Tarefas encerrado. Até a próxima!\n')
                break
            case _:
                print('Opção inválida.')

def adicionar_tarefa(tarefas):
    while True:
        id = gerar_id(tarefas)
        
        print('\n====== Adicionar Tarefa ======')
        descricao = validar_descricao('\nQual terefa deseja adicionar?(Digite "0" para cancelar.): ').lower()
        if descricao == '0':
            print('\nAdição de tarefas encerrada.\n')
            break
        
        status = 'Pendente'
        
        urgencia = validar_urgencia(
            '\nEssa tarefa é urgente?\n\n'
            '====== Opções de Urgência ======\n'
            '[1] - Urgente\n'
            '[2] - Mediana\n'
            '[3] - Sem Urgência\n\n'
            'Digite a opção desejada abaixo:\n'
        )
        
        criacao = gerar_data()
        
        prazo_final = validar_prazo_final('\nQual o prazo final para essa tarefa ser concluída?(Formato dd/mm): \n')
        
        nova_tarefa = [id, descricao.title(), status, urgencia, criacao, prazo_final]
        tarefas.append(nova_tarefa)
        print('Tarefa adicionada com sucesso!\n')
        listar_todas_tarefas(tarefas)

def listar_tarefas_pendentes(tarefas):
    print('\n====== Tarefas Pendentes ======')
    posicao = 0
    encontrou_pendente = False

    for tarefa in tarefas:
        if tarefa[2] == 'Pendente':
            encontrou_pendente = True
            posicao += 1
            print(f'Tarefa n˚{posicao}')                 
            print(f'Id: {tarefa[0]}')
            print(f'Descrição: {tarefa[1]}')
            print(f'Urgência: {tarefa[3]}')
            print(f'Data da Criação: {tarefa[4]}')
            print(f'Prazo Final: {tarefa[5]}')
            print()
    
    if not encontrou_pendente:
        print('\nNão existem tarefas pendentes!\n')

def listar_todas_tarefas(tarefas):
    print('\nEssas são todas as suas tarefas, ordenadas por status: ')

    print('\n====== Pendentes ======')
    for tarefa in tarefas:
        if tarefa[2] == 'Pendente':
            print(f'Id: {tarefa[0]}')
            print(f'Descrição: {tarefa[1]}')
            print(f'Urgência: {tarefa[3]}')
            print(f'Data da Criação: {tarefa[4]}')
            print(f'Prazo Final: {tarefa[5]}')
            print()
    print('\n====== Concluídas ======')
    for tarefa in tarefas:
        if tarefa[2] == 'Concluída':
            print(f'Id: {tarefa[0]}')
            print(f'Descrição: {tarefa[1]}')
            print(f'Urgência: {tarefa[3]}')
            print(f'Data da Criação: {tarefa[4]}')
            print(f'Prazo Final: {tarefa[5]}')
            print()

def marcar_conclusao(tarefas):
    while True:
        listar_tarefas_pendentes(tarefas)
        concluir = validar_opcao_numero('\nQual tarefa deseja marcar como concluída? Escolha pelo número do Id ou digite "0" para sair: ')
        
        if concluir == 0:
            print('\nMarcação encerrada.\n')
            break
        
        for tarefa in tarefas:
            if tarefa[0] == concluir:
                tarefa[2] = 'Concluída'
                print(f'\nTarefa "{tarefa[1]}" marcada como concluída.\n')
                break
        else:
            print('\nERRO: Id inválido.\n')

def remover_tarefa(tarefas):
    while True:
        listar_tarefas_pendentes(tarefas)
        remover = validar_opcao_numero('\nQual tarefa deseja remover da lista? Escolha pelo número do Id ou digite "0" para sair: ')
        
        if remover == 0:
            print('\nRemoção encerrada.\n')
            break
        
        for tarefa in tarefas:
            if tarefa[0] == remover:
                tarefas.remove(tarefa)
                print('\nRemoção concluída.\n')
                break
        else:
            print('ERRO: Id inválido.')

# id, descrição, status, urgência, data da criação, prazo final
tarefas = [[1, 'Lavar Louça', 'Concluída', 'Urgente', '03/11', '05/11']]
id = gerar_id(tarefas)
data = gerar_data()
print('\nBem vindo ao Gerenciador de Tarefas! Escolha uma opção do Menu para iniciar.\n')
menu(tarefas)


