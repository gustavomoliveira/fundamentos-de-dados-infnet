from funcionario.funcionario_manager import Funcionario

def menu():
    funcionario_manager = Funcionario()
    while True:
        print("\n" + "=" * 30)
        print("  🏢 Gestão de Funcionários  ")
        print("=" * 30)
        print("1  Listar funcionários")
        print("2  Adicionar funcionário")
        print("3  Atualizar funcionário")
        print("4  Excluir funcionário")
        print("5  Sair")
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            funcionario_manager.listar_funcionario()
        elif opcao == "2":
            funcionario_manager.adicionar_funcionario()
        elif opcao == "3":
            funcionario_manager.atualizar_funcionario()
        elif opcao == "4":
            funcionario_manager.excluir_funcionario()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

menu()