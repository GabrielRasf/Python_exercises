import random

lista = [random.randint(-15, 15) for _ in range(20)]
print('Lista: {}'.format(lista))

# Maior e menor
maior = lista[0]
menor = lista[0]

for num in lista:
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print('Menor: {}'.format(menor))
print('Maior: {}'.format(maior))

# Média
soma = 0
contador = 0
for num in lista:
    soma += num
    contador += 1

media = soma / contador
print('Média: {}'.format(media))

# Positivos, zeros e negativos
contadorZ = 0
contadorP = 0
contadorN = 0

for num in lista:
    if num == 0:
        contadorZ += 1
    if num % 2 == 0:
        contadorP += 1
    else:
        contadorN += 1

print('Qtde zeros: {}'.format(contadorZ))
print('Qtde positivos: {}'.format(contadorP))
print('Qtde negativos: {}'.format(contadorN))