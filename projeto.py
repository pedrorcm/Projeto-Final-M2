import csv
import copy


class Dados():
  #PERGUNTAS = ('Você já contraiu covid?', 'Caso tenha contraído. Teve alguma sequela?', 'Você tomou a vacina?', 'Se tiver tomado, completou o esquema vacinal?')
  lista_pessoas = []

  def setRespostas(self, pergunta1, pergunta2, pergunta3, pergunta4):
    self.resposta1 = pergunta1
    self.resposta2 = pergunta2
    self.resposta3 = pergunta3
    self.resposta4 = pergunta4
  

  def setGenero(self):
    genero = input('Insira o gênero do entrevistado: ')
    self.genero = genero

  def setIdade(self,idade):
  #  idade = int
    self.idade = idade

  def getRespostas(self):
    return [self.resposta1, self.resposta2, self.resposta3, self.resposta4]
  
  def enquanto(self):
    # idade = int(input(''))
    # while idade != 00:
    # receber uma idade, verificar se é 00.
    # sair ou continuar
    # self.setRespostas








    while len(self.lista_pessoas) <10:
      idd = int(input('insira a idade do entrevistado'))

      while (idd < 9) or (idd > 120):
        print('Idade inválida')
        idd = int(input('não é possível realizar a pesquisa com a faixa etária inserida.\nInsira uma idade válida:'))

      if idd == 00:
        break

      self.setResposta()

      varTemporaria = Dados(idd)
      self.lista_pessoas.append(copy.deepcopy(varTemporaria))

d1 = Dados()

    
'''  def validando_resposta(self, resposta):
    while True:
      try:
        break
    
      except ValueError:
        pass
    
    return resposta'''
      
'''    if (resposta < 1 or resposta > 3):
      print('resposta invalida')
      return False
    return True'''

'''
print(
Responda às seguintes perguntas com as opções:
1 para SIM
2 para NÃO
3 para NÃO SEI RESPONDER
)
'''
'''
with open('arquivo.csv', 'w') as arq:
  arq.writelines(f'issoESoUmTeste')
'''

  # aprender como pula a linha, quebra de linha
  # e fazer um loop de repetição aqui

