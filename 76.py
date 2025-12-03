import random

lista = []

for _ in range(20):
    num = random.randint(1,10)
    lista.append(num)
print(lista)

nRemove = int(input('Remove a number - 1 to 10: '))

lista = [num for num in lista if num != nRemove]

print(lista)