tipo = str(input('a -> ácool | g -> gasolina\n'))

if (tipo == 'a'):

    litros_a = float(input('Litros álcool: '))

    if (litros_a <= 20):
        preco_a = litros_a * 0.97
        print(preco_a)
    else:
        preco_a = litros_a * 0.95
        print(preco_a)

elif (tipo == 'g'):

    litros_g = float(input('Litros gasolina'))

    if (litros_g <= 20):
        preco_g = litros_g * 0.96
        print(preco_g)
    else:
        preco_g = litros_g * 0.94
        print(preco_g)
