#-------------------------------------------------------------------------------
# Name:        Interfaz_10_wxBoxSizer
# Purpose:     Uso del ridemsionador wxBoxSizer, que nos habilita para poner varios
#       componentes dentro de una fila o una columna
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
        super(Example, self).__init__(parent, title=title, size=(260, 180))
        self.InitUI()
        self.Centre()               # Centra la ventana creada
        self.Show()                 # Muestra el objeto en pantalla

    def InitUI(self):
        panel = wx.Panel(self) # Panel redimensionable
        panel.SetBackgroundColour('#4f5049')
        vbox = wx.BoxSizer(wx.VERTICAL) # Orientacion Vertical
        midPan = wx.Panel(panel)
        midPan.SetBackgroundColour('#ededed')

        # Se colocan algunos espacios alrededor del panel
        # Se tiene colocado un borde de 20 px alrededor de midPan. wxAll
        # Aplica el tama?o del borde a todos los cuatro lados

        # wx.EXPAND : Nuestro componente ocupa todo el espacio que se le habia
        # asignado.
        # Se puede definir la alineacion de los componentes con:
        # wx.ALIGN_LEFT
        # wx.ALIGN_RIGHT
        # wx.ALIGN_TOP
        # wx.ALIGN_BOTTOM
        # wx.ALIGN_CENTER_VERTICAL
        # wx.ALIGN_CENTER_HORIZONTAL
        # wx.ALIGN_CENTER

        vbox.Add(midPan, 1, wx.EXPAND | wx.ALL, 20)
        panel.SetSizer(vbox)

if __name__ == '__main__':
    app = wx.App()          # Se crea el objeto de aplicacion
    Example(None, title='') # Nombre de la Ventana
    app.MainLoop()          # Bucle Infinito

