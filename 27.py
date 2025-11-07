a = int(input('Gols'))
b = int(input('Gols'))

if (a > b):
    print('Time A venceu por {} a {}'.format(a, b))
elif (b > a):
    print('Time B venceu por {} a {}'.format(b, a))
else:
    print('Empate')