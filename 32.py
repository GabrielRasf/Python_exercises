n1 = float(input('Nota: '))
n2 = float(input('Nota: '))
n3 = float(input('Nota: '))

media = (n1 + n2 + n3) / 3

mediaA = (n1 + n2 * 2 + n3 * 3 + media) / 7
print('Média: {:.2f}'.format(mediaA))

if (mediaA >= 9):
    print('A')
elif (mediaA >= 7.5):
    print('B')
elif (mediaA >= 6):
    print('C')
else:
    print('D')

