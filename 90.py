import time
listaProduto = []

def menu():
    print("===========================")
    print("MENU DA LOJA")
    print("===========================")
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Listar produtos em estoque")
    print("4 - Sair")

while True:

    try:
        menu()
        opcao = int(input("Opção: ").strip())
    except ValueError:
        print("Digite um número válido!")
        continue
    

    # 1 - Adicionar
    if opcao == 1:
        produto = input("Nome do produto: ").strip().capitalize()
        listaProduto.append(produto)
        print('{} adicionado ao estoque'.format(produto))

    # 2 - Remover
    elif opcao == 2:
        procurar = input("Digite o nome para remover: ").strip().capitalize()

        if procurar in listaProduto:
            listaProduto.remove(procurar)
            print('{} removido do estoque'.format(procurar))
        else:
            print("Produto não encontrado!")

    # 3 - Listar
    elif opcao == 3:
        print("===========================")
        print("Produtos em estoque:".upper())
        print("===========================")
        for item in listaProduto:
            print("- {}".format(item))

    # 4 - Sair
    elif opcao == 4:
        print("Saindo...")
        time.sleep(2)
        print("Saiu")
        break

    else:
        print("Opção inválida!")
