import random

listaA = []
listaB = []
listaIguais = []

for _ in range(15):
    listaA.append(random.randint(1, 10))

for _ in range(15):
    listaB.append(random.randint(1, 10))

print("A:", listaA)
print("B:", listaB)

count = 0

for i in range(15):
    if listaA[i] == listaB[i]:
        listaIguais.append(listaA[i])
        count += 1

print("\nIguais nas mesmas posições:", listaIguais)
print("Total:", count)
