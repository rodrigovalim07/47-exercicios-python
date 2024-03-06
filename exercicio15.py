soma = 0
cont = 1
while (cont <= 5):
    x = float(input('qual a {}º nota: '.format(cont)))
    soma += x   # equivalente: soma = soma + x
    cont += 1   # equivalente: cont = cont + 1
media = soma / 5    # equivalente: media = soma / cont
print('sua nota média nas matérias é: {}'.format(media))