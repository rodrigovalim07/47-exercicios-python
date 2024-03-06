print ('escolha o que deseja comprar')
print ('1 - maça')
print ('2 - laranja')
print ('3 - banana')
produto = int(input('qual sua escolha? '))
qnt = int(input('quantas? '))
if (produto == 1):
    pagar = qnt * 2.3
    print('voce comprou {} maças, valor a se pagar: {}'.format(qnt, pagar))
elif (produto == 2):
    pagar = qnt * 3.6
    print('voce comprou {} laranjas, valor a se pagar: {}'.format(qnt, pagar))
elif (produto == 3):
    pagar = qnt * 1.85
    print('voce comprou {} bananas, valor a se pagar: {}'.format(qnt, pagar))
else: print('produto inexistente')