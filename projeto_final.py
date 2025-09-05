# Adiciona as tarefas na lista de tarefas
def adicionar_tarefa(lista_de_tarefas, tarefa):
    lista_de_tarefas.append(tarefa)
    print('--> Tarefa adicionada com sucesso!')
    return lista_de_tarefas

# Exibe as tarefas que estão na lista de tarefas
def listar_tarefas(lista_de_tarefas):
    print('-' * 50)
    print(f"{' ' * 15}Lista de Tarefas")
    print('-' * 50)
    n = 1
    for tarefa in lista_de_tarefas:
        print(f'{n} - {tarefa}')
        n += 1
    print('-' * 50)

# Deleta uma tarefa
def deletar_tarefa(lista_de_tarefas, tarefa):
    lista_de_tarefas.pop((tarefa - 1))
    return lista_de_tarefas
 
# Exibe o menu com as opções
def exibir_menu():
    print('-' * 50)
    print('Escolha uma opção:\n' \
    '1 - Inserir nova tarefa\n' \
    '2 - Listar tarefas\n' \
    '3 - Deletar tarefa\n' \
    '4 - Sair')
    print('-' * 50)
    
lista_de_tarefas = []
continuar = True

while continuar == True:
    # Exibe o menu
    print('Bem-vinde à sua lista de tarefas!')
    exibir_menu()
    opcao = input('Insira o que deseja fazer: ')
    
    
    if opcao == "1":
        tarefa = input('Insira uma nova tarefa: ')
        lista_de_tarefas = adicionar_tarefa(lista_de_tarefas, tarefa)
    elif opcao == "2":
        listar_tarefas(lista_de_tarefas)
    elif opcao == "3":
        tarefa = input('Insira o número da tarefa que deseja deletar: ')
        if not tarefa.isnumeric():
            print('-' * 50)
            print('Número inválido! Tente novamente.')
        elif int(tarefa) > len(lista_de_tarefas):
            print('-' * 50)
            print('Número inválido! Tente novamente.')
        elif int(tarefa) <= 0:
            print('-' * 50)
            print('Número inválido! Tente novamente.')
        else:
            deletar_tarefa(lista_de_tarefas, int(tarefa))
    elif opcao == "4":
        continuar = False
    else:
        print('Opção inválida! Por favor, tente novamente.')
        print('\n')
