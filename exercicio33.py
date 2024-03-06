# NUMEROS PRIMOS DE 2 A 99

print('numeros primos de 2 a 99:')
for numero in range (2, 100, 1):
    flag = 0                      #FLAG começa como falso pois nao foi feito o mod dele ainda
    for i in range (2, numero, 1):
        if (numero % i == 0): # feito o mod, se o numero for divisivel por algum ele recebe 1 pra se tornar true
            flag = 1
            break
    if not flag: #dar print dos numeros q nao foram divididos por nenhum a nao ser 1 e ele msm
        print(numero)