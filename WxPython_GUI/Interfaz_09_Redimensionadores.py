#-------------------------------------------------------------------------------
# Name:       Interfaz_09_Redimensionadores
# Purpose:    Crear una ventana con un area de texto que se redimensiona con
#        la ventana.
#
# Author:      Anonymous
#
# Created:     27/05/2013
# Copyright:   (c) Anonymous 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import wx
class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title,
            size=(260, 180)) # Tama?o de la ventana
        self.InitUI()
        self.Centre()               # Centra la ventana creada
        self.Show()                 # Muestra el objeto en pantalla

    def InitUI(self): # Metodo Constructor
        menubar = wx.MenuBar()
        filem = wx.Menu()
        editm = wx.Menu()
        helpm = wx.Menu()
        menubar.Append(filem, '&File')  # Se agregra el elemento File
        menubar.Append(editm, '&Edit')  # Se agregra el elemento Edit
        menubar.Append(helpm, '&Help')  # Se agregra el elemento Help
        self.SetMenuBar(menubar)
        wx.TextCtrl(self)

if __name__ == '__main__':
    app = wx.App()          # Se crea el objeto de aplicacion
    Example(None, title='') # Nombre de la Ventana
    app.MainLoop()          # Bucle Infinito
