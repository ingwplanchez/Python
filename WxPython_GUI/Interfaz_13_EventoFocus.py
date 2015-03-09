#-------------------------------------------------------------------------------
# Name:        Interfaz_13_EventoFocus
# Purpose:  Muestra el comportamiento del evento Focus
#
# Author:      Anonymous
#
# Created:     30/05/2013
# Copyright:   (c) Anonymous 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import wx
class MyWindow(wx.Panel):# Clase MyWindow
    def __init__(self, parent): # Creacion del metodo constructor
        wx.Panel.__init__(self, parent, -1) # Creacion de un pamel
        self.color = '#b3b3b3' # Color del panel

        # Aqui vinculamos el enlazador wx.EVT_PAINT al metodo OnPaint()
        self.Bind(wx.EVT_PAINT, self.OnPaint)

        # Bind(event, handler, source=None, id=wx.ID_ANY, id2=wx.ID_ANY)
        # event es uno de los objetos EVT_*. Este especifica el tipo del evento.

        # handler es un objeto para ser llamado. En otras palabras, esto es una m?todo, que Un
        #programador binds a un evento.

        #   Par?metro source es usado cuando buscamos diferenciar al mismo tipo de evento desde
        #diferentes componentes.

        # id par?metro es usado, cuando tenemos m?ltiples botones, items de men? etc. El id es usado
        #para diferenciar entre ellos.

        # id2 es usado cuando ?ste es deseable enlazar un manejador a un rango de ids, tales como
        #EVT_MENU_RANGE.

        # Aqui vinculamos el enlazador wx.EVT_SIZE al metodo OnSize()
        self.Bind(wx.EVT_SIZE, self.OnSize)

        # Aqui vinculamos el enlazador wx.EVT_SET_FOCUS al metodo OnSetFocus()
        # El evento wx.EVT_SET_FOCUS, el cual es generado cuando
        # un componente recibe el foco
        self.Bind(wx.EVT_SET_FOCUS, self.OnSetFocus)

        # Aqui vinculamos el enlazador wx.EVT_KILL_FOCUS al metodo OnKillFocus()
        # El wx.EVT_KILL_FOCUS es generado, cuando el componente pierde
        # el foco
        self.Bind(wx.EVT_KILL_FOCUS, self.OnKillFocus)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        dc.SetPen(wx.Pen(self.color))
        x, y = self.GetSize()
        dc.DrawRectangle(0, 0, x, y)

    def OnSize(self, event):
        self.Refresh()

    def OnSetFocus(self, event):
        self.color = '#0099f7'
        self.Refresh()

    def OnKillFocus(self, event):
        self.color = '#b3b3b3'
        self.Refresh()

class FocusEvent(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(350, 250))
        grid = wx.GridSizer(2, 2, 10, 10) # Creacion de celdas
        grid.AddMany([(MyWindow(self), 1, wx.EXPAND|wx.TOP|wx.LEFT,9),
            (MyWindow(self), 1, wx.EXPAND|wx.TOP|wx.RIGHT, 9),
            (MyWindow(self), 1, wx.EXPAND|wx.BOTTOM|wx.LEFT, 9),
            (MyWindow(self), 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT, 9)])

        self.SetSizer(grid)
        self.Centre()
        self.Show(True)

if __name__ == '__main__':
    app = wx.App()                      # Se crea el objeto de aplicacion
    FocusEvent(None, -1, 'focus event') # Nombre de la ventana
    app.MainLoop()                      # Bucle Infinito