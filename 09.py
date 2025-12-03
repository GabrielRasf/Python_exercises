import math

num = int(input('N°: '))

dobro = num  * 2
triplo = num * 3
raiz = math.sqrt(num)

print(dobro)
print(triplo)
print(raiz)

print('O dobro de {} é {}.'.format(num, dobro))
print('O triplo de {} é {}'.format(num, triplo))
print('A raíz quadrada de {} é {}'.format(num, raiz))