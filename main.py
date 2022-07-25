from datetime import datetime
import csv


class Tabela():
  
  def __init__(self):
    self.file = 'pesquisacovid.csv'
    self.listaDeRespostas = []

  #Abrindo o arquivo CSV e escrevendo através de um loop
  def loop(self):

    with open (self.file, 'w', newline = '') as csvfile:

      while len(self.listaDeRespostas) < 10:
        dd = Dados()
        dd.genero = input('Digite o gênero do entrevistado (M - F - NB): ').upper()
        dd.respostas = None

        self.listaDeRespostas.append(dd.respostaCompleta)

        escrevendo = csv.writer(csvfile, delimiter = ',')
        escrevendo.writerow(dd.respostaCompleta)

    csvfile.close()


class Dados():

  def __init__(self):
    self.idade = int(input('Digite a Idade do participante: '))
    self._datahora = datetime.today().strftime('%y-%m-%d %H:%M')


  #Retorna todas as respostas do objeto, para serem escritas no csv
  @property
  def respostaCompleta(self):
    return [self._idade, self._genero,
        self._primeira_resposta, self._segunda_resposta,
        self._terceira_resposta, self._quarta_resposta,
        self._datahora, self.respostas]
  

  #Getter e Setter da Idade

  @property
  def idade(self):
    return self._idade

  @idade.setter
  def idade(self, idd):
   
    while (idd < 9) or (idd > 130):
      if idd == 00:
       print('Idade 00 digitada. Agradecemos pela participação. Pesquisa finalizada.')
       exit()

      print('Idade inválida para a pesquisa. Verifique o número digitado e a idade do participante. ')
      idd = int(input('Insira a idade do entrevistado: '))

    self._idade = idd
  

  #Getter e setter das Respostas

  @property
  def respostas(self):
    return self._primeira_resposta, self._segunda_resposta, self._terceira_resposta, self._quarta_resposta

  @respostas.setter
  def respostas(self, ignorar):
    primeira_resposta = int(input('Você já contraiu Covid-19?: '))
    self._primeira_resposta = self.verificaRespostas(primeira_resposta)

    segunda_resposta = int(input('Caso tenha contraído Covid-19, apresentou alguma sequela? '))
    self._segunda_resposta = self.verificaRespostas(segunda_resposta)

    terceira_resposta = int(input('Você tomou a vacina? '))
    self._terceira_resposta = self.verificaRespostas(terceira_resposta)

    quarta_resposta = int(input('Se tiver se vacinado, completou o esquema vacinal?'))
    self._quarta_resposta = self.verificaRespostas(quarta_resposta)

  #Verifica se as respostas inseridas estão no intervalo entre 1 e 3.

  def verificaRespostas(self, respostaQuestao):
    while (respostaQuestao < 1) or (respostaQuestao > 3):
      print('Digite uma resposta válida, entre 1 e 3')
      respostaQuestao = int(input('>> '))

    return respostaQuestao

  #Getter e setter do gênero. A verificação ocorre dentro do setter.

  @property
  def genero(self):
    return self._genero

  @genero.setter
  def genero(self, genero):
    gen = ['M','F','NB']

    while genero not in gen:
      genero = input('\nOpção inválida.\nDigite uma das opções (M - F - NB): ').upper()

    self._genero = genero


escrever = Tabela()
escrever.loop()