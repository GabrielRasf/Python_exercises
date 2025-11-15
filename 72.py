import random

lista = []

for i in range(30):
    n = random.randint(1, 15)
    lista.append(n)

print(lista)

b = int(input('Digite um n°: '))

indice = 0

for val in lista:
    if val == b:
        print(indice, val)
    indice += 1
