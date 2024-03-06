n1 = int(input('escreva um numero: '))
n2 = int(input('escreva outro numero: '))
print('+ para adição')
print('- para subtração')
print('/ para divisão')
print('* para multiplicação')
op = input('qual operação deseja fazer?: ')
if (op == '+'):
    res = n1 + n2
    print('o resultado do {} + {} é: {}'.format(n1, n2, res))
elif (op == '-'):
    res = n1 - n2
    print('o resultado do {} - {} é: {}'.format(n1, n2, res))
elif (op == '/'):
    res = n1 / n2
    print('o resultado do {} / {} é: {}'.format(n1, n2, res))
elif (op == '*'):
    res = n1 * n2
    print('o resultado do {} * {} é: {}'.format(n1, n2, res))
else:
    print('operação nao encontrada')