import datetime

tarefas = []
def mostrar_tarefas():
    """
    Exibe todas as tarefas que ainda estão pendentes.
    Se não houver nenhuma tarefa, avisa o usuário.
    """
    if not tarefas:
        print("Nenhuma tarefa pendente.")
    else:
        for tarefa in tarefas:
            print(f"ID: {tarefa['id']}, Descrição: {tarefa['descricao']}, Status: {tarefa['status']}, Prazo: {tarefa['prazo']}, Urgência: {tarefa['urgencia']}")
def adicionar_tarefa(descricao, prazo, urgencia):
    """
    Adiciona uma nova tarefa à lista de tarefas.
    Você precisa fornecer a descrição, o prazo e a urgência da tarefa.
    """
    tarefa = {
        'id': len(tarefas) + 1,
        'descricao': descricao,
        'data_criacao': datetime.datetime.now().strftime('%d-%m-%Y'),
        'status': 'Pendente',
        'prazo': prazo,
        'urgencia': urgencia
    }
    tarefas.append(tarefa)
def concluir_tarefa(id_tarefa):
    """
    Marca uma tarefa como concluída.
    Você deve informar o ID da tarefa que deseja concluir.
    """
    for tarefa in tarefas:
        if tarefa['id'] == id_tarefa:
            tarefa['status'] = 'Concluída'
            print(f"Tarefa {id_tarefa} concluída.")
            return
    print(f"Tarefa {id_tarefa} não encontrada.")
def excluir_tarefa(id_tarefa):
    """
    Remove uma tarefa da lista.
    Diga o ID da tarefa que você quer excluir.
    """
    for i, tarefa in enumerate(tarefas):
        if tarefa['id'] == id_tarefa:
            del tarefas[i]
            print(f"Tarefa {id_tarefa} excluída.")
            return
    print(f"Tarefa {id_tarefa} não encontrada.")
def menu():
    """
    Exibe um menu para o usuário escolher o que deseja fazer.
    O menu continua aparecendo até que o usuário decida sair.
    """
    while True:
        print("1. Adicionar Tarefa")
        print("2. Mostrar Tarefas")
        print("3. Concluir Tarefa")
        print("4. Excluir Tarefa")
        print("5. Sair")

        opcao = input("Escolha uma opção (1-5): ")

        if opcao == '1':
            descricao = input("Descrição da tarefa: ")
            prazo = input("Prazo (DD-MM-YYYY): ")
            urgencia = input("Urgência (Baixa, Média, Alta): ")
            adicionar_tarefa(descricao, prazo, urgencia)
        elif opcao == '2':
            mostrar_tarefas()
        elif opcao == '3':
            id_tarefa = int(input("ID da tarefa a concluir: "))
            concluir_tarefa(id_tarefa)
        elif opcao == '4':
            id_tarefa = int(input("ID da tarefa a excluir: "))
            excluir_tarefa(id_tarefa)
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

menu()
