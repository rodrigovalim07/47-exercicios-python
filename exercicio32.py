while True:
    idade = int(input('qual sua idade? '))
    if idade < 0:
        break
    sexo = input('sexo: "m" masculino e "f" para feminino -> ')
    if sexo == 'm':
        print('boa noite, senhor, sua idade é {} anos.'.format(idade))
    elif sexo == 'f':
        print('boa noite, senhora, sua idade é {} anos.'.format(idade))