kmRodados = float(input('Quantos km rodados? '))
dias = float(input('Quantos dias? '))

dia = 60
km = 0.15

valorDia = dia * dias
valorKm = kmRodados * 0.15
valorTotal = valorDia + valorKm

print('O valor a ser pago é {}'.format(valorTotal))