from datetime import datetime
import csv


class Dados():
  listaDeRespostas = []


  def __init__(self):
    self.loop = self.enquanto()


  def enquanto(self):
    with open ('pesquisacovid19.csv', 'w', newline = '') as csvfile:

      while len(self.listaDeRespostas) < 10:
        self.setIdade()
        self.setGenero()
        self.setRespostas()
        self.setHora()

        respostaParaEscrever = [self.idade, self.genero,
        self.primeira_resposta, self.segunda_resposta,
        self.terceira_resposta, self.quarta_resposta,
        self.datahora]

        self.listaDeRespostas.append(respostaParaEscrever)

        escrevendo = csv.writer(csvfile, delimiter = ',')
        escrevendo.writerow(respostaParaEscrever)
      
    csvfile.close()


  def setHora(self):
    self.datahora = datetime.today().strftime('%y-%m-%d %H:%M')


  def setRespostas(self):
    primeira_resposta = int(input('Você já contraiu Covid-19?: '))
    self.primeira_resposta = self.verificaRespostas(primeira_resposta)

    segunda_resposta = int(input('Caso tenha contraído Covid-19, apresentou alguma sequela? '))
    self.segunda_resposta = self.verificaRespostas(segunda_resposta)

    terceira_resposta = int(input('Você tomou a vacina? '))
    self.terceira_resposta = self.verificaRespostas(terceira_resposta)

    quarta_resposta = int(input('Se tiver se vacinado, completou o esquema vacinal?'))
    self.quarta_resposta = self.verificaRespostas(quarta_resposta)
    
  
  def verificaRespostas(self, respostaQQ):
    while (respostaQQ < 1) or (respostaQQ > 3):
      print('Digite uma resposta válida, entre 1 e 3')
      respostaQQ = int(input('>> '))

    return respostaQQ


  def setGenero(self):
    gen = ['M','F','NB']
    genero = input('Digite o gênero do entrevistado (M - F - NB): ').upper()

    while genero not in gen:
      genero = input('\nOpção inválida.\nDigite uma das opções (M - F - NB): ').upper()

    self.genero = genero


  def setIdade(self):
    idade = int(input('Insira a idade do entrevistado: '))

    while (idade < 9) or (idade > 130):
      if idade == 00:
       print('Idade 00 digitada. Agradecemos pela participação. Pesquisa finalizada.')
       exit()

      print('Idade inválida para a pesquisa. Verifique o número digitado e a idade do participante. ')
      idade = int(input('Insira a idade do entrevistado: '))

    self.idade = idade
      


    
    


dd = Dados()







#  def verificaIdade(self):


#Coisas que faltam: 
# 1. acabar o codigo (Portar o código da Mari p/ objeto)
# 2. fazer o slide
# 3. fazer o fluxograma
# 4. fazer o readme.md para o github
# 5. dividir falas e partes