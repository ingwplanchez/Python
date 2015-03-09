#------------------------------------------------------------------------------
# Name:        Interfaz_2_Tam_Pos
# Purpose:  Mostrar una ventana Grafica, con acho y Alto especificos
#           Ancho=250, Alto =200
#
# Author:     Wilmer Planchez (Mentor Anonymous)
#
# Created:     17/08/2012
# Copyright:   (c) Mentor Anonymous 2012
# Licence:     <your licence>
#------------------------------------------------------------------------------

import wx
class Example(wx.Frame):
    # En este ejemplo la aplicacion, podra ser del tama?o 250x200 px.
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title,
            size=(250, 200))    # Tama?o de la Ventana
        self.Show()             # Muestra el objeto en pantalla
if __name__ == '__main__':      # Funcion principal
    app = wx.App()              # Se crea el objeto de aplicacion
    Example(None, title='Size') # Titulo de la ventana
    app.MainLoop()              # Bucle infinito

