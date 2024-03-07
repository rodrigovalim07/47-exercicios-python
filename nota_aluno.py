while True:
  sair = input('inserir dados?  1 -> sim     0 -> não: ') # pergunta se o usuário deseja iniciar o programa ou não
  if (sair == '0'): # se o usuário digitar 0 correspondente a não, o programa sera encerrado
    print('Encerrando...')
    break
  elif (sair != '1'): # caso o usuário digitar algo diferente de 1, o programa ira perguntar novamente até ele digitar 0 para encerrar ou 1 para prosseguir o programa
    continue
  # dados de entrada do aluno (nome e nota)
  aluno = input('Nome do aluno: ')
  nota = float(input('Nota final: '))
  if (nota >= 0 and nota <= 2.9):  # se a nota se enquadrar com a exigência contida no if ele recebe o conceito determinado pelo exercício
    conceito = 'E'
  elif (nota >= 3 and nota <= 4.9): # e assim como no primeiro if os demais elif seguem com a mesma premissa de nota dentro da exigência e recebendo o conceito de acordo com a nota
    conceito = 'D'
  elif (nota >= 5 and nota <= 6.9):
    conceito = 'C'
  elif (nota >= 7 and nota <= 8.9):
    conceito = 'B'
  elif (nota >= 9 and nota <= 10):
    conceito = 'A'
  else: # se a nota digitada não for de 0 a 10 o programa vai aparecer nota inválida e voltar ao inicio para perguntar o nome e a nota novamente
    print('Nota inválida')
    continue
  print('O aluno {} tirou a nota {} e se enquadra no conceito {}'.format(aluno, nota, conceito))  # no final do programa ira aparecer uma frase mostrando o nome, a nota e o conceito do aluno