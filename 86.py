lista = []

nota = float(input('Nota: '))
soma = 0
contador = 0

while True:
    if nota >= 0 and nota <= 10:
        lista.append(nota)
        soma += nota
        contador += 1
        nota = float(input('Nota: '))

    else:
        break

media = soma / contador

print(lista)
print(media)
