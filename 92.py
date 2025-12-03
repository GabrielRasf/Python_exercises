fila = []
atendimento = []
finalizados = []

def menu():
    print('=================================')
    print('MENU')
    print('1 - Cliente entrou na fila')
    print('2 - Cliente está sendo atendido')
    print('3 - Atendimento finalizado')
    print('0 - Sair')
    print('=================================')
    return int(input("Escolha uma opção: "))

n = menu()

contadorFila = 0

while n != 0:

    # 1 - Entrou na fila
    if n == 1:
        fila.append(contadorFila)

        print('=================================')
        print('Pessoas na fila: {}'.format(len(fila)))
        print('Pessoas sendo atendida: {}'.format(len(atendimento)))
        print('Atendimentos finalizados: {}'.format(len(finalizados)))

        n = menu()

    # 2 - Começou atendimento
    elif n == 2:
        if len(fila) == 0:
            print("Ninguém na fila para atender!")
        else:
            pessoa = fila.pop(0)     
            atendimento.append(pessoa)

        print('=================================')
        print('Pessoas na fila: {}'.format(len(fila)))
        print('Pessoas sendo atendida: {}'.format(len(atendimento)))
        print('Atendimentos finalizados: {}'.format(len(finalizados)))

        n = menu()

    # 3 - Finalizou atendimento
    elif n == 3:
        if len(atendimento) == 0:
            print("Ninguém está sendo atendido para finalizar!")
        else:
            pessoa = atendimento.pop(0) 
            finalizados.append(pessoa)

        print('=================================')
        print('Pessoas na fila: {}'.format(len(fila)))
        print('Pessoas sendo atendida: {}'.format(len(atendimento)))
        print('Atendimentos finalizados: {}'.format(len(finalizados)))

        n = menu()

    else:
        print("Opção inválida!")
        n = menu()

print("Programa encerrado!")
