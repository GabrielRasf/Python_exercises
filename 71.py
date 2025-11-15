lista = []

for i in range(10):
    n = int(input('N°: '))
    lista.append(n)

    if n % 2 == 0:
        print('Posição {} -> Valor {}'.format(lista[i], n))
