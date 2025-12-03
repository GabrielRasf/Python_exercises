import random

idades = []

for _ in range(9):
    idade = random.randint(1, 36)
    idades.append(idade)

[print (idade) for idade in idades if idade < 18]


