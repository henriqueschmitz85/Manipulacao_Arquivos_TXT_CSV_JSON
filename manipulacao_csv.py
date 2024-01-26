import csv

#criar um arquivo csv com as funcoes writer e writerow

with open('arquivos/nome.csv','w+',newline="",encoding='utf-8') as fcsv:
    escreve = csv.writer(fcsv,delimiter=',')
    escreve.writerow(('Nome',"Sobrenome","Idade"))
    escreve.writerow(('Joao',"Ricardo","39"))
    escreve.writerow(('Juca',"Franciso","40"))
    escreve.writerow(('Francisco',"Juca","41"))


with open('arquivos/nome.csv','r') as fcsv2:
    ler = csv.reader(fcsv2)
    lista1 = list(ler)
    print(lista1)

    for c in lista1:
        print(c)

## transformar a saida em dicionario com o metodo dictreader

with open('arquivos/nome.csv','r') as fcsv3:
    ler_dic = csv.DictReader(fcsv3)

    #iterar os valores

    for d in ler_dic:
        print(d["Nome"])