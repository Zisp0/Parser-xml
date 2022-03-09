import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
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

def mostrar(obj, item, treeView):

    item2 = treeView.insert(item, tk.END, text=obj.getNombre())
    
    item3 = treeView.insert(item2, tk.END, text="Nombre científico")
    treeView.insert(item3, tk.END, text=obj.getNombreCientifico())
    
    item4 = treeView.insert(item2, tk.END, text="Velocidad máxima")
    treeView.insert(item4, tk.END, text=obj.getvelocidadMaxima())
    
    item5 = treeView.insert(item2, tk.END, text="Periodo de gestación")
    treeView.insert(item5, tk.END, text=obj.getperiodoGestacion())

def limpiarArbol(treeView):
    for item in treeView.get_children():
        treeView.delete(item)

def verXml(dirXml):
    
    try:
        root = ET.parse(dirXml).getroot()
    except:
        messagebox.showerror(message="Archivo no compatible, por favor ingrese un archivo XML.", title="Error")
    
    animales = []
    for animal in root:
        nombre = animal.tag
        nombreCientifico = animal.find('nombreCientifico').text
        velocidad = animal.find('velocidad').text
        periodoDeGestacion = animal.find('periodoDeGestacion').text
        tipo = animal.find('tipo').text

        if tipo == "Terrestre":
            animales.append(animalTerrestre(
                nombre, nombreCientifico, velocidad, periodoDeGestacion))
        elif tipo == "Aereo":
            animales.append(animalAereo(
                nombre, nombreCientifico, velocidad, periodoDeGestacion))
        elif tipo == "Acuático":
            animales.append(animalAcuatico(
                nombre, nombreCientifico, velocidad, periodoDeGestacion))
        else:
            messagebox.showerror(message="XML no compatible, ingrese 'Animales.xml'", title="Error")
            return 

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

    raiz = treeView.insert("", tk.END, text=root.tag, open = True)
    terItem = treeView.insert(raiz, tk.END, text="Terrestres", open = True)
    aerItem = treeView.insert(raiz, tk.END, text="Aereos", open = True)
    acuItem = treeView.insert(raiz, tk.END, text="Acuáticos", open = True)

    for ter in terrestres:
        mostrar(ter, terItem, treeView)

    for aer in aereos:
        mostrar(aer, aerItem, treeView)

    for acu in acuaticos:
        mostrar(acu, acuItem, treeView)

def buscarArchivo():
    filename = filedialog.askopenfilename(initialdir="/", title="Selecciona el  archivo XML", filetypes=(("Text files", "*.xml*"), ("all files", "*.*")))

    if filename != "":
        limpiarArbol(treeView)     
        verXml(filename)
        labelArchivo.configure(text="Archivo abierto desde: " + filename, fg="blue")    
    else:
        labelArchivo.configure(text="Por favor seleccione un archivo XML", fg="red")


window = tk.Tk()
window.title('XmlParser')
window.geometry("700x500+0+0")
frmContainer = ttk.Frame(window)

labelArchivo = tk.Label(frmContainer, text="Por favor, busque el archivo xml", fg="blue")
labelArchivo.pack(pady = 20)

treeView = ttk.Treeview(frmContainer, padding = '10 10 12 10', selectmode= 'browse')

btnBuscar = tk.Button(frmContainer, text="Buscar archivo", command=buscarArchivo, fg = "White", bg = "Green")
btnBuscar.pack(pady = 10)
frmContainer.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)
treeView.pack(fill = tk.X)
vsb = ttk.Scrollbar(treeView, orient="vertical", command=treeView.yview)
vsb.place(relx=0.96, rely=0.175, relheight=0.713, relwidth=0.035)


window.mainloop()
