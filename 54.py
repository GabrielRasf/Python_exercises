maiores = []
menores = []
count = 0
num = 0
somaMenores = 0

while count < 10:
    num = float(input('N°: '))
    if num < 40:
        menores.append(num)
        somaMenores += num
    else:
        maiores.append(num)

    count += 1

print('Maiores: {}'.format(maiores))
print('Menores: {}'.format(menores))
print('Soma: {}'.format(somaMenores))

