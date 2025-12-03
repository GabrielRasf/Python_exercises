n = int(input('N°: '))

def eh_primo(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

if eh_primo(n):
    print('{} é primo'.format(n))
else:
    print('{} não é primo'.format(n))