def validaint(pergunta, min, max):
    x = int(input(pergunta))
    while (x < min) or (x > max):
        x = int(input(pergunta))
    return x


def fatorial(num):
    """
    calcula a fatorial
    :param num: numero para tirar a fatorial
    :return: retorna o valor
    """
    fat = 1
    if num == 0:
        return fat
    for i in range(num, 0, -1):
        fat *= i    # fat = fat * i
    return fat


x = validaint('digite um valor para tirar o fatorial: ', 0, 10)
print(f'{x}! = {fatorial(x)}')
