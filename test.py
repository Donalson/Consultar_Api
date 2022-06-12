from numpy import random
import requests 

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
tipos = {
    'normal':'https://media.vandal.net/m/6-2021/20216312412377_11.jpg',
    'fighting':'https://media.vandal.net/m/6-2021/20216312412377_10.jpg',
    'flying':'https://media.vandal.net/m/6-2021/20216312412377_18.jpg',
    'poison':'https://media.vandal.net/m/6-2021/20216312412377_17.jpg',
    'ground':'https://media.vandal.net/m/6-2021/20216312412377_16.jpg',
    'rock':'https://media.vandal.net/m/6-2021/20216312412377_14.jpg',
    'bug':'https://media.vandal.net/m/6-2021/20216312412377_3.jpg',
    'ghost':'https://media.vandal.net/m/6-2021/20216312412377_6.jpg',
    'steel':'https://media.vandal.net/m/6-2021/20216312412377_1.jpg',
    'fire':'https://media.vandal.net/m/6-2021/20216312412377_7.jpg',
    'water':'https://media.vandal.net/m/6-2021/20216312412377_2.jpg',
    'grass':'https://media.vandal.net/m/6-2021/20216312412377_12.jpg',
    'electric':'https://media.vandal.net/m/6-2021/20216312412377_5.jpg',
    'psychic':'https://media.vandal.net/m/6-2021/20216312412377_13.jpg',
    'ice':'https://media.vandal.net/m/6-2021/20216312412377_9.jpg',
    'dragon':'https://media.vandal.net/m/6-2021/20216312412377_4.jpg',
    'dark':'https://media.vandal.net/m/6-2021/20216312412377_15.jpg',
    'fairy':'https://media.vandal.net/m/6-2021/20216312412377_8.jpg'
}
for i in range(0,6):
    url = 'https://pokeapi.co/api/v2/pokemon/'+str(verificador[i])
    temp = requests.get(url)
    temp = temp.json()
    pokemons.append({'ID':verificador[i],'Nombre':temp['name'],'Alt':temp['height'],'Peso':temp['weight'],'Tipos':temp['types']})

#print(pokemons[0]['Tipos'][0]['type']['name'])
for t in pokemons[0]['Tipos']:
    print(t['type']['name'])
print(tipos['poison'])

#print('name' in pokemons[0])
#print(pokemons[0]['name'])