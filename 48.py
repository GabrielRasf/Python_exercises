vI = int(input('N° inicial: '))
vF = int(input('N° final: '))
interacao = int(input('Interação: '))

if vI > vF:
    print('Initial value must be lower than final value')
    vI = int(input('N° inicial: '))
    vF = int(input('N° final: '))

for i in range(vI, vF, interacao):
    print(i)