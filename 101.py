def verificador_palindromo(palavra):

    palavra_invertida = ""

    for letra in palavra:
        palavra_invertida = letra + palavra_invertida

    print(palavra_invertida)

    return palavra == palavra_invertida

verificador_palindromo('Araraquara')