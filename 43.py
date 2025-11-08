n = int(input('N°: '))

while n <= 0 or n >= 11:
    print('Valores entre 1 e 10')
    n = int(input('N°'))

for i in range(1, 11):
    print('{} x {} = {}'.format(n, i, n*i))