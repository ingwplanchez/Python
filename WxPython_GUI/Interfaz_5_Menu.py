#------------------------------------------------------------------------------
# Name:        Interfaz_5_Menu
# Purpose:  Mostrar una peque?a ventana con menu simple
#
# Author:     Wilmer Planchez (Mentor Anonymous)
#
# Created:     17/08/2012
# Copyright:   (c) Mentor Anonymous 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import wx
class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):

        menubar = wx.MenuBar()  # Barra de menu funcional
        fileMenu = wx.Menu()    # Creacion de un objeto Barra de Menu

        # Creacion de un objeto menu
        # fitem = fileMenu.Append(1?,2?,3?)
        # 1? Parametro Item del menu (wx.ID_EXIT)
        # 2? Parametro Nombre del Item de menu ('Quit')
        # 3? Parametro Cadena que se muestra cuando se seleciona el menu
        # ('Salir de la aplicaci?n')

        fitem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Salir de la aplicaci?n')

        menubar.Append(fileMenu, '&File')   # Creacion implicita de wx.MenuItem
                                            # Con Append()
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.OnQuit, fitem)  # Metodo que cerrara las
                                                    # Aplicaciones

        self.SetSize((300, 200))        # Tama?o de Ventana
        self.SetTitle('Menu simple')    # Titulo de ventana
        self.Centre()                   # Mostrar  Centrada
        self.Show(True)                 # Mostrar ventana

    def OnQuit(self, e):    # Definicion de la funcion OnQuit
        self.Close()        # Cerrar

if __name__ == '__main__':
    ex = wx.App()           # Se crea el objeto de aplicacion
    Example(None)
    ex.MainLoop()           # Bucle infinito

