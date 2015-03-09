#-------------------------------------------------------------------------------
# Name:     Interfaz_08_PosicionamientoAbs
# Purpose:  Crear una ventana con un area de texto usando posicionamiento
#        Absoluto( No se redimensiona)
#
# Author:      Wilmer Planchez (Mentor Anonymous)
#
# Created:     27/05/2013
# Copyright:   (c) Anonymous 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import wx
class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title,
            size=(260, 180))
        self.InitUI()
        self.Centre()               # Centra la ventana creada
        self.Show()                 # Muestra el objeto en pantalla

    def InitUI(self):
        panel = wx.Panel(self, -1) # Se crea un panel dentro de la ventana
        menubar = wx.MenuBar()  # Barra de menu funcional
        filem = wx.Menu()       # Creacion de un Objeto Barra de menu
        editm = wx.Menu()       # "     "       "       "       "
        helpm = wx.Menu()       # "     "       "       "       "
        menubar.Append(filem, '&File')  # Se agregra el elemento File
        menubar.Append(editm, '&Edit')  # Se agregra el elemento Edit
        menubar.Append(helpm, '&Help')  # Se agregra el elemento Help
        self.SetMenuBar(menubar)

        # Se Agrega un Area de Texto
        # Largo = 250 Ancho = 150
        wx.TextCtrl(panel, pos=(3, 3), size=(250, 150))

if __name__ == '__main__':
    app = wx.App()          # Se crea el objeto de aplicacion
    Example(None, title='') # Nombre de la Ventana
    app.MainLoop()          # Bucle Infinito
