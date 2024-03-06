kw = float(input('quantidade de energia (kwh) consumida: '))
print('r para residências')
print('i para indústrias')
print('c para comércios')
tipo = input('qual o tipo da instalação? ')

if (tipo == 'r'):
    if kw <= 500:
        preco = 0.4
    else:
        preco = 0.65
elif (tipo == 'i'):
    if kw <= 1000:
        preco = 0.55
    else:
        preco = 0.6
elif (tipo == 'c'):
    if kw <= 5000:
        preco = 0.55
    else:
        preco = 0.6
else:
    print('operação inválida')
print('total a pagar: {}'.format(kw * preco))