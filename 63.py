lista = []

while True:
    n = int(input('N°: '))
    if(n == 999):
        break
    if(n % 2 == 0):
        lista.append(n)

print(lista)