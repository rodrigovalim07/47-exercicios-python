def contador(inicio=0, fim=0, passo=1):
    for i in range(inicio, fim, passo):
        print('{} '.format(i), end='')
    print('\n') # fez pular duas linhas
contador(0, 200, 5)