# Name:        Interfaz_4_Centrar
# Purpose:  Mostrar una ventana Grafica Centrada, con acho y Alto especificos
#           Ancho=300, Alto =200
#
# Author:     Wilmer Planchez (Mentor Anonymous)
#
# Created:     17/08/2012
# Copyright:   (c) Mentor Anonymous 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import wx
class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title,
            size=(300, 200))
        self.Centre()               # Centra la ventana creada
        self.Show()                 # Muestra el objeto en pantalla
if __name__ == '__main__':          # Funcion Principal
    app = wx.App()                  # Se crea el objeto de aplicacion
    Example(None, title='Center')   # Nombre de la Ventana
    app.MainLoop()                  # Bucle Infinito


