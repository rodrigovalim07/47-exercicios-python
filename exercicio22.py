#MÉDIA DOS PARES DE 1 A 100
soma = 0
qnt = 0
for x in range (1,101):
    if (x % 2 == 0):
        soma += x
        qnt += 1
media = soma / qnt
print('a média de numeros pares de 0 a 100 é: {}'.format(media))