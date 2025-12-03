lista = ['a', 'b', 'c']
preco = [5, 8, 12]

# Mostrando os produtos disponíveis
print("Produtos disponíveis:")
for i in range(len(lista)):
    print("{}. {} - R$ {}".format(i+1, lista[i], preco[i]))

# Pergunta qual produto o usuário quer
escolha = int(input("Escolha o número do produto: ")) - 1

# Pergunta a quantidade
quantidade = int(input("Quantidade: "))

# Calcula o valor final
valorFinal = quantidade * preco[escolha]

print("Total a pagar: R$ {}".format(valorFinal))
