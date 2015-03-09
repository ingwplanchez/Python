#------------------------------------------------------------------------------
# Name:        Interfaz_0_Ventana
# Purpose:  Mostrar una ventana grafica usando WxPython
#
# Author:      Wilmer Planchez (Mentor Anonymous)
#
# Created:     11/08/2012
# Copyright:   (c) Mentor Anonymous 2012
# Licence:     <your licence>
#------------------------------------------------------------------------------

import wx                   # Esta linea importa el modulo wxPython Basico
app=wx.App()                # Se crea el objeto de aplicacion
frame = wx.Frame(None,-1, 'simple.py')  # Objeto Aplicacion
frame.Show()                # Se muestra el objeto en pantalla
app.MainLoop()              # Bucle sin fin


