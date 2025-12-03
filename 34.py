a = float(input('N°: '))
b = float(input('N°: '))

while b == 0:
    print('Precisa ser maior que zero')
    b = float(input('N°: '))

div = a / b

print('{:.2f} : {:.2f} é {:.2f}'.format(a, b, div))
