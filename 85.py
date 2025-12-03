import random

def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == alvo:
            return meio 

        elif lista[meio] < alvo:
            inicio = meio + 1

        else:
            fim = meio - 1 

    return -1

lista = [random.randint(10, 30) for n in range(20)]
print(lista)

for i in range(len(lista) - 1):
    for j in range(len(lista) - 1 - i):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]


print(lista)
pos = busca_binaria(lista, 20)

print(pos) 
