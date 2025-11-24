import random

listaA = []
listaB = []

for n in range(10):
    a = random.randint(1, 10)
    listaA.append(a)

print(listaA)

x = int(input('N°: '))        

for y in range(len(listaA)):
    mult = print(x * listaA[y])
    listaB.append(mult)

print(listaB)