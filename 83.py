matriz = []

for linha in range(3):
    linha = []
    for coluna in range(3):
        valor = int(input('Valor: '))
        linha.append(valor)
    matriz.append(linha)

soma = 0
for linha in matriz:
    print(linha)

# Soma linha
for linha in range(3):
    soma_linha = 0
    for coluna in range(3):
        soma_linha += matriz[linha][coluna]
    print('Linha {}: {}'.format(linha + 1, soma_linha))

#Soma coluna
for coluna in range(3):
    soma_coluna = 0
    for linha in range(3):
        soma_coluna += matriz[linha][coluna]
    print('Coluna {}: {}'.format(coluna + 1, soma_coluna))