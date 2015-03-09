#------------------------------------------------------------------------------
# Name:        Interfaz_6_Menu_Atajo
# Purpose:  Mostrar una peque?a ventana con menu simple Con teclas de atajo
#
# Author:      Wilmer Planchez (Mentor Anonymous)
#
# Created:     24/08/2012
# Copyright:   (c) Mentor Anonymous 2012
# Licence:     <your licence>
#------------------------------------------------------------------------------

import wx
APP_EXIT = 1
class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()
    def InitUI(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        qmi = wx.MenuItem(fileMenu, APP_EXIT, '&Quit\tCtrl+Q') # Creacion de un
        # Item de menu de salida
        ##qmi.SetBitmap(wx.Bitmap('exit.png')) # Se elige un icono personalizado
        # Y un atajo para el item de menu

        fileMenu.AppendItem(qmi) # Creacion del Objeto wx.MenuItem
        self.Bind(wx.EVT_MENU, self.OnQuit, id=APP_EXIT) # Cuando se selecciona
        # El Item de menu creado, el Metodo OnQuit es llamado.
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)
        self.SetSize((250, 200))            # Tama?o de Ventana
        self.SetTitle('Icons y shortcuts')  # Titulo de Ventana
        self.Centre()                       # Mostrar Centrada
        self.Show(True)
    def OnQuit(self, e):                    # Definicion de la funcion OnQuit
        self.Close()
def main():                                 # Definicion de la funcion Main
    ex = wx.App()                           # Se Crea el objeto de aplicacion
    Example(None)
    ex.MainLoop()                           # Bucle infinito
if __name__ == '__main__':
    main()
