n1 = int(input('N° 1: '))

while n1 < 0 or n1 > 10:
    print('Valor inválido')
    n1 = int(input('N° 1: '))
    
n2 = int(input('N° 2: '))

while n2 < 0 or n2 > 10:
    print('Valor inválido')
    n2 = int(input('N° 2: '))

media = (n1 + n2) / 2
print('Média: {}'.format(media))