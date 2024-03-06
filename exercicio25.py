# RESULTADO DE MULTIPLICAÇÃO USANDO SÓ ADIÇÃO E SUBTRAÇÃO

x = int(input('digite um numero: '))
y = int(input('digite outro numero: '))
cont = 1
mult = 0
while (cont <= x):
    mult += y
    cont += 1
print('{} x {} é: {}'.format(x, y, mult))