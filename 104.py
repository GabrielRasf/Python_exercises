produtos = [
    {"nome": "Caderno", "categoria": "Papelaria", "preco": "14.90"},
    {"nome": "Mouse", "categoria": "Eletrônicos", "preco": "47.90"},
    {"nome": "Café", "categoria": "Alimentos", "preco": "24.90"},
]

for produto in produtos:
    print(produto)

print("=====================================")

print(produtos[0])
print(produtos[1])
print(produtos[2])

print("=====================================")

print('Este é o elemento 1 da lista: {}'.format(produtos[0]))