valor = float(input('qual o valor da compra? '))
print('"1" para pagamento a vista')
print('"3" para parcelar em 3x')
print('"5" para parcelar em 5x')
print('"10" para parcelar em 10x')
pg = input('qual a forma de pagamento? ')
if (pg == '1'):
    valor = valor * 0.95
    print('valor total da compra ${}. obrigado'.format(valor))
elif (pg == '3'):
    par = valor / 3
    print('valor total da compra ${}, parcelas de ${}. obrigado'.format(valor, par))
elif (pg == '5'):
    valor = valor * 1.02
    par = valor / 5
    print('valor total da compra ${}, parcelas de ${}. obrigado'.format(valor, par))
elif (pg == '10'):
    valor = valor * 1.08
    par = valor / 10
    print('valor total da compra ${}, parcelas de ${}. obrigado'.format(valor, par))
else:
    print('operação inválida')