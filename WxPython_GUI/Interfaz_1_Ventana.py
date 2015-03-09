#------------------------------------------------------------------------------
# Name:        Interfaz_1_Ventana
# Purpose:  Mostrar una ventana grafica usando WxPython
#
# Author:      Wilmer Planchez (Mentor Anonymous)
#
# Created:     11/08/2012
# Copyright:   (c) Mentor Anonymous 2012
# Licence:     <your licence>
#------------------------------------------------------------------------------

import wx           # Esta linea importa el modulo wxPython B?sico
app = wx.App()      # Se crea el objeto de aplicaci?n
window = wx.Frame(None, style=wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER
| wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)   # Parametros de la ventana

# wx.MINIMIZE_BOX : Minimizacion de ventana
# wx.MAXIMIZE_BOX : Maximizacion de ventana
# wx.CLOSE_BOX: Cerrar Ventana
# wx.RESIZE_BORDER : Agrandar / Restaurar ventana
# wx.SYSTEM_MENU : Men? de ventana
# wx.CAPTION: Etiqueta

window.Show(True)   # Mostrar objeto
app.MainLoop()      # Bucle infinito


