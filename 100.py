def inverter_lista(frase):
    palavras = frase.split()
    print(palavras)

    frase_invertida = []

    for i in range(len(palavras) -1, -1, -1):
        frase_invertida.append(palavras[i])
    
    print(frase_invertida)

    return " ".join(frase_invertida)

print(inverter_lista('Bom dia, senhorita!'))    