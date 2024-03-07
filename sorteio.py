import random
listasorteio = []

while True:
    s = input('Deseja adicionar doadores? 1 - SIM     2 - NÃO: ')   # validando se o usuário deseja adicionar doadores
    if (s == '2'):
        print('Sorteando...\n')
        break
    elif (s != '1'):
        continue
    pessoas = (input('Nome do doador: '))   # adicionando o nome do doador e o valor doado
    x = (int(input('Qual o valor doado: ')))
    y = x // 10  # para cada 10 reais sera adicionado o nome uma vez, entao eu pego o valor doado e faço uma divisão inteira pra eliminar o resto
    for i in range(y):  # adicionando o nome na lista de acordo com o resultado de y, o resultado de y é quantas vezes sera adici-onado
        listasorteio.append(pessoas)


random.shuffle(listasorteio)    # embaralhando a lista
sorteado = random.choice(listasorteio)  # sortenado aleatório um nome
print('O ganhador do sorteio foi: {}'.format(sorteado)) # prints de quem foi sorteado e a lista como pedido no exercício
print('A lista do sorteio: {}'.format(listasorteio))
