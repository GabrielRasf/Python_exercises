n = int((input('N°: ')))

for i in range (n, 0, -1):
    print(i)
    i -= 1
    if i % 4 == 0:
        print('[{}]'.format(i))
