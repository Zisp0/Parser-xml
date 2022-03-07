import xml.etree.ElementTree as ET

class animal():
    def __init__(self, nombre, nombreCientifico, velocidadMaxima, periodoGestacion):
        self.nombre = nombre
        self.nombreCientifico = nombreCientifico
        self.velocidadMaxima = velocidadMaxima
        self.periodoGestacion = periodoGestacion

    def getNombre(self):
        return self.nombre
    
    def getNombreCientifico(self):
        return self.nombreCientifico

    def getvelocidadMaxima(self):
        return self.velocidadMaxima

    def getperiodoGestacion(self):
        return self.periodoGestacion

class animalTerrestre(animal):
    def getTipo(self):
        return("Terrestre")

class animalAereo(animal):
    def getTipo(self):
        return("Aereo")

class animalAcuatico(animal):
    def getTipo(self):
        return("Acuatico")

dos = ".   .   "
tres = ".   .   .   "
four = ".   .   .   .   "
def mostrar(obj):
    print(dos + obj.getNombre())
    print(tres + "Nombre científico")
    print(four + obj.getNombreCientifico())
    print(tres + "Velocidad máxima")
    print(four + obj.getvelocidadMaxima())
    print(tres + "Periodo de gestación")
    print(four + obj.getperiodoGestacion())

import xml.etree.ElementTree as ET
root = ET.parse('animales.xml').getroot()

animales = []

for animal in root:
    nombre = animal.tag
    nombreCientifico = animal.find('nombreCientifico').text
    velocidad = animal.find('velocidad').text
    periodoDeGestacion = animal.find('periodoDeGestacion').text
    tipo = animal.find('tipo').text

    if tipo == "Terrestre":
        animales.append(animalTerrestre(nombre, nombreCientifico, velocidad, periodoDeGestacion))
    elif tipo == "Aereo":
        animales.append(animalAereo(nombre, nombreCientifico, velocidad, periodoDeGestacion))
    elif tipo == "Acuático":
        animales.append(animalAcuatico(nombre, nombreCientifico, velocidad, periodoDeGestacion))
    else:
        print("Tipo erroneo")

terrestres = []
aereos = []
acuaticos = []

for animal in animales:
    tipo = animal.getTipo()
    if tipo == "Terrestre":
        terrestres.append(animal)
    elif tipo == "Aereo":
        aereos.append(animal)
    else:
        acuaticos.append(animal)

print (root.tag)
print (".   Terrestres")
for ter in terrestres:
    mostrar(ter)

print (".   Aereos")
for aer in aereos:
    mostrar(aer)

print (".   Acuáticos")
for acu in acuaticos:
    mostrar(acu)
