inicial = int(input('escreva um valor inicial: '))
final = int(input('escreva um valor final: '))
intposi = 0
somaposi = 0
pares = 0
somapar = 0
impar = 0
somaimpar = 0
if (inicial < final):
  while (inicial <= final):
    if (inicial % 2 == 0):
      pares += 1
      somapar += inicial
    else:
      impar += 1
      somaimpar += inicial
    if (inicial > 0 and inicial <= final):
      intposi += 1
      somaposi += inicial
    inicial += 1
mediapar = somapar / pares
mediaimpar = somaimpar / impar
mediaposi = somaposi / intposi
print('A quantidade de números inteiros e positivos é: {}'.format(intposi))
print('A quantidade de números pares é: {}'.format(pares))
print('A quantidade de números ímpares é: {}'.format(impar))
print('A média dos numeros é: {}'.format(mediaposi))
print('A média dos numeros pares é: {}'.format(mediapar))
print('A média dos numeros ímpares é: {}'.format(mediaimpar))