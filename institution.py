#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.6.8 on Sat Sep 16 15:37:30 2017
#

import wx

# begin wxGlade: dependencies
import gettext
import THEME
from dboperations import db_operations
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class institution(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: institution.__init__
        kwds["style"] = wx.CAPTION | wx.RESIZE_BORDER |wx.MINIMIZE_BOX| wx.CLOSE_BOX | wx.MAXIMIZE_BOX | wx.THICK_FRAME|wx.CAPTION | wx.MAXIMIZE| wx.MINIMIZE_BOX
        wx.Dialog.__init__(self, *args, **kwds)
        self.label_1 = wx.StaticText(self, wx.ID_ANY, ("Institution Details"))
        self.label_2 = wx.StaticText(self, wx.ID_ANY, ("School Name"))
        self.text_ctrl_name = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_3 = wx.StaticText(self, wx.ID_ANY, ("School Code"))
        self.text_ctrl_code = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_4 = wx.StaticText(self, wx.ID_ANY, ("Email"))
        self.text_ctrl_email = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_5 = wx.StaticText(self, wx.ID_ANY, ("Phone"))
        self.text_ctrl_phone = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_6 = wx.StaticText(self, wx.ID_ANY, ("DEO"))
        self.text_ctrl_deo = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_cancel = wx.Button(self, wx.ID_ANY, ("Cancel"))
        self.button_save = wx.Button(self, wx.ID_ANY, ("Save"))


        self.DB=db_operations()
        self.__set_properties()
        self.__do_layout()
        self.on_load()

        self.Bind(wx.EVT_BUTTON, self.on_cancel, self.button_cancel)
        self.Bind(wx.EVT_BUTTON, self.on_save, self.button_save)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: institution.__set_properties
        self.SetBackgroundColour(THEME.WINDOW_BG_COLOR)
        self.SetTitle(("Institution Settings"))
        self.SetSize((665, 628))
        self.text_ctrl_name.SetMinSize((300, 30))
        self.text_ctrl_code.SetMinSize((300, 30))
        self.text_ctrl_email.SetMinSize((300, 30))
        self.text_ctrl_phone.SetMinSize((300, 30))
        self.text_ctrl_deo.SetMinSize((300, 30))
        self.button_cancel.SetMinSize((95, 33))
        self.button_save.SetMinSize((95, 33))
        
        self.label_1.SetFont(THEME.FONT_H1)
        self.label_2.SetFont(THEME.FONT_H3)
        self.label_3.SetFont(THEME.FONT_H3)
        self.label_4.SetFont(THEME.FONT_H3)
        self.label_5.SetFont(THEME.FONT_H3)
        self.label_6.SetFont(THEME.FONT_H3)
        
        self.button_cancel.SetForegroundColour(THEME.BUTTON_FG_COLOR_WHITE)
        self.button_cancel.SetBackgroundColour(THEME.BUTTON_BG_COLOR_GREEN)
        self.button_save.SetForegroundColour(THEME.BUTTON_FG_COLOR_WHITE)
        self.button_save.SetBackgroundColour(THEME.BUTTON_BG_COLOR_GREEN)
        
        
        self.label_1.SetForegroundColour(THEME.LABEL_FG_COLOR_WHITE)
        self.label_2.SetForegroundColour(THEME.LABEL_FG_COLOR_WHITE)
        self.label_3.SetForegroundColour(THEME.LABEL_FG_COLOR_WHITE)
        self.label_4.SetForegroundColour(THEME.LABEL_FG_COLOR_WHITE)
        self.label_5.SetForegroundColour(THEME.LABEL_FG_COLOR_WHITE)
        self.label_6.SetForegroundColour(THEME.LABEL_FG_COLOR_WHITE)
      
        
        
           
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: institution.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.GridSizer(5, 2, 0, 0)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_5.Add(self.label_1, 0, 0, 0)
        sizer_4.Add(sizer_5, 1, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_3.Add(sizer_4, 1, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_1.Add(self.label_2, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_name, 0, 0, 0)
        grid_sizer_1.Add(self.label_3, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_code, 0, 0, 0)
        grid_sizer_1.Add(self.label_4, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_email, 0, 0, 0)
        grid_sizer_1.Add(self.label_5, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_phone, 0, 0, 0)
        grid_sizer_1.Add(self.label_6, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_deo, 0, 0, 0)
        sizer_3.Add(grid_sizer_1, 1, wx.BOTTOM | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 50)
        sizer_7.Add(self.button_cancel, 0, wx.ALIGN_RIGHT, 0)
        sizer_6.Add(sizer_7, 1, wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 50)
        sizer_8.Add(self.button_save, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_6.Add(sizer_8, 1, wx.LEFT | wx.EXPAND, 50)
        sizer_3.Add(sizer_6, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_2.Add(sizer_3, 1, wx.ALL | wx.EXPAND, 40)
        sizer_1.Add(sizer_2, 30, wx.ALL | wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def on_cancel(self, event):  # wxGlade: institution.<event_handler>
        self.Close(True)
        event.Skip()

    def on_save(self, event):  # wxGlade: institution.<event_handler>
        try:
            self.DB.Set_School_Name(self.text_ctrl_name.Value) 
            self.DB.Set_School_Code(self.text_ctrl_code.Value)   

            self.DB.Set_School_Email(self.text_ctrl_email.Value)       
            self.DB.Set_School_Contact(self.text_ctrl_phone.Value)
            self.DB.Set_School_DEO(self.text_ctrl_deo.Value)
            #print "valuses",self.text_ctrl_name.Value,self.text_ctrl_code.Value,self.text_ctrl_email.Value,self.text_ctrl_phone.Value,self.text_ctrl_deo.Value
            dlg = wx.MessageDialog(self, 'Successfully Saved', '',wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
        except:
            dlg = wx.MessageDialog(self, 'Could not save some values', '',wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
                
              
            
        
        self.Close(True)
        event.Skip()
    def on_load(self):
        
        school=self.DB.Get_School_Name()
        self.text_ctrl_name.Value=school
        code=self.DB.Get_School_Code()
        self.text_ctrl_code.Value=code
        email=self.DB.Get_School_Email()
        deo=self.DB.Get_School_DEO()
        contact=self.DB.Get_School_Contact()
        
        self.text_ctrl_email.Value=email
        self.text_ctrl_phone.Value=contact
        self.text_ctrl_deo.Value=deo
# end of class institution
if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name

    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    institution = institution(None, wx.ID_ANY, "")
    app.SetTopWindow(institution)
    institution.ShowModal()
    institution.Destroy()
    app.MainLoop()