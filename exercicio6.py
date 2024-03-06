n1 = float(input('qual sua nota em matematica?(0 a 10): '))
n2 = float(input('qual sua nota em quimica?: '))
n3 = float(input('qual sua nota em fisica?: '))
if (n1 >= 7 and n2 >= 7 and n3 >= 7):
    print('voce passou de ano. parabens')
else:
    print('voce foi reprovado')