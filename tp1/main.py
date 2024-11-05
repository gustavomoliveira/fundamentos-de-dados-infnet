
from datetime import date
import re

def validar_descricao(txt):
    """
    Valida que 'entrada' receba apenas caracteres alfabéticos,
    aceite espaços para o caso de strings compostas e o numeral 0.

    Parâmetro:
    - txt (str): A inserção por input() do usuário.

    Retorno:
    - str: Resultado validado da inserção do usuário.
    """
    while True:
        entrada = input(txt)
        if entrada == '0':
            return entrada
        elif all(letra.isalpha() or letra.isspace() for letra in entrada):
            return entrada
        else:
            print('Digite apenas letras/caracteres para a palavra ou frase.')

def validar_urgencia(opcao):
    """
    Valida que 'urgencia' receba apenas um número int() entre 1 e 3.

    Parâmetros:
    - opcao (str): A inserção por input() do usuário.

    Retorno:
    - str: Resultado validado da inserção do usuário.
    """
    while True:
        try:
            urgencia = int(input(opcao))
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

def validar_menu(num):
    """
    Valida que 'numero' receba apenas um número int() entre 0 e 5.

    Parâmetros:
    - num (str): A inserção por input() do usuário.

    Retorno:
    - str: Resultado validado da inserção do usuário.
    """
    while True:
        try:
            numero = int(input(num))
            if 0 <= numero <= 5:
                return numero
            else:
                print('Digite uma das opções do Menu.')
        except ValueError:
            print('ERRO: Digite um número válido.')

def validar_opcao_numero(num):
    """
    Valida que 'numero' receba apenas um número int().

    Parâmetros:
    - num (str): A inserção por input() do usuário.

    Retorno:
    - str: Resultado validado da inserção do usuário.
    """
    while True:
        try:
            numero = int(input(num))
            return numero
        except ValueError:
            print('ERRO: Digite um número de Id.')

def validar_prazo_final(prazo):
    """
    Valida que 'prazo_final' possua o formato exato de dd/mm, seguindo, também, as
    regras de intervalo de números e comparação com 'data_atual'.

    Parâmetros:
    - prazo(str): A inserção por input() do usuário.

    Retorno:
    - str: Resultado validado da inserção do usuário.

    """
    data_atual = gerar_data()
    while True:
        prazo_final = input(prazo)
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
    """
    Gera um número int() maior que o comprimento da lista passada como parâmetro.

    Caso o número já exista nessa lista, o mesmo é acrescido de 1.

    Parâmetros:
    - tarefas([]): Uma lista.

    Retorno:
    - []: Uma lista aninha de mais listas.
    """
    id = len(tarefas) + 1
    for index in tarefas:
        if id == index[0]:
            id += 1
    return id

def gerar_data():
    """
    Gera a data atual no formato dd/mm.

    Retorno:
    - str: Data dd/mm formatada.
    """
    hoje = date.today()
    dia = hoje.day
    mes = hoje.month
    return f'{dia:02d}/{mes:02d}'

def menu(tarefas):
    """ 
    Exibe um menu interativo com opções de seleção numérica de 0 a 5.

    Parâmetros:
    - tarefas([]): Uma lista.
    """
    while True:
        opcao_menu = validar_menu(
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
    """
    Aninha uma lista 'nova_tarefa' composta por 'id', 'descricao', 'status', 'urgencia', 'criacao' e 'prazo_final'
    a lista recebida por parâmetro como referência.

    Parâmetros:
    - tarefas([]): Uma lista.
    """
    while True:
        id = gerar_id(tarefas)
        
        print('\n====== Adicionar Tarefa ======')
        descricao = validar_descricao('\nQual terefa deseja adicionar?(Digite "0" para cancelar.): ')
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
        print('\nTarefa adicionada com sucesso!')
        listar_todas_tarefas(tarefas)

def listar_tarefas_pendentes(tarefas):
    """
    Exibe todas as tarefas com status 'pendente' na lista passada por parâmetro.

    Se não houver tarefas pendentes, exibe mensagem informando.

    Parâmetros:
    - tarefas([]): Uma lista.
    """
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
    """
    Exibe todas as tarefas na lista passada por parâmetro, independente de seus status.

    Parâmetros:
    - tarefas([]): Uma lista.
    """
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
    """
    Altera o status de 'Pendente' para 'Concluída' de tarefas selecionadas via id pelo usuário
    contidas em uma lista passada como parâmetro por referência.

    Parâmetro:
    - tarefas([]): Uma lista.
    """
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
    """
    Remove tarefas selecionadas via id pelo usuário
    contidas em uma lista passada como parâmetro por referência.

    Parâmetro:
    - tarefas([]): Uma lista.
    """
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

tarefas = []
print('\nBem vindo ao Gerenciador de Tarefas! Escolha uma opção do Menu para iniciar.\n')
menu(tarefas)


