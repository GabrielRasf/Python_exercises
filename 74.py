import random

palavras = [ "marinheiro", "formigada", "girassois", "notivagos", "boiadeiro", "livreiro", "caminhada", "caranguejo", "tartaruga", "lamparina" ]

palavra = random.choice(palavras)
tracos = ["_"] * len(palavra)
tentativas = 6
palpites = []

while tentativas > 0:
    print(" ".join(tracos))
    palpite = input("Letra: ").lower()

    if palpite in palpites:
        print('Você já tentou essa letra\n')
        continue

    palpites.append(palpite)

    if palpite == palavra:
        tracos = palavra
        break
    
    elif palpite in palavra:
        for i in range(len(palavra)):
            if palavra[i] == palpite:
                tracos[i] = palpite
        print('Acertou! Palavra: {}'.format(palavra))
    
    else:
        tentativas -= 1
        print("================")
        print("Tentativas: {}".format(tentativas))

    if "_" not in tracos:
        print("Palavra: {}".format(palavra))

    if tentativas == 0 and "_" in tracos:
        print("Palavra: {}".format(palavra))
        print("Você perdeu")


