n1 = float(input('N°: '))
n2 = float(input('N°: '))
n3 = float(input('N°: '))

maior = n1

if (n1 > n2) and (n1 > n3):
    print('Maior n° é {}'.format(n1))
elif (n2 > n1) and (n2 > n3):
    print('Maior n° é {}'.format(n2))
else:
    print('Maior n° é {}'.format(n3))

