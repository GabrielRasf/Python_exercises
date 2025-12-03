lista = []
soma = 0

while True:
    n = int(input('N°: '))
    if n == 0:
        break
    lista.append(n)
    soma += n

print(soma)
print(lista)