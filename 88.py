import random

numSecreto = random.randint(1,10)
listaChutes = []
print(numSecreto)

while True:
    chute = int(input('N°: '))
    if chute == "":
        print('Entrada vazia. Digite um n°.')
        continue

    if chute != numSecreto:
        if chute in listaChutes:
            print('Já tentou este número. Tente outro!')
            continue
        listaChutes.append(chute)
        print(listaChutes)

    else:
        print('Acertou! N° secreto é {}'.format(numSecreto))
        break

