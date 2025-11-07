nome = str(input('Produto: '))
qtd = int(input('Quantidade: '))
precoUni = float(input('Preço: '))
precoTotal = precoUni * qtd

if qtd <= 5:
    desconto = 0.02
elif qtd <= 10:
    desconto = 0.03
else:
    desconto = 0.05

precoComDesc = precoTotal * (1 - desconto)

print('Produto:', nome)
print('Preço total:', precoTotal)
print('Preço com desconto:', precoComDesc)
