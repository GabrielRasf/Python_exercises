a = float(input('N°: '))
b = float(input('N°: '))

while True:
    if (b == 0):
        print('Valor inválido')
        b = float(input('N°: '))
    else:
        break

div = a / b

print('{} : {} = {}'.format(a, b, div))