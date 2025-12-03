# n = int(input('Number: '))
# num = str(n)

# print('Analisando o n°: {}'.format(num))
# print('Número: {}'.format(num))
# print('Milhar: {}'.format(num[0]))
# print('Centena: {}'.format(num[1]))
# print('Dezena: {}'.format(num[2]))
# print('Unidade: {}'.format(num[3]))

n = int(input('Number: '))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print('Analisando o n°: {}'.format(n))
print('Milhar: {}'.format(m))
print('Centena: {}'.format(c))
print('Dezena: {}'.format(d))
print('Unidade: {}'.format(u))