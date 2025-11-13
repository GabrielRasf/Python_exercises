lista = []

while True:
    n = int(input('N°: '))
    if n == 0:
        break
    lista.append(n)

maior = lista[0]

for num in lista:
    if num > maior:
        maior = num
    
print(maior)
print(lista)