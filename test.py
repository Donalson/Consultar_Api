from numpy import random
import requests 
""""
#Se crea una lista para guardar los 6 identificadores de los pokemons
verificador = []
#Se añade un valor inicial a la lista
verificador.append(random.randint(151))

#Se crea un bucle para asegurar de que hay 6 elementos en lista y que sean diferente
while len(verificador) < 6:
    aleatorio = random.randint(151)
    rango = len(verificador)
    sirve = True
    for index in range(0,rango):
        if aleatorio == verificador[index]:
            diferente = False
    if sirve:
        verificador.append(aleatorio)

pokemons = []
for i in range(0,6):
    url = 'https://pokeapi.co/api/v2/pokemon/'+str(verificador[i])
    temp = requests.get(url)
    temp = temp.json()
    pokemons.append({'ID':verificador[i],'Nombre':temp['name']})

print(pokemons[0]['Nombre'])

#print('name' in pokemons[0])
#print(pokemons[0]['name'])
"""

test = random.randint(252,386)
print(test)