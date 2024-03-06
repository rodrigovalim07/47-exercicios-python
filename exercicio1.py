preco = float(input('qual o valor do produto?: '))
p = float(input('qual percentual de desconto a ser aplicado?: '))
desconto = preco * (p/100)
final = preco - desconto

print('o preço do produto é de {}, o desconto sera de {}%.'.format(preco, p))
print('valor de desconto: {}. valor final do produto: {}.'.format(desconto, final))