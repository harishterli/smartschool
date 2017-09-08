#!/usr/bin/env python
import wx,os
import gettext
from login import login


if __name__ == "__main__":
    
    path="/tmp/.smart-lock"
    
    
    if not os.path.exists(path):
        
        open(path,'w')
        app = wx.PySimpleApp(0)
        wx.InitAllImageHandlers()
        frame_1 = login(None, -1, "")
        app.SetTopWindow(frame_1)
        frame_1.Show()
        app.MainLoop()
        
        
       
    else:
        
        
        app = wx.PySimpleApp(0)
       
        dlg = wx.MessageDialog(None, 'Another instance of E-asy Exam Already Running.', '',wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
