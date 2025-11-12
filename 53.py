alunos = []
notas = []
soma = 0
qtdeAlunos = int(input('Qtde de anos: '))

for i in range(qtdeAlunos):
    nome = str(input('Nomes'))
    nota = float(input('Nota: '))

    alunos.append(nome)
    notas.append(nota)
    soma += nota

media = soma / qtdeAlunos


print('Alunos: {}'.format(alunos))
print('Notas: {}'.format(notas))
print('Soma das notas: {}'.format(soma))
print('Media: {}'.format(media))
