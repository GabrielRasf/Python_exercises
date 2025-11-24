import random

lista = []

for _ in range(30):
    n = random.randint(1, 10)
    lista.append(n)

print(lista)

count = 0
nGoal = int(input('N°: '))

for num in lista:
    if num == nGoal:
        count += 1

print('O número {} aparece {} vezes'.format(nGoal, count))