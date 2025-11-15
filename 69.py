lista = []

a = 0
b = 1

for i in range(50):
    a, b = b, a + b
    fib = b
    lista.append(fib)

print(lista)