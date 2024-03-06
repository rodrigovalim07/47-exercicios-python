pessoas = 0
somaingre = 0
contidade = 0
ingresso = 0
while True:
    idade = input('quantos anos voce tem? ')
    if idade == 's':
        break
    idade = int(idade)
    pessoas += 1
    if idade < 3:
        ingresso = 0
        print('total a pagar: {}'.format(ingresso))
    elif idade >= 3 and idade <= 12:
        ingresso = 15
        print('total a pagar: {}'.format(ingresso))
    elif idade > 12:
        ingresso = 30
        print('total a pagar: {}'.format(ingresso))
    contidade += idade
    somaingre += ingresso
mediaidade = contidade / pessoas
print('total de pessoas que assistiram ao filme: {}'.format(pessoas))
print('total de dinheiro arrecadado: {}'.format(somaingre))
print('média de idade das pessoas : {}'.format(mediaidade))
