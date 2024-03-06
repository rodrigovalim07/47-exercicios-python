# COMO CRIAR UM "HELP", UMA DOCSTRING
def soma(x=0, y=0, z=0):
    """
    função que soma até três valores inteiros
    :param x: valor inteiro opcional
    :param y: valor inteiro opcional
    :param z: valor inteiro opcional
    :return: a soma inteira
    """
    return x+y+z


print(soma(1, 2, 3))
help(soma)
