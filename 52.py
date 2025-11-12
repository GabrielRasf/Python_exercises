sum = 0
cont = 0

while cont < 10:
    num = float(input('N°: '))
    sum += num
    cont += 1

media = sum / cont

print('Soma: {}'.format(sum))
print('Media: {}'.format(media))