nome = ''
while not nome:   #while nao começa se nao for valor verdadeiro, entao estou negando um valor falso #só repete se mantiver verdadeiro
    nome = input('qual seu nome? ')
valor = int(input('digite um numero : '))
if valor:
    print('voce digitou um valor diferente de zero')
else:
    print('voce digitou numero zero')