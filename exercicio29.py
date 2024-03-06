print('CALCULADORA')
print('+ para adição')
print('- para subtração')
print('/ para divisão')
print('* para multiplicação')
print('"sair" para sair do programa')
while True:
    op = input('qual operação deseja fazer?: ')
    if (op == '+' or op == '-' or op == '*' or op == '/'):
        n1 = int(input('escreva o primeiro numero: '))
        n2 = int(input('escreva o segundo numero: '))
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
    elif (op == 'sair'):
        break
    else:
        print('operaçãp inválida')
print('ENCERRANDO O PROGRAMA...')