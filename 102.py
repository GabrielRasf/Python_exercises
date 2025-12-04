produtos = [
    "Arroz 5kg",
    "Feijão carioca 1kg",
    "Macarrão espaguete",
    "Óleo de soja",
    "Açúcar refinado",
    "Sabonete líquido",
    "Shampoo anticaspa",
    "Pasta de dente",
    "Detergente neutro",
    "Esponja de cozinha",
    "Papel higiênico (12 rolos)",
    "Café em pó",
    "Leite integral",
    "Leite desnatado"
    "Manteiga",
    "Biscoito cream cracker",
    "Garrafa térmica",
    "Fones de ouvido Bluetooth",
    "Caderno universitário",
    "Caneta esferográfica azul",
    "Pilhas AA (4 unidades)",
]

removidos = []

def mostrarProdutos():
    for produto in produtos:
        print(produto)

print("============")
print("MENU")
print("============")
print("1 - Adiconar produto")
print("2 - Procurar produto")
print("3 - Remover produto")
print("4 - Mostrar lista de produtos")
print("0 - Sair")

while True:
    menu = int(input('Opção:'))

    match menu:
        case 1:
            addProduto = input('Nome do produto: ').capitalize()
            produtos.append(addProduto)
            print('{} adicionado'.format(addProduto))
            mostrarProdutos()

        case 2:
            busca = input('Digite o nome de um produto: ').lower()
            for item in produtos:
                if busca in item.lower():
                    print(item)

        case 3:
            busca = input('Digite o nome de um produto: ').lower()
            for item in produtos:
                if busca in item.lower():
                    removidos.append(item)
                    produtos.remove(item)
                    print('{} removido'.format(item))
                    print(removidos)

        case 4:
            mostrarProdutos()
            
        case 0:
            break


print(produtos)