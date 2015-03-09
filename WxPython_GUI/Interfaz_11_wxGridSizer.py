#-------------------------------------------------------------------------------
# Name:        Interfaz_11_wxGridSizer(No Corre)
# Purpose:     El wx.GridSizer establece los componentes en una tabla
# bidimensional. Cada celda dentro de la tabla tiene el mismo tama?o.
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
        super(Example, self).__init__(parent, title=title, size=(300, 250))
        self.InitUI()
        self.Centre()               # Centra la ventana creada
        self.Show()                 # Muestra el objeto en pantalla

    def InitUI(self):

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        vbox = wx.BoxSizer(wx.VERTICAL)
        self.display = wx.TextCtrl(self, style=wx.TE_RIGHT)
        vbox.Add(self.display, flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=4)
        gs = wx.GridSizer(4, 4, 5, 5)

        gs.AddMany( [(wx.button(self, label='Cls'), 0, wx.EXPAND),
            (wx.button(self, label='Bck'), 0, wx.EXPAND),
            (wx.StaticText(self), wx.EXPAND),
            (wx.button(self, label='Close'), 0, wx.EXPAND),
            (wx.button(self, label='7'), 0, wx.EXPAND),
            (wx.button(self, label='8'), 0, wx.EXPAND),
            (wx.button(self, label='9'), 0, wx.EXPAND),
            (wx.button(self, label='/'), 0, wx.EXPAND),
            (wx.button(self, label='4'), 0, wx.EXPAND),
            (wx.button(self, label='5'), 0, wx.EXPAND),
            (wx.button(self, label='6'), 0, wx.EXPAND),
            (wx.button(self, label='*'), 0, wx.EXPAND),
            (wx.button(self, label='1'), 0, wx.EXPAND),
            (wx.button(self, label='2'), 0, wx.EXPAND),
            (wx.button(self, label='3'), 0, wx.EXPAND),
            (wx.button(self, label='-'), 0, wx.EXPAND),
            (wx.button(self, label='0'), 0, wx.EXPAND),
            (wx.button(self, label='.'), 0, wx.EXPAND),
            (wx.button(self, label='='), 0, wx.EXPAND),
            (wx.button(self, label='+'), 0, wx.EXPAND) ])

        vbox.Add(gs, proportion=1, flag=wx.EXPAND)
        self.SetSizer(vbox)

if __name__ == '__main__':

    app = wx.App()                      # Se crea el objeto de aplicacion
    Example(None, title='Calculator')   # Nombre de la Ventana
    app.MainLoop()                      # Bucle Infinito
