fruta = str(input('Mo - morango || Ma - Maçã\n')).lower()

if (fruta == 'mo'):
    moKg = float(input('Kg: '))
    if (moKg <= 5):
        moPreco = moKg * 2.5
    elif (moKg <= 8):
        moPreco = moKg * 2.2
    else:
        moPreco = moKg * 2.2 * 0.9

    print('Valor: {:.2f}'.format(moPreco))

elif (fruta == 'ma'):
    maKg = float(input('Kg: '))
    if (maKg <= 5):
        maPreco = maKg * 1.8
    elif (maKg <= 8):
        maPreco = maKg * 1.5
    else:
        maPreco = maKg * 1.5 * 0.9

    print('Valor: {:.2f}'.format(maPreco))

else:
    print('Código inválido')
