#-------------------------------------------------------------------------------
# Name:        Interfaz_7_Submenues_Separadores
# Purpose:  Mostrar una barra de menu, con elementos , un separador, y
#           un submenu.
#
# Author:      James Marshall
#
# Created:     24/08/2012
# Copyright:   (c) James Marshall 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import wx
class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()
    def InitUI(self):
        menubar = wx.MenuBar()          # Barra de Menu
        fileMenu = wx.Menu()            # Creacion de un Objeto Barra de menu
        fileMenu.Append(wx.ID_NEW, '&New')      # Creacion del Item de menu New
        fileMenu.Append(wx.ID_OPEN, '&Open')    # Creacion del Item de menu Open
        fileMenu.Append(wx.ID_SAVE, '&Save')    # Creacion del Item de menu Save
        fileMenu.AppendSeparator()              # Se a?ade Un separador de menu
        imp = wx.Menu()                         # nuevo Menu (SubMenu)
        imp.Append(wx.ID_ANY, 'Import newsfeed list...')    # Item del Submenu
        imp.Append(wx.ID_ANY, 'Import bookmarks...')        # "     "       "
        imp.Append(wx.ID_ANY, 'Import mail...')             # "     "       "
        fileMenu.AppendMenu(wx.ID_ANY, 'I&mport', imp)  # Nombre del Submenu
        qmi = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+W') # Item salir
        fileMenu.AppendItem(qmi) # Se agrega el item al menu
        self.Bind(wx.EVT_MENU, self.OnQuit, qmi) # Metodo que cerrara las Ap.
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)
        self.SetSize((350, 250))    # Tama?o de la ventana
        self.SetTitle('Submenu')    # Titulo de la ventana
        self.Centre()               # Mostrar centrada
        self.Show(True)
    def OnQuit(self, e):
        self.Close()
def main():
    ex = wx.App()
    Example(None)
    ex.MainLoop()
if __name__ == '__main__':
    main()
