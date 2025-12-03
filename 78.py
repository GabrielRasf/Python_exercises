import random 

lista = []

for n in range(20):
    n = random.randint(1, 100)
    lista.append(n)

print(lista)

maior = lista[0]
menor = lista[0]

posiMaior = 0
posiMenor = 0

for i in range(len(lista)):
    if lista[i] > maior:
        maior = lista[i]
        posiMaior = i
    if lista[i] < menor:
        menor = lista[i]
        posiMenor = i

print(posiMaior)
print(maior)

print(posiMenor)
print(menor)
