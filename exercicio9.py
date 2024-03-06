nome = input('qual seu nome? ')
anos = int(input('quantos anos voce tem?: '))
if (nome == 'rodrigo' and anos == 23):
     print('bem vindo')
if (nome == 'rodrigo' and anos != 23):
     print('voce nao é o rodrigo')
if (anos < 18):
    print('voce é menor de idade')
if (anos > 130):
    print('voce nao existe')
