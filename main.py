import csv
from datetime import datetime


class Tabela():

  def __init__(self):
    #Escolha uma das opções abaixo (nome fixo ou escolher o nome do arquivo), e comente a outra.

    #self.file = 'pesquisa_covid.csv'
    self.file = (input('Digite o nome do arquivo (sem extensão) em que deseja escrever as respostas.') + '.csv')

    self.lista_respostas = []
    


  def escrevendo_linhas(self):
    """Abrindo o arquivo CSV e escrevendo através de um loop"""

    with open(self.file, 'w', newline='') as csvfile:

        while len(self.lista_respostas) < 10:
          
          dd = Dados()
          dd.setAll()
          

          self.lista_respostas.append(dd.todas_respostas_do_participante())
          

          escrevendo = csv.writer(csvfile, delimiter=',')
          escrevendo.writerow(dd.todas_respostas_do_participante())

    csvfile.close()



class Dados():

  PERGUNTAS = ['Você já contraiu Covid-19?: ', 'Caso tenha contraído Covid-19, apresentou alguma sequela? ',
              'Você tomou a vacina? ', 'Se tiver se vacinado, completou o esquema vacinal? ']
  OPCOES = "\n1 - SIM\n2 - NÃO\n3 - NÃO SEI\n"
  RESPOSTASPOSSIVEIS = ["1", "2", "3"]
  GENEROS = ['M', 'F', 'NB']


  def __init__(self):
    self.idade = int(input('Digite a Idade do participante: '))



  @property
  def idade(self):
    return self._idade

  @idade.setter
  def idade(self, value):
      '''Verifica e atribui valor à idade.'''
      while (value < 14) or (value > 130):
          if value == 00:
            print(
                'Idade 00 digitada. Agradecemos pela participação. Pesquisa finalizada.')
            exit()

          print('Idade inválida para a pesquisa. Verifique o número digitado e a idade do participante. ')
          value = int(input('Insira a idade do entrevistado: '))

      self._idade = value


  @property
  def genero(self):
    return self._genero
  
  @genero.setter
  def genero(self, gen):
    '''Verifica e seta o gênero do participante'''
    while gen not in self.GENEROS:
      gen = input('\nOpção inválida.\nDigite uma das opções (M - F - NB): \n>> ').upper()

    self._genero = gen



  @property
  def respostas(self):
    return self._respostas

  @respostas.setter
  def respostas(self, ignorar): #Ignorar existe aqui para poder realizar a atribuição de respostas no método setAll e ele identificar a operação como um setter.
    '''Faz as perguntas ao usuário, verifica a entrada para cada pergunta, e retorna uma lista com suas respostas.'''

    respostas_individuo = []

    for i in range(len(self.PERGUNTAS)):
      resposta_temporaria = input(self.PERGUNTAS[i] + self.OPCOES)

      while resposta_temporaria not in self.RESPOSTASPOSSIVEIS:
        print("\nResposta inválida\n")
        resposta_temporaria = input(self.PERGUNTAS[i] + self.OPCOES)

      respostas_individuo.append(resposta_temporaria)
    
    self._respostas = ','.join(respostas_individuo)



  def setAll(self):
    '''Seta todos os elementos de UMA pessoa (Instância de Dados)'''

    self.genero = input('Digite o gênero do entrevistado (M - F - NB): ').upper()

    self.respostas = None

    self._datahora = datetime.today().strftime('%d-%m-%y %H:%M')



  def todas_respostas_do_participante(self):
    '''retorna todos os elementos de um participante da pesquisa'''

    return self._idade, self._genero, self._respostas, self._datahora



Tabela().escrevendo_linhas()