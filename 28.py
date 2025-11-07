a = int(input('Valor: '))
b = int(input('Valor: '))

if (a > b):
    print('Valor de a ({}) é maior que b ({})'.format(a, b))
elif (b > a):
    print('Valor de b ({}) é maior que a ({})'.format(b, a))
else:
    print('São iguais')
