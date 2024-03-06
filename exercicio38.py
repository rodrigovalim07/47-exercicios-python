def validar (pergunta, min, max):
    x = len(input(pergunta))
    while (x<min or x>max):
        x = len(input(pergunta))
    return x
x = validar('digite uma frase com 10 a 20 caracteres: ',10,20)
print('voce digitou uma frase de {} caracteres'.format(x))