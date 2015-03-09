#-------------------------------------------------------------------------------
# Name:     Interfaz_14_CuadrosDeDialogo
# Purpose:  Cuadros de dialogo
#
# Created:     30/05/2013
# Copyright:   (c) Anonymous 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import wx
class MessageDialog(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)
        wx.FutureCall(1000, self.ShowMessage)
        self.Centre()
        self.Show(True)

    def ShowMessage(self):
        wx.MessageBox('Download completed', 'Info')

if __name__ == '__main__':
    app = wx.App()
    MessageDialog(None, -1, 'MessageDialog')
    app.MainLoop()
    wx.FutureCall(1000, self.ShowMessage)
