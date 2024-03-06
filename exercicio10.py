n1 = int(input('valor primeiro lado: '))
n2 = int(input('valor segundo lado: '))
n3 = int(input('valor terceiro lado: '))
if (n1 == 0 or n2 == 0 or n3 == 0):
    print ('nenhum lado pode ser igual a zero')
elif (n1 > n2 + n3 or n2 > n1 + n3 or n3 > n1 + n2):
    print('nenhum dos lados pode ser maior que a soma dos outros dois')
elif (n1 == n2 == n3):
    print('seu triangulo é equilatero')
elif (n1 != n2 != n3):
    print('seu triangulo é escaleno')
elif (n1 == n2 or n1 == n3 or n2 == n3):
    print('seu triangulo é isosseles')