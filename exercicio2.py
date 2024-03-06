km = int(input('quantos kilomêtros você andou no carro: '))
dia = int(input('quantos dias você ficou com o carro?: '))
preco = 60 * dia + 0.15 * km

print('dias alugado: {}. km rodados: {}'.format(dia, km))
print('valor a ser pago: {}'.format(preco))