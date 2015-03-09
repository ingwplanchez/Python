#-------------------------------------------------------------------------------
# Name:     Program_50_AgendaGUI
# Purpose:  Desarrollo de una interfaz grafica
#
# Author:      Wilmer Planchez (Mentor Anonymous)
#
# Created:     09/05/2013
#-------------------------------------------------------------------------------


from tkinter import * # Importacion de la libreria grafica
import Modulos

def Listar():
    Agenda = open("agendatelefonica.csv")
    Numero = 0
    for i in range(1,30):
        Lectura = Agenda.readline()
        Lista.insert(END,Lectura.replace(",","  "))
        Numero = Numero + 1
    Agenda.close()
        
f = Frame(height=300,width=300) # Largo = 300, Ancho = 300
f.pack(padx=15,pady=15) # Margen interior

logoimg= PhotoImage(file = "Mentor2.gif")   # Se indica el archivo de imagen a mostrar   
EtiquetaLogo = Label(f,image = logoimg)     # Se agrega la imagen
EtiquetaLogo.pack(side=TOP,padx=10,pady=10) # Se indica la posicion

Titulo = Label(f,text="Agenda Telefonica",fg="blue",font=("Arial",24))  # Se crea un label, f indica que pertenece
                                                                        # Al frame f creado.
                                                                        # fg ="blue" Indica le color del texto
                                                                        # font = ("Arial",24) tipo de letra y tamaño
                                                               
Titulo.pack(side=TOP,padx=10,pady=10)      # Posicion de la etiqueta

Autor = Label(f,text="Wilmer Planchez")        
Autor.pack(side=TOP,padx=10,pady=10)

Campo =Entry(f,textvariable = 5)
Campo.pack(side=TOP,padx=10,pady=10)

## Boton = Button(f,text = "Listar elementos de la agenda",command = lambda:Modulos.Consulta(int(Entry.get(Campo))))
Boton = Button(f,text = "Listar elementos de la agenda",command = Listar)    # Label del boton
Boton.pack(side=BOTTOM,padx=10,pady=10)                     #POsicion del boton  

# Lambdas: sirven para poder llamar a funciones dentro de
# una funcion superior y pasarle parametros
# Entry.get() : Obtiene los elementos de un campo de texto (Campo)

Lista = Listbox(f)
Lista.pack(side=TOP,padx=10,pady=10)
