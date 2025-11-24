# --------------------------------------------------------------
# 1) Texto para análise
# --------------------------------------------------------------
texto = """O vento soprava leve naquela manhã de domingo, deslizando entre as árvores como quem sabe exatamente para onde quer ir. As ruas ainda estavam silenciosas, pontuadas apenas pelo canto distante de algum passarinho teimoso em começar o dia mais cedo. Clara caminhava devagar, observando cada detalhe, como se o mundo tivesse diminuído a velocidade só para que ela pudesse apreciá-lo.
Carregava consigo uma xícara de café quente e uma sensação tranquila de que, apesar de tudo, as coisas eventualmente se ajeitam. Não era um pensamento otimista demais, nem ingênuo — era apenas um entendimento simples, amadurecido com o tempo. Enquanto caminhava, sentiu que aquele seria um bom dia. Talvez não extraordinário, nem memorável, mas bom o suficiente para deixá-la contente. E às vezes, isso era tudo que alguém precisava."""

# Separar o texto em palavras

lista_de_palavras_brutas = texto.split()

# Criar um dicionário para armazenar a frequência das palavras

frequencia_das_palavras = {}

# Processar cada palavra:

for palavra in lista_de_palavras_brutas:

    # converter para minúsculo
    palavra_limpa = palavra.lower()

    # remover pontuação
    palavra_limpa = palavra_limpa.strip(".,!?—…“”\"")

    # evitar palavras vazias após limpeza
    if palavra_limpa == "":
        continue

    # registrar contagem no dicionário
    if palavra_limpa not in frequencia_das_palavras:
        frequencia_das_palavras[palavra_limpa] = 1
    else:
        frequencia_das_palavras[palavra_limpa] += 1

# Encontrar quais palavras aparecem exatamente 1 vez
palavras_unicas = []  
for palavra, quantidade in frequencia_das_palavras.items():
    if quantidade == 1:
        palavras_unicas.append(palavra)

# Encontrar a maior frequência encontrada no texto
maior_frequencia = max(frequencia_das_palavras.values())

# Encontrar TODAS as palavras que possuem essa maior frequência
palavras_mais_frequentes = []

for palavra, quantidade in frequencia_das_palavras.items():
    if quantidade == maior_frequencia:
        palavras_mais_frequentes.append(palavra)

# Exibir resultados
print("-" * 60)
print("TOTAL DE PALAVRAS APÓS DIVISÃO COM SPLIT:", len(lista_de_palavras_brutas))
print("TOTAL DE PALAVRAS ÚNICAS:", len(palavras_unicas))
print("MAIOR FREQUÊNCIA REGISTRADA:", maior_frequencia)
print("-" * 60)

print("\nPALAVRAS QUE APARECEM APENAS UMA VEZ:")
print(palavras_unicas)

print("\nPALAVRAS QUE MAIS APARECEM (CONSIDERANDO EMPATE):")
print(palavras_mais_frequentes)

print(texto.lower())
print(texto.upper())
