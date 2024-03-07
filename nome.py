def nome(): # criando a função
  nome = input('Qual seu primeiro nome? ')  # entrada de nome e sobrenome
  sobre = input('Qual seu sobrenome? ')
  ru = input('Qual o nº do seu RU? ')
  x = (nome[0:1] + sobre + ru[-2:] + '@algoritmos.com.br')  # concatenando a primeira letra do nome, sobrenome, ru e o email
  x = x.lower() # transformando o email em minúsculo caso a entrada do nome e sobrenome contenha letra maiúscula
  print(f'Sr {nome} {sobre}, seu email é {x}')  # por fim, escrevendo na tela a frase pedida no exercício, juntando as variáveis

# Programa principal
nome()  # invocando a função