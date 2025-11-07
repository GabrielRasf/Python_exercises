a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

if (a < b + c) and (b < a + c) and (c < a + b):
    print('Triângulo')
else:
    print('Não éum triângulo')