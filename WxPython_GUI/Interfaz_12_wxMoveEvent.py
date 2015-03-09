#-------------------------------------------------------------------------------
# Name:        Interfaz_12_wxMoveEvent
# Purpose:  Interfaz en la cual se muestra un ejemplo de evento de movimiento
#
# Author:      Anonymous
#
# Created:     27/05/2013
# Copyright:   (c) Anonymous 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# self.Bind(wx.EVT_MOVE, self.OnMove)
# Aqu? vinculamos el enlazador wx.EVT_MOVE al m?todo OnMove().
# def OnMove(self, event):
# x, y = event.GetPosition()

import wx
class MoveEvent(wx.Frame):
    def __init__(self, parent, id, title): # Metodo Constructor
        wx.Frame.__init__(self, parent, id, title, size=(250, 180))
        wx.StaticText(self, -1, 'x:', (10,10)) # Objeto etiqueta
        wx.StaticText(self, -1, 'y:', (10,30)) # Objeto etiqueta
        self.st1 = wx.StaticText(self, -1, '', (30, 10)) # st1 sera una etiqueta
        self.st2 = wx.StaticText(self, -1, '', (30, 30)) # st2 sera una etiqueta

        # Aqu? vinculamos el enlazador wx.EVT_MOVE al m?todo OnMove()
        self.Bind(wx.EVT_MOVE, self.OnMove)
        self.Centre()               # Centra la ventana creada
        self.Show()                 # Muestra el objeto en pantalla

    def OnMove(self, event):
        x, y = event.GetPosition()  # Se obtiene la posicion
        self.st1.SetLabel(str(x))   # La etiqueta refleja muestra el valor de x
        self.st2.SetLabel(str(y))   # La etiqueta refleja muestra el valor de y

if __name__ == '__main__':
    app = wx.App()                      # Se crea el objeto de aplicacion
    MoveEvent(None, -1, 'move event')   # Nombre de la ventana
    app.MainLoop()                      # Bucle Infinito
