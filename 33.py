codFuncionario = int(input('Código do funcionário: '))
anoNasc = int(input('Ano nascimento: '))
anoIngresso = int(input('Ano de ingnresso na empresa: '))
idadeReal = 2025 - anoNasc
anosTrab = 2025 - anoIngresso

if (idadeReal >= 65):
    print('Requerer aposentadoria')
elif (anosTrab >= 30):
    print('Requerer aposenadoria')
elif (idadeReal >= 60) and (anosTrab >= 25):
    print('Requerer aposentadoria')
else:
    print('Não requerer')

print('Funcionário: {}'.format(codFuncionario))
print('Idade: {}'.format(idadeReal))
print('Tempo na empresa: {}'.format(anosTrab))
