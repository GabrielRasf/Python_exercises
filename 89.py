matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print('Matriz original')
for linha in matriz:
    print(linha)

for linha in range(len(matriz)):
    for coluna in range(linha + 1, len(matriz)):
        matriz[linha][coluna], matriz[coluna][linha] = matriz[coluna][linha], matriz[linha][coluna]

print('Matriz transposta')
for linha in matriz:
    print(linha)