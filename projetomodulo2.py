import csv

informacoes_pesquisa= dict ()
idade = ''
condicao = True
while condicao :
        print('Bem vindo(a) a pesquisa sobre Covid19. Primeiro gostaríamos de cadastrar algumas informações. ')
        idade = (input('Digite a sua idade: '))


        if idade == '00':
            condicao = False


        if condicao == True:
            genero= input('Digite seu gênero: ')

            print("Agradecemos pelas informações. ")
            print('Pedimos que responda as perguntas apenas com: 1 (sim) , 2 (não) , 3 (não sei responder): ')
            primeira_pergunta = input('Você já contraiu Covid19?: ')
            segunda_pergunta = input('Caso tenha contraído Covid19, apresentou alguma sequela? ')
            terceira_pergunta = input('Você tomou a vacina? ')
            quarta_pergunta = input('Se tiver se vacinado. Completou o esquema vacinal?')
            lista = [idade, genero,primeira_pergunta,segunda_pergunta,terceira_pergunta,quarta_pergunta]
            informacoes_pesquisa=[lista]
            print(informacoes_pesquisa)
            with open ('pppesquisacovid19.csv', 'a', newline = '') as csvfile:
                my_writer = csv.writer(csvfile, delimiter = ',')
                my_writer.writerow(informacoes_pesquisa)



        else:
            print('Idade 00 digitada. Agradecemos pela participação. Pesquisa finalizada. ')




    #linhas = 0
    # for coluna in range(10):
    #     if linhas ==0:
    #         print(coluna)
    #         linhas = linhas +1
        






