# JavaScript Object Notation
# Ele e estruturado por chaves e valores (dicionario)

#Json e usado para troca de informacoes entre sistemas beckends
# e o formato utilizado pelas APIs
# Graphql as APIs REST

# capturar uma informação da internet ##

import urllib.request
import json 

url = 'http://api.open-notify.org/astros.json'

## capturar essas informações em dados JSON

pega_json = urllib.request.urlopen(url).read().decode()

#converter esses valores em dicionarios para manipulação

dic_json = json.loads(pega_json)

# Iterar os valores do dicionario

for c in dic_json.values():
    print(c)

print(dic_json)

for p in dic_json['people']:
    print(p['name'])

#cria um arquivo json com os valores extraidos

with open('arquivos/nomes.json','w+') as f:
    json.dump(dic_json,f,indent=4)

