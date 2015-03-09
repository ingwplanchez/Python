#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# Name:        Interfaz_3_Tam_Pos_Move
# Purpose:  Mostrar una ventana Grafica, con Acho y Alto especificos, ademas de
# Mover la ventana a las coordenadas x,y especificas
#           Tama?o:         Ancho=250, Alto =
#           Coordenadas :   x = 350 , y = 200
#
# Author:     Wilmer Planchez (Mentor Anonymous)
#
# Created:     17/08/2012
# Copyright:   (c) Mentor Anonymous 2012
# Licence:     <your licence>
#------------------------------------------------------------------------------

import wx
class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title,
            size=(300, 200))    # Tama?o de la Ventana (size = (Ancho, Alto)
        self.Move((350, 200))   # Ubicacion de la Ventana
        self.Show()
if __name__ == '__main__':      # Funcion principal
    app = wx.App()              # Se crea el objeto de aplicacion
    Example(None, title='Move') # Titulo de la ventana
    app.MainLoop()              # Bucle infinito

