n = int(input('N°: '))

while n <= 0:
    print('N° deve ser maior que zero')
    n = int(input('N°: '))

for i in range(1, n):
    print(i)
    i += 1