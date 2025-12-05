produtos = [
    # --- ALIMENTOS ---
    {"nome": "Arroz 5kg", "categoria": "Alimentos", "preco": 16.90},
    {"nome": "Feijão carioca 1kg", "categoria": "Alimentos", "preco": 8.50},
    {"nome": "Macarrão espaguete", "categoria": "Alimentos", "preco": 5.20},
    {"nome": "Açúcar refinado", "categoria": "Alimentos", "preco": 4.99},
    {"nome": "Óleo de soja 900ml", "categoria": "Alimentos", "preco": 7.40},
    {"nome": "Leite integral 1L", "categoria": "Alimentos", "preco": 4.80},
    {"nome": "Café torrado e moído", "categoria": "Alimentos", "preco": 17.90},
    {"nome": "Biscoito de chocolate", "categoria": "Alimentos", "preco": 3.90},
    {"nome": "Manteiga 200g", "categoria": "Alimentos", "preco": 9.50},

    # --- HIGIENE ---
    {"nome": "Shampoo anticaspa", "categoria": "Higiene", "preco": 18.90},
    {"nome": "Sabonete líquido", "categoria": "Higiene", "preco": 12.70},
    {"nome": "Pasta de dente", "categoria": "Higiene", "preco": 6.40},
    {"nome": "Escova de dentes", "categoria": "Higiene", "preco": 4.20},
    {"nome": "Desodorante aerosol", "categoria": "Higiene", "preco": 11.50},
    {"nome": "Algodão 50g", "categoria": "Higiene", "preco": 3.80},

    # --- LIMPEZA ---
    {"nome": "Detergente neutro", "categoria": "Limpeza", "preco": 2.90},
    {"nome": "Esponja de cozinha", "categoria": "Limpeza", "preco": 3.50},
    {"nome": "Desinfetante 1L", "categoria": "Limpeza", "preco": 8.90},
    {"nome": "Sabão em pó 1kg", "categoria": "Limpeza", "preco": 12.60},
    {"nome": "Amaciante 2L", "categoria": "Limpeza", "preco": 10.50},
    {"nome": "Água sanitária 2L", "categoria": "Limpeza", "preco": 4.30},

    # --- ELETRÔNICOS ---
    {"nome": "Fones de ouvido Bluetooth", "categoria": "Eletrônicos", "preco": 79.90},
    {"nome": "Caixa de som portátil", "categoria": "Eletrônicos", "preco": 129.90},
    {"nome": "Mouse sem fio", "categoria": "Eletrônicos", "preco": 39.90},
    {"nome": "Teclado mecânico", "categoria": "Eletrônicos", "preco": 199.90},
    {"nome": "Monitor 24 polegadas", "categoria": "Eletrônicos", "preco": 699.00},
    {"nome": "Carregador de celular", "categoria": "Eletrônicos", "preco": 25.90},

    # --- PAPELARIA ---
    {"nome": "Caderno universitário", "categoria": "Papelaria", "preco": 15.90},
    {"nome": "Caneta esferográfica azul", "categoria": "Papelaria", "preco": 2.20},
    {"nome": "Bloco de notas", "categoria": "Papelaria", "preco": 9.90},
    {"nome": "Lápis grafite", "categoria": "Papelaria", "preco": 1.50},
    {"nome": "Borracha branca", "categoria": "Papelaria", "preco": 1.20},
    {"nome": "Marcador de texto", "categoria": "Papelaria", "preco": 4.80},

    # --- VESTUÁRIO ---
    {"nome": "Camiseta básica", "categoria": "Vestuário", "preco": 29.90},
    {"nome": "Calça jeans", "categoria": "Vestuário", "preco": 89.90},
    {"nome": "Tênis esportivo", "categoria": "Vestuário", "preco": 149.90},
    {"nome": "Jaqueta corta-vento", "categoria": "Vestuário", "preco": 119.90},
    {"nome": "Boné ajustável", "categoria": "Vestuário", "preco": 25.90},
    {"nome": "Meias esportivas (3 pares)", "categoria": "Vestuário", "preco": 14.90},
]

def ordenacaoPrecos(produtos):

    for i in range(len(produtos) - 1):
        for j in range(len(produtos) - 1 - i):
            if produtos[j]["preco"] > produtos[j + 1]["preco"]:
                produtos[j], produtos[j + 1] = produtos[j + 1], produtos[j]
    return produtos

ordenados = ordenacaoPrecos(produtos)

for p in ordenados:
    print(p)

    