import os
from datetime import datetime
import csv

class Questionário:

    """ def __init__(self, idade, genero):
        self.idade = idade
        self.genero = genero """

    def perguntas(self, idade, genero, pergunta1, pergunta2, pergunta3, pergunta4,datahora):
                self.idade = idade
                self.genero = genero
                self.pergunta1 = pergunta1
                self.pergunta2 = pergunta2
                self.pergunta3 = pergunta3
                self.pergunta4 = pergunta4
                self.datahora = datahora

lista_entrevistados = []
for i in range(3):
    idade = input("informe sua idade: ")
    genero = input("informe seu genero: ")
    pergunta1 = input('Você já contraiu covid?')
    pergunta2 = input('Caso tenha contraído. Teve alguma sequela?')
    pergunta3 = input('Você tomou a vacina?')
    pergunta4 = input('Se tiver tomado, completou o esquema vacinal?')
    datahora = datetime.today()
    os.system("cls")
    temp = Questionário()
    temp.perguntas(idade, genero, pergunta1, pergunta2, pergunta3, pergunta4,datahora)
    lista_entrevistados.append(temp)
    
print(lista_entrevistados)


with open ('respostas_covid.csv', 'w', newline = '') as arq:
    my_writer = csv.writer(arq, delimiter = ' ')
    my_writer.writerow(lista_entrevistados)

