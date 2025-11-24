import random

notas = []
soma = 0
for i in range(20):
    nota = random.randint(100, 1000) / 100
    notas.append(nota)
    soma += nota

print(notas)
print(soma)

media = soma / len(notas)

print(media)