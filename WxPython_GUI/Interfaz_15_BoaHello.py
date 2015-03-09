#Boa:Frame:Frame1

import wx

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1BUTTON2, wxID_FRAME1PANEL1, 
 wxID_FRAME1STATICTEXT1, wxID_FRAME1TEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(6)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(405, 195), size=wx.Size(414, 220),
              style=wx.DEFAULT_FRAME_STYLE, title=u'HOLA MUNDO')
        self.SetClientSize(wx.Size(406, 193))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(406, 193),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Georgia'))
        self.panel1.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'HOLA MUNDO', name='staticText1', parent=self.panel1,
              pos=wx.Point(120, 136), size=wx.Size(168, 29), style=0)
        self.staticText1.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Georgia'))

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label=u'COLORIZADOR',
              name='button1', parent=self.panel1, pos=wx.Point(56, 88),
              size=wx.Size(128, 32), style=0)
        self.button1.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Georgia'))
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

        self.button2 = wx.Button(id=wxID_FRAME1BUTTON2, label=u'RESTAURAR',
              name='button2', parent=self.panel1, pos=wx.Point(232, 88),
              size=wx.Size(128, 32), style=0)
        self.button2.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Georgia'))
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_FRAME1BUTTON2)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self.panel1, pos=wx.Point(128, 40), size=wx.Size(144, 24),
              style=0, value=u'Escribe Aqui')
        self.textCtrl1.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Georgia'))

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        self.panel1.SetBackgroundColour('blue')
        self.Refresh()
        event.Skip()

    def OnButton2Button(self, event):
        self.panel1.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.Refresh()
        event.Skip()


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
