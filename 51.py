interv = 0
foraInterv = 0
n = 0

while n <= 10:
    num = int(input('N°: '))
    if (10 <= num <= 20):
        interv += 1
    else:
        foraInterv += 1
    n += 1

print('Intervalo: {}'.format(interv))
print('Fora do intervalo: {}'. format(foraInterv))