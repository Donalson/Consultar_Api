#Importacion de flask para crear y ejecutar sitio web, renderizar plantillas y numpy para generar numeros aleatorios
from flask import Flask, render_template
from numpy import random

#Instanciacion de flask dentro de la variable app
app = Flask(__name__)

#Se crea una lista para guardar los 6 identificadores de los pokemons
verificador = []
#Se añade un valor inicial a la lista
verificador.append(random.randint(155))

#Se crea un bucle para asegurar de que hay 6 elementos en lista y que sean diferente
while len(verificador) < 6:
    aleatorio = random.randint(155)
    rango = len(verificador)
    sirve = True
    for index in range(0,rango):
        if aleatorio == verificador[index]:
            diferente = False
    if sirve:
        verificador.append(aleatorio)

#Creacion de la ruta principal del sitio web y texto de prueba
@app.route('/')
def Inicio():
    return render_template('index.html')

#Inializacion del sitio web para correr(modo debug encendido para detectar cambios)
if __name__ == '__main__':
    app.run(debug=True)