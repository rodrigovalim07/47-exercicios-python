deposito = []   # criando a lista deposito e o dicionario produto
produto = {}
deposito_ordenado = []

while True:
    # na chave codigo adiciono o dado condizente ao codigo do produto, e assim nas demais chaves serao inseridos os dados
    produto['codigo'] = int(input('Código do produto: '))
    if produto['codigo'] == 0:  # se o código receber valor 0 ele interrompe a leitura e encerra o laço
        print('Encerrando...')
        break
    produto['estoque'] = int(input('Estoque atual do produto: '))
    produto['minimo'] = int(input('Estoque mínimo necessário: '))
    deposito.append(produto.copy())  # adicionando o dicionario produto dentro da lista deposito


# deposito ordenado recebendo o deposito com a chave codigo organizada em forma crescente
deposito_ordenado = sorted(deposito, key=lambda item: item['codigo'])
print(deposito_ordenado)
