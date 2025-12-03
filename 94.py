import random

lista = [random.randint(1, 20) for _ in range(20)]

print(lista)

for i in range(len(lista) - 1):
    for j in range(len(lista) - 1 - i):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

print(lista)

print(lista[1])
