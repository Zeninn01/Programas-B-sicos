Lista = []

def mostrar_lista():
    """Exibe a lista."""
    if not Lista:
        print("A lista está vazia!")
        
    else:
        print("\n Sua lista:")
        for i, tarefa in enumerate(Lista, start = 1):
            print(f"{i}. {tarefa}")
    print() #Linha vazia pra deixar bonito

def adicionar_item():
    """Adiciona um item a lista"""
    tarefa = input("Digite o que você quer adicionar: ")
    Lista.append(tarefa)
    print(f"Item '{tarefa}' adicionada com sucesso!\n")
    
def remover_item():
    """Remove um item da lista."""
    mostrar_lista()
    try:
        indice = int(input("Digite o número de itens que deseja remover: ")) - 1
        if 0 <= indice < len(Lista):
            item_removido = Lista.pop(indice)
            print(f"Item '{item_removido}' removida com sucesso!\n")
        else:
            print("Número invalido, tente novamente.\n")
    except ValueError:
        print("Entrada invalida! Por favor, digite um número.\n")
        
def exibir_menu():
    """Exibe o menu e lida com a escolha do usuário."""
    while True:
        print("---- MENU ----")
        print("1. Mostrar tarefas")
        print("2. Adicionar tarefa")
        print("3. Remover tarefa")
        print("4. Sair")
        
        escolha = input("Escolha um opção: ")
        
        if escolha == "1":
            mostrar_lista()
        elif escolha == "2":
            adicionar_item()
        elif escolha == "3":
            remover_item()
        elif escolha == "4":
            print("Fechando programa...")
            break
        else:
            print("Opção invalida! Tente Novamente.\n")
            
#Executar programa \/     
exibir_menu()
