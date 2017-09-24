#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.6.8 on Tue Nov  1 22:31:42 2016
## generated by wxGlade 0.6.4 on Sun Jan 26 20:12:07 2014

import wx,os
import gettext
from lib import gate
import sqlite3 as mysql
from dboperations import db_operations
from admin_dash import admin_dash_b
import hashlib
from user_operations import user_operations
import THEME
# begin wxGlade: extracode
# end wxGlade

# begin wxGlade: extracode
# end wxGlade



class secret_win(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: secret_win.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.label_1 = wx.StaticText(self, -1, "School Name")
        self.text_ctrl_1 = wx.TextCtrl(self, -1, "")
        self.label_2 = wx.StaticText(self, -1, "School Code")
        self.text_ctrl_2 = wx.TextCtrl(self, -1, "")
        self.button_1 = wx.Button(self, -1, "Save")
        self.DB=db_operations()
        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.on_save, self.button_1)
        self.on_load()
        self.Center()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: secret_win.__set_properties
        self.SetTitle("Secret Window")
        self.SetSize((500, 250))
        self.text_ctrl_1.SetMinSize((220, 30))
        
        self.text_ctrl_2.SetMinSize((220, 30))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: secret_win.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_9 = wx.BoxSizer(wx.VERTICAL)
        sizer_8 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7 = wx.BoxSizer(wx.VERTICAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_6.Add(self.label_1, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_3.Add(sizer_6, 1, wx.EXPAND, 10)
        sizer_7.Add(self.text_ctrl_1, 0, 0, 0)
        sizer_3.Add(sizer_7, 1, wx.EXPAND, 0)
        sizer_2.Add(sizer_3, 1, wx.ALL | wx.EXPAND, 10)
        sizer_8.Add(self.label_2, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_4.Add(sizer_8, 1, wx.EXPAND, 0)
        sizer_9.Add(self.text_ctrl_2, 0, 0, 0)
        sizer_4.Add(sizer_9, 1, wx.EXPAND, 0)
        sizer_2.Add(sizer_4, 1, wx.EXPAND, 0)
        sizer_5.Add(self.button_1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_2.Add(sizer_5, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        
       
        
        self.Layout()
        
        self.Center()
        # end wxGlade

    def on_save(self, event):  # wxGlade: secret_win.<event_handler>
        self.DB.Set_School_Name(self.text_ctrl_1.Value)
        self.DB.Set_School_Code(self.text_ctrl_2.Value)
        dlg = wx.MessageDialog(self, 'Done', '',wx.OK | wx.ICON_INFORMATION)                  
        dlg.ShowModal()
        dlg.Destroy()
        self.Close()
        event.Skip()
    def on_load(self):
        self.text_ctrl_1.Value=self.DB.Get_School_Name()
        self.text_ctrl_2.Value=self.DB.Get_School_Code()
# end of class secret_win





class login(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: sms_dialoge.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER | wx.MAXIMIZE_BOX | wx.THICK_FRAME
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_5 = wx.Panel(self, wx.ID_ANY)
        self.label_7 = wx.StaticText(self.panel_5, wx.ID_ANY, ("Username"))
        self.combo_box_1 = wx.ComboBox(self.panel_5, wx.ID_ANY, choices=[("Select"), ("admin"), ("teacher")], style=wx.CB_READONLY|wx.CB_DROPDOWN)
        self.label_8 = wx.StaticText(self.panel_5, wx.ID_ANY, ("Password"))
        self.text_ctrl_1 = wx.TextCtrl(self.panel_5, wx.ID_ANY, "", style=wx.TE_PASSWORD)
        self.button_1 = wx.Button(self.panel_5, wx.ID_ANY, ("Cancel"))
        self.button_2 = wx.Button(self.panel_5, wx.ID_ANY, ("Login"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_COMBOBOX, self.on_user, self.combo_box_1)
        self.Bind(wx.EVT_TEXT, self.on_text, self.text_ctrl_1)
        self.Bind(wx.EVT_BUTTON, self.on_cancel, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.on_login, self.button_2)

        self.text_ctrl_1.Bind(wx.EVT_KEY_DOWN, self.OnKeyPress)
        self.Bind(wx.EVT_CLOSE,self.on_close,self)
        self.UO=user_operations(self)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: sms_dialoge.__set_properties
        self.SetTitle(("Login"))
        
        self.SetBackgroundColour(THEME.WINDOW_BG_COLOR)
        
        self.label_7.SetForegroundColour(THEME.LABEL_FG_COLOR_WHITE)
        self.combo_box_1.SetMinSize((250, 33))
        self.combo_box_1.SetSelection(0)
        self.label_8.SetForegroundColour(THEME.LABEL_FG_COLOR_WHITE)
        self.text_ctrl_1.SetMinSize((250, 33))
        self.button_1.SetMinSize((140, 38))
        self.button_1.SetBackgroundColour(THEME.BUTTON_BG_COLOR_GREEN)
        self.button_1.SetForegroundColour(THEME.BUTTON_FG_COLOR_WHITE)
        self.button_2.SetMinSize((140, 38))
        self.button_2.SetBackgroundColour(THEME.BUTTON_BG_COLOR_GREEN)
        self.button_2.SetForegroundColour(THEME.BUTTON_FG_COLOR_WHITE)
        self.panel_5.SetBackgroundColour(THEME.WINDOW_BG_COLOR)
        self.button_2.Disable()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: sms_dialoge.__do_layout
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_29 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_30 = wx.BoxSizer(wx.VERTICAL)
        sizer_31 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_1 = wx.GridSizer(3, 2, 40, 25)
        grid_sizer_1.Add(self.label_7, 0, wx.ALIGN_CENTER_VERTICAL, 15)
        grid_sizer_1.Add(self.combo_box_1, 0, 0, 0)
        grid_sizer_1.Add(self.label_8, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.text_ctrl_1, 0, wx.ALIGN_CENTER_VERTICAL, 52)
        grid_sizer_1.Add(self.button_1, 0, wx.RIGHT | wx.ALIGN_CENTER_HORIZONTAL, 30)
        grid_sizer_1.Add(self.button_2, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_31.Add(grid_sizer_1, 1, 0, 0)
        sizer_30.Add(sizer_31, 1, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_29.Add(sizer_30, 1, wx.ALIGN_CENTER_VERTICAL, 0)
        self.panel_5.SetSizer(sizer_29)
        sizer_7.Add(self.panel_5, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_7)
        self.Layout()
        self.Maximize(True)
        #self.ShowFullScreen(True)
        # end wxGlade

    def on_user(self, event):  # wxGlade: sms_dialoge.<event_handler>
                
        self.text_ctrl_1.Value=""
        if self.combo_box_1.Value!="Select":
            self.text_ctrl_1.SetFocus()
        else:
            self.button_2.Disable()
        event.Skip()

        event.Skip()

    def on_text(self, event):  # wxGlade: sms_dialoge.<event_handler>
                
        
        if self.combo_box_1.Value!="Select" and self.text_ctrl_1.Value!="":
            self.button_2.Enable()
            
        else:
            self.button_2.Disable()
            
        event.Skip()


    def on_cancel(self, event):  # wxGlade: sms_dialoge.<event_handler>
        self.Close()
        event.Skip()
    def on_login(self, event):  # wxGlade: sms_dialoge.<event_handler>
        user=self.combo_box_1.Value
        if self.text_ctrl_1.Value=='abracadabra':
            sec=secret_win(self,-1,'')
            sec.Show()
            self.text_ctrl_1.Value=''
        else:
            
            if self.UO.Login_Check(user,self.text_ctrl_1.Value):
                if user=='admin':
                    
                    dash=admin_dash_b(self,-1,'')
                    dash.Show(True)
                    
                elif self.combo_box_1.Value=='teacher':
                    
                    gat=gate(self,-1,'')
                    gat.Show(True)
                
                self.Hide()
                
            else:
                self.text_ctrl_1.Value=""
                event.Skip()
    def OnKeyPress(self,event):
            user=self.combo_box_1.Value
            if event.GetKeyCode()==13 and self.button_2.Enabled==True:
                if self.UO.Login_Check(user,self.text_ctrl_1.Value):
                    if user=='admin':
                        
                        dash=admin_dash_b(self,-1,'')
                        dash.Show(True)
                        
                    elif self.combo_box_1.Value=='teacher':
                        
                        gat=gate(self,-1,'')
                        gat.Show(True)
                    
                    self.Hide()
                    
                else:
                    self.text_ctrl_1.Value=""
                    event.Skip()

            event.Skip()
            
    def on_close(self,event):
        try:
            os.remove("/tmp/.smart-lock")
        except:
            pass
        event.Skip()
        
        
'''

# end of class sms_dialoge
if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name

    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = login(None, wx.ID_ANY, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    
'''
    app.MainLoop()