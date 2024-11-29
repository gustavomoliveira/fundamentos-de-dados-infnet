""" Estrutura de Dados """

# Dicionário

task = {
    'id': 0,
    'nome': 'Gustavo Mendes',
    'descricao': 'Lavar Louça',
    'status': 'Pendente'
}

# acesso através da chave
for key in task:
    print(f'Chave: {key}, Valor: {task[key]}')
print()

# acesso através do method items()
for key, value in task.items():
    print(f'Chave: {key}, Valor: {value}')

lista_tarefas = []

# Inicia o programa
lista_tarefas.append(task)
print(lista_tarefas)