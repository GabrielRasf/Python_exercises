valor = 0

for i in range(1, 11):
    num = float(input('N°: '))
    valor += num

media = valor / 10

print('Total das notas: {}'.format(valor))
print('Média das notas: {}'.format(media))