def rotacionar(vetor, k):
    k = k % len(vetor)

    for _ in range(k):
        ultimo = vetor[-1]
        
        for i in range(len(vetor)-1, 0, -1):
            vetor[i] = vetor[i - 1]

        vetor[0] = ultimo

    return vetor

vetor = [ 1,2,3,4,5]
k = 3
print(rotacionar(vetor, k))