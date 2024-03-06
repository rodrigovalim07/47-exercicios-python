def validaint(pergunta, min, max):
    x = int(input(pergunta))
    while (x < min) or (x > max):
        x = int(input(pergunta))
    return x


def existearquivo(nomearquivo):
    try:
        a = open(nomearquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarquivo(nomearquivo):
    try:
        a = open(nomearquivo, 'wt+')
        a.close()
    except:
        print('erro na criação do arquivo')
    else:
        print('arquivo {} foi criado com sucesso'.format(nomearquivo))


def cadastrarjogo(nomearquivo, nomejogo, nomevideogame):
    try:
        a = open(nomearquivo, 'at')
    except:
        print('erro ao abrir o arquivo')
    else:
        a.write('{};{}\n'.format(nomejogo, nomevideogame))
    finally:
        a.close()


def listararquivo(nomearquivo):
    try:
        a = open(nomearquivo, 'rt')
    except:
        print('erro ao ler o arquivo')
    else:
        print(a.read())
    finally:
        a.close()


arquivo = 'games.txt'
if existearquivo(arquivo):
    print('arquivo localizado no computador')
else:
    print('arquivo inexistente')
    criarquivo(arquivo)
while True:
    print('MENU\n1 - cadastrar novo item? \n2 - listar cadastros\n3 - sair')
    op = validaint('escolha uma opção: ', 1, 3)
    if op == 1:
        print('opção de cadastrar o item selecionada\n')
        nomejogo = input('nome do jogo: ')
        nomevideogame = input('nome do video game: ')
        cadastrarjogo(arquivo, nomejogo, nomevideogame)
    elif op == 2:
        print('opção de listar cadastro selecionada\n')
        listararquivo(arquivo)
    elif op == 3:
        print('encerrando...')
        break
