# vamos abrir um arquivo TXT

arq1 = open('arquivos/arquivo.txt','r')

##ler o aquivo txt

print(arq1.read())

## voltar o cursor ao inicio

arq1.seek(0,0)

print(arq1.read())

arq1.close()

## usar um arquivo de modo gravacao

arq2 = open('arquivos/arquivo.txt','w+')

#gravar no arquivo

arq2.write("Tem novo conteudo\n")
arq2.write("Gravei outra linha\n")

arq2.seek(0,0)
print(arq2.read())

arq2.close()

# abrir uma nova manipulacao de alteracao de arquivo

arq3 = open('arquivos/arquivo.txt','a+')

arq3.write("Novo conteudo sem apagar o antigo\n")

arq3.seek(0,0)

print(arq3.read())

arq3.close()

## Gerenciador de contexto de arquivos

with open("arquivos/arquivo1.txt","w+") as f:
    f.write('Primeira linha\n')
    f.write('Segunda linha\n')
    f.seek(0,0)
    grava = str(f.read())
    f.seek(0,0)
    print(f.read())

#gravar informacoe em um 2 arquivo

with open('arquivos/arquivo2.txt','w+') as f2:
    f2.write(grava)
    f2.seek(0,0)
    print(f2.read())

