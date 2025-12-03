import random

lista = [random.randint(1, 10) for _ in range(30)]
listaRem = []

for num in lista:
    if num not in listaRem:
        listaRem.append(num)
    else:
        continue
    
print(lista)
print(listaRem)