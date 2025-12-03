n = int(input("N°: "))

if n < 0:
    print("Digite um número não negativo!")
elif n <= 1:
    print(n)
else:
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    print(b)

