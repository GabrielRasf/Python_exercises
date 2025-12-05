produtos = [
    {"nome": "Arroz 5kg", "categoria": "Alimentos", "preco": 16.90},
    {"nome": "Feijão carioca 1kg", "categoria": "Alimentos", "preco": 8.50},
    {"nome": "Macarrão espaguete", "categoria": "Alimentos", "preco": 5.20},
    {"nome": "Açúcar refinado", "categoria": "Alimentos", "preco": 4.99},
    {"nome": "Óleo de soja 900ml", "categoria": "Alimentos", "preco": 7.40},

    {"nome": "Shampoo anticaspa", "categoria": "Higiene", "preco": 18.90},
    {"nome": "Sabonete líquido", "categoria": "Higiene", "preco": 12.70},
    {"nome": "Pasta de dente", "categoria": "Higiene", "preco": 6.40},

    {"nome": "Detergente neutro", "categoria": "Limpeza", "preco": 2.90},
    {"nome": "Esponja de cozinha", "categoria": "Limpeza", "preco": 3.50},
    {"nome": "Desinfetante 1L", "categoria": "Limpeza", "preco": 8.90},

    {"nome": "Fones de ouvido Bluetooth", "categoria": "Eletrônicos", "preco": 79.90},
    {"nome": "Caixa de som portátil", "categoria": "Eletrônicos", "preco": 129.90},
    {"nome": "Mouse sem fio", "categoria": "Eletrônicos", "preco": 39.90},

    {"nome": "Caderno universitário", "categoria": "Papelaria", "preco": 15.90},
    {"nome": "Caneta esferográfica azul", "categoria": "Papelaria", "preco": 2.20},
    {"nome": "Bloco de notas", "categoria": "Papelaria", "preco": 9.90},

    {"nome": "Camiseta básica", "categoria": "Vestuário", "preco": 29.90},
    {"nome": "Calça jeans", "categoria": "Vestuário", "preco": 89.90},
    {"nome": "Tênis esportivo", "categoria": "Vestuário", "preco": 149.90}
]

busca = input('Produto: ').lower()

for produto in produtos:
    if busca in produto["nome"].lower():
        print(produto)