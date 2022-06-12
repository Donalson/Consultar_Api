#Importacion de flask para crear y ejecutar sitio web, renderizar plantillas, numpy para generar numeros aleatorios
# y flask_cors para utilizar datos externos
from distutils.log import debug
from pickle import TRUE
from flask import Flask, render_template
from numpy import random
import requests
from flask_cors import CORS

#Instanciacion de flask dentro de la variable app
app = Flask(__name__)
CORS(app)

#Creacion de la ruta principal del sitio web y texto de prueba
@app.route('/')
def Inicio():
    #Se crea una lista para guardar los 6 identificadores de los pokemons
    verificador = []
    #Se añade un valor inicial a la lista
    verificador.append(random.randint(252,386))

    #Se crea un bucle para asegurar de que hay 6 elementos en lista y que sean diferente
    while len(verificador) < 6:
        aleatorio = random.randint(252,386)
        rango = len(verificador)
        sirve = True
        for index in range(0,rango):
            if aleatorio == verificador[index]:
                sirve = False
        if sirve == True:
            verificador.append(aleatorio)
            
    pokemons = []
    for i in range(0,6):
        url = 'https://pokeapi.co/api/v2/pokemon/'+str(verificador[i])
        temp = requests.get(url)
        temp = temp.json()
        pokemons.append({'ID':verificador[i],'Nombre':temp['name'],'Alt':temp['height'],'Peso':temp['weight'],'Tipos':temp['types']})
    
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
    
    return render_template('index.html', lista = pokemons, tipos = tipos)

#Inializacion del sitio web para correr(modo debug encendido para detectar cambios)
if __name__ == '__main__':
    app.run(debug=True)