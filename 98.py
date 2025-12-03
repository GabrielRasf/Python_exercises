import random

lista = [random.randint(1, 10) for _ in range(10)]
print(lista)

for i in range(len(lista) - 1):
    for j in range(len(lista) - 1 - i):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

print(lista)

alvo = random.randint(1, 10)
print('Alvo: {}'.format(alvo))

inicio = lista[0]
fim = len(lista) - 1

while inicio <= fim:
    meio = (inicio + fim) // 2
    print('Meio da lista: {}'.format(meio))

    if lista[meio] == alvo:
        print('Valor encontrado: {}'.format(alvo))
        break 
    
    elif lista[meio] < alvo:
        inicio = meio + 1
    
    else:
        fim = meio - 1

