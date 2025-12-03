import random

lista = [random.randint(1, 10) for _ in range(20)]
listaDup = []

print(lista)

for i in lista:
    if i not in listaDup:
        listaDup.append(i)
    if i in listaDup:
        continue
    
print(listaDup)