# CÉDULAS DE TROCO
while True:
    valor = int(input('digite um valor em R$: '))
    if (valor >= 100):
        troco100 = valor // 100
        valor -= troco100 * 100
        print('cédulas de 100: {}'.format(troco100))
        if not valor:
            break
    if (valor >= 50):
        troco50 = valor // 50
        valor -= troco50 * 50
        print('cédulas de 50: {}'.format(troco50))
        if not valor:
            break
    if (valor >= 20):
        troco20 = valor // 20
        valor -= troco20 * 20
        print('cédulas de 20: {}'.format(troco20))
        if not valor:
            break
    if (valor >= 10):
        troco10 = valor // 10
        valor -= troco10 * 10
        print('cédulas de 10: {}'.format(troco10))
        if not valor:
            break
    if (valor >= 5):
        troco5 = valor // 5
        valor -= troco5 * 5
        print('cédulas de 5: {}'.format(troco5))
        if not valor:
            break
    if (valor >= 1):
        troco1 = valor // 1
        valor -= troco1 * 1
        print('cédulas de 1: {}'.format(troco1))
        break