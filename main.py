
import wx
 
import body
 
class CalcFrame(body.MyFrame1):
    def __init__(self,parent):
        body.MyFrame1.__init__(self,parent)
    

 
app = wx.App(False)
 
frame = CalcFrame(None)
 
frame.Show(True)
 
app.MainLoop()