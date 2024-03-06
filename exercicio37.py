def maior3 (n1=0, n2=0, n3=0):
    if (n1 and n2 and n3):
        if (n1>n2 and n1>n3):
            if (n2>n3):
                print('ordem crescente: {}, {}, {}'.format(n3, n2, n1), end='')
            else:
                print('ordem crescente: {}, {}, {}'.format(n2, n3, n1), end='')
        elif (n2>n1 and n2>n3):
            if (n1>n3):
                print('ordem crescente: {}, {}, {}'.format(n3, n1, n2), end='')
            else:
                print('ordem crescente: {}, {}, {}'.format(n1, n3, n2), end='')
        elif (n3>n1 and n3>n2):
            if (n1>n2):
                print('ordem crescente: {}, {}, {}'.format(n2, n1, n3), end='')
            else:
                print('ordem crescente: {}, {}, {}'.format(n1, n2, n3), end='')
while True:
    print('ORGANIZANDO EM ORDEM CRESCENTE')
    s = input('incerir dados? s - sim     n - nao: ')
    if (s == 'n'):
        print('ENCERRANDO...')
        break
    elif (s != 's'):
        print('COMANDO INVÁLIDO, TENTE NOVAMENTE')
        continue
    a = int(input('digite o primeiro numero: '))
    b = int(input('digite o segundo numero: '))
    c = int(input('digite o terceiro numero: '))
    maior3(c,a,b)  # nao importa a ordem q eu colocar as variaveis
    print('\n')