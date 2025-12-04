import random

lista = [random.randint(-10, 10) for _ in range(20)]

def soma_contigua(lista):
    if len(lista) == 0:
        return 0
    
    soma_atual = lista[0]
    maior_soma = lista[0]
    
    # Começa do segundo elemento (índice 1)
    for posicao in range(1, len(lista)):
        elemento_atual = lista[posicao]
        soma_atual += elemento_atual
        
        if soma_atual > maior_soma:
            maior_soma = soma_atual
            
        if soma_atual < 0:
            soma_atual = 0
    
    return maior_soma

print(lista)
print(soma_contigua(lista))