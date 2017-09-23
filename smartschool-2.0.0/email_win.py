#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.6.8 on Wed Nov 23 20:12:58 2016
#

import wx

# begin wxGlade: dependencies
import gettext
import THEME
from sms_win import CheckListCtrl
from dboperations import db_operations
from validations import validate
from email_library import  send_gmail
import sys,os
import wx.html as html
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


mypath = os.path.split(sys.argv[0])[0]



from HTMLParser import HTMLParser


class template_data_type(): 
    def __init__(self):
        self.name=''
        self.id=''
        self.data=''



class html_parser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        
        self.TEMPLATES=[]   #KEEPS WHOLE TABLE DATA OF THE WEBPAGE
        self.temp_data=template_data_type()
        self.templates_no=0
        self.current_template=0
        self.template_flag=False
        self.col_data=''
        
    def handle_starttag(self, tag, attrs):
        
            
        if tag=='template':
            
            self.template_flag=True
            self.temp_data.name=''
            self.temp_data.id=''
            self.temp_data.data=''
            
            for each in attrs:
                if each[0]=='name':
                    
                    self.temp_data.name=each[1]
                elif each[0]=='id':
                    self.temp_data.id=each[1]
            else:
                
                #adding tags manually since they are ignored in parsed data
                my_attrs=''
                for each in attrs:
                    my_attrs+=each[0]+'="'+each[1]+'"'
                my_tag="<"+tag.upper()+ " "+my_attrs+ " >"
                self.temp_data.data+=my_tag
        

    def handle_data(self, data):
        
        self.temp_data.data+=data
        '''
        if self.template_flag==True:
            self.temp_data.data=data
        '''
        
            
        #print data

    def handle_endtag(self, tag):
        if tag=="template":
            
            self.template_flag=False
            self.TEMPLATES.append(self.temp_data)
            print "name ",self.temp_data.name, "id ",self.temp_data.id,"data " ,self.temp_data.data
        
        self.temp_data.data+="</"+tag.upper()+">"
            
    def feed_html(self,html,first_page=False):
        
        
        self.feed(html)
   


class email_templates():
    
    
    def find_templates(self):
        temp_path=mypath+'/Resources/templates.xml'
        f=open(temp_path,'r+')
        text= f.read()
        parser=html_parser()
        parser.feed_html(text)
        self.TEMPLATES=parser.TEMPLATES
        '''for each in self.TEMPLATES:
            print each.name
            print each.id
            print each.data
        print self.TEMPLATES
        '''
        f.close()
        
        
    def load_templates(self):
        pass
        
    def delete_template(self,name):
        pass
    def save_template(self):
        pass
    def add_template(self):
        pass


class email_dialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: email_dialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER | wx.MAXIMIZE_BOX | wx.THICK_FRAME
        wx.Dialog.__init__(self, *args, **kwds)
        self.notebook_1 = wx.Notebook(self, wx.ID_ANY, style=wx.NB_LEFT)
        self.pane_send1 = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.combo_box_staff = wx.ComboBox(self.pane_send1, wx.ID_ANY, choices=[_("Select"), _("Staff"), _("Students")], style=wx.CB_DROPDOWN | wx.CB_DROPDOWN | wx.CB_READONLY | wx.CB_SORT)
        self.combo_box_year = wx.ComboBox(self.pane_send1, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN | wx.CB_READONLY)
        self.combo_box_class = wx.ComboBox(self.pane_send1, wx.ID_ANY, choices=["Select Standard","8","9","10"], style=wx.CB_DROPDOWN | wx.CB_READONLY)
        self.combo_box_div = wx.ComboBox(self.pane_send1, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN | wx.CB_READONLY)
        
        self.checklist_ctrl_1 = CheckListCtrl(self.pane_send1)
        
        self.button_add_email = wx.Button(self.pane_send1, wx.ID_ANY, _("Add Email"))
        self.text_ctrl_selected_email = wx.TextCtrl(self.pane_send1, wx.ID_ANY, "", style=wx.TE_READONLY|wx.TE_MULTILINE  | wx.TE_LINEWRAP)
        self.button_clear_all = wx.Button(self.pane_send1, wx.ID_ANY, _("Clear all"))
        self.button_close = wx.Button(self.pane_send1, wx.ID_ANY, _("Close"))
        self.button_next = wx.Button(self.pane_send1, wx.ID_ANY, _("Next ->>"))
        self.pane_send2 = wx.Panel(self.notebook_1, wx.ID_ANY, style=wx.SUNKEN_BORDER | wx.TAB_TRAVERSAL)
        self.label_id = wx.StaticText(self.pane_send2, wx.ID_ANY, _("Email"))
        self.combo_box_templates = wx.ComboBox(self.pane_send2, wx.ID_ANY, choices=[_("Select Templates")], style=wx.CB_DROPDOWN | wx.CB_DROPDOWN | wx.CB_READONLY)
        self.label_5 = wx.StaticText(self.pane_send2, wx.ID_ANY, _("Message body(plain Text or HTML)"))
        self.label_10 = wx.StaticText(self.pane_send2, wx.ID_ANY, _("Preview"))
        self.text_ctrl_msg = wx.TextCtrl(self.pane_send2, wx.ID_ANY, "", style=wx.TE_MULTILINE)
        self.html_preview_1 = html.HtmlWindow(self.pane_send2, wx.ID_ANY, size=(1, 1))#wx.TextCtrl(self.pane_send2, wx.ID_ANY, "")
        self.checkbox_1 = wx.CheckBox(self.pane_send2, wx.ID_ANY, _("Attach Performance Card"))
        self.text_ctrl_attachment = wx.TextCtrl(self.pane_send2, wx.ID_ANY, "")#, style=wx.TE_READONLY)
        self.button_attachment = wx.Button(self.pane_send2, wx.ID_ANY, _("Other Attchments"))
        self.label_4 = wx.StaticText(self.pane_send2, wx.ID_ANY, _("* In order to personalise message use tags <STUDENT>,<FATHER>,<SCHOOL> in capital letters which wil be replaced by actual names of student, parent and school."))
        self.button_back = wx.Button(self.pane_send2, wx.ID_ANY, _("<<- Back"))
        self.button_send = wx.Button(self.pane_send2, wx.ID_ANY, _("Send"))
        self.pane_templates = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.label_11 = wx.StaticText(self.pane_templates, wx.ID_ANY, _("Email Templates"))
        self.combo_box_templates_2 = wx.ComboBox(self.pane_templates, wx.ID_ANY, choices=[_("Select Templates")], style=wx.CB_DROPDOWN | wx.CB_DROPDOWN | wx.CB_READONLY)
        self.text_ctrl_msg_2 = wx.TextCtrl(self.pane_templates, wx.ID_ANY, "", style=wx.TE_MULTILINE)
        self.html_preview_2 = wx.TextCtrl(self.pane_templates, wx.ID_ANY, "")
        self.button_delete_temp = wx.Button(self.pane_templates, wx.ID_ANY, _("Delete"))
        self.button_add_temp = wx.Button(self.pane_templates, wx.ID_ANY, _("Save New"))
        self.button_save_temp = wx.Button(self.pane_templates, wx.ID_ANY, _("Save"))
        self.pane_report = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.panel_3 = wx.Panel(self.pane_report, wx.ID_ANY)
        self.label_6 = wx.StaticText(self.panel_3, wx.ID_ANY, _("Recent Emails"))
        self.text_ctrl_report = wx.TextCtrl(self.panel_3, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.pane_password = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.panel_5 = wx.Panel(self.pane_password, wx.ID_ANY)
        self.label_7 = wx.StaticText(self.panel_5, wx.ID_ANY, _("Institution Email"))
        self.text_ctrl_email = wx.TextCtrl(self.panel_5, wx.ID_ANY, "")
        self.label_8 = wx.StaticText(self.panel_5, wx.ID_ANY, _("Email Password"))
        self.text_ctrl_email_passwd = wx.TextCtrl(self.panel_5, wx.ID_ANY, "", style=wx.TE_PASSWORD)
        self.button_cancel = wx.Button(self.panel_5, wx.ID_ANY, _("Cancel"))
        self.button_save = wx.Button(self.panel_5, wx.ID_ANY, _("Save"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_COMBOBOX, self.on_combo_staff, self.combo_box_staff)
        self.Bind(wx.EVT_COMBOBOX, self.on_combo_year, self.combo_box_year)
        self.Bind(wx.EVT_COMBOBOX, self.on_combo_class, self.combo_box_class)
        self.Bind(wx.EVT_COMBOBOX, self.on_combo_div, self.combo_box_div)
        #self.Bind(wx.EVT_BUTTON, self.on_button_add_email, self.button_add_email)
        #self.Bind(wx.EVT_BUTTON, self.on_button_clear_all, self.button_clear_all)
        self.Bind(wx.EVT_BUTTON, self.on_button_close, self.button_close)
        self.Bind(wx.EVT_BUTTON, self.on_button_next, self.button_next)
        self.Bind(wx.EVT_COMBOBOX, self.on_combo_template_1, self.combo_box_templates)
        self.Bind(wx.EVT_CHECKBOX, self.on_checkbox, self.checkbox_1)
        self.Bind(wx.EVT_BUTTON, self.on_button_attachments, self.button_attachment)
        self.Bind(wx.EVT_BUTTON, self.on_button_back, self.button_back)
        self.Bind(wx.EVT_BUTTON, self.on_button_send, self.button_send)
        self.Bind(wx.EVT_COMBOBOX, self.on_combo_template_2, self.combo_box_templates_2)
        self.Bind(wx.EVT_BUTTON, self.on_button_delete_temp, self.button_delete_temp)
        self.Bind(wx.EVT_BUTTON, self.on_button_add_temp, self.button_add_temp)
        self.Bind(wx.EVT_BUTTON, self.on_button_save_temp, self.button_save_temp)
        self.Bind(wx.EVT_TEXT, self.on_email, self.text_ctrl_email)
        self.Bind(wx.EVT_TEXT, self.on_email_password, self.text_ctrl_email_passwd)
        self.Bind(wx.EVT_BUTTON, self.on_button_cancel, self.button_cancel)
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.on_page_change, self.notebook_1)
        # end wxGlade
        
        self.checklist_ctrl_1.OnCheckItem = self.on_check
        
        #self.Bind(wx.EVT_TEXT, self.on_sending_list_text, self.text_ctrl_selected_email)
        self.Bind(wx.EVT_TEXT,self.on_msg_text,self.text_ctrl_msg)
        self.Bind(wx.EVT_BUTTON,self.on_button_email_passwd,self.button_save)
        self.Bind(wx.EVT_BUTTON,self.on_button_cancel,self.button_cancel)
        #self.Bind(wx.EVT_BUTTON,self.on_button_cancel2,self.button_cancel2)
        
        #self.text_ctrl_selected_email.Bind(wx.EVT_KEY_DOWN, self.on_keydown_email)
        #self.text_ctrl_id.Bind(wx.EVT_KEY_UP, self.on_keydown_sms_id)
        
        self.DB=db_operations()
        self.V=validate()

    def __set_properties(self):
        # begin wxGlade: email_dialog.__set_properties
        self.SetTitle(_("Email"))
        self.SetSize((1262, 707))
        self.SetBackgroundColour(THEME.WINDOW_BG_COLOR)
        self.combo_box_staff.SetMinSize(THEME.COMBO_SIZE_NORMAL)
        self.combo_box_staff.SetBackgroundColour(wx.Colour(143, 188, 143))
        self.combo_box_staff.SetSelection(0)
        self.combo_box_year.SetMinSize(THEME.COMBO_SIZE_NORMAL)
        self.combo_box_class.SetMinSize(THEME.COMBO_SIZE_NORMAL)
        self.combo_box_div.SetMinSize(THEME.COMBO_SIZE_NORMAL)
        self.checklist_ctrl_1.SetMinSize((700,300))
        self.button_add_email.SetMinSize(THEME.BUTTON_SIZE_NORMAL)
        self.button_add_email.SetBackgroundColour(THEME.BUTTON_BG_COLOR)
        self.button_add_email.SetForegroundColour(THEME.BUTTON_FG_COLOR)
        
        self.button_delete_temp.SetMinSize(THEME.BUTTON_SIZE_NORMAL)
        self.button_delete_temp.SetBackgroundColour(THEME.BUTTON_BG_COLOR)
        self.button_delete_temp.SetForegroundColour(THEME.BUTTON_FG_COLOR)
        self.button_add_temp.SetMinSize(THEME.BUTTON_SIZE_NORMAL)
        self.button_add_temp.SetBackgroundColour(THEME.BUTTON_BG_COLOR)
        self.button_add_temp.SetForegroundColour(THEME.BUTTON_FG_COLOR)
        self.button_save_temp.SetMinSize(THEME.BUTTON_SIZE_NORMAL)
        self.button_save_temp.SetBackgroundColour(THEME.BUTTON_BG_COLOR)
        self.button_save_temp.SetForegroundColour(THEME.BUTTON_FG_COLOR)
        
        self.text_ctrl_selected_email.SetMinSize((700, 80))
        self.button_clear_all.SetMinSize(THEME.BUTTON_SIZE_NORMAL)
        self.button_clear_all.SetBackgroundColour(THEME.BUTTON_BG_COLOR)
        self.button_clear_all.SetForegroundColour(THEME.BUTTON_FG_COLOR)
        self.button_close.SetMinSize(THEME.BUTTON_SIZE_NORMAL)
        self.button_close.SetBackgroundColour(THEME.BUTTON_BG_COLOR)
        self.button_close.SetForegroundColour(THEME.BUTTON_FG_COLOR)
        self.button_next.SetMinSize(THEME.BUTTON_SIZE_NORMAL)
        self.button_next.SetBackgroundColour(THEME.BUTTON_BG_COLOR)
        self.button_next.SetForegroundColour(THEME.BUTTON_FG_COLOR)
        self.pane_send1.SetBackgroundColour(THEME.WINDOW_BG_COLOR)
        self.label_id.SetForegroundColour(THEME.LABEL_FG_COLOR)
        self.label_id.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.combo_box_templates.SetSelection(0)
        
        self.label_10.SetFont(THEME.FONT_H4)
        self.label_5.SetFont(THEME.FONT_H4)
        self.label_5.SetForegroundColour(THEME.LABEL_FG_COLOR)
        self.label_10.SetForegroundColour(THEME.LABEL_FG_COLOR)
        
        
        self.checkbox_1.SetValue(1)
        self.button_attachment.SetBackgroundColour(THEME.BUTTON_BG_COLOR)
        self.button_attachment.SetForegroundColour(THEME.BUTTON_FG_COLOR)
        self.button_attachment.SetMinSize(THEME.BUTTON_SIZE_NORMAL)
        self.text_ctrl_attachment.SetMinSize((270,40))
        self.label_4.SetForegroundColour(THEME.FG_COLOR_RED)
        self.button_back.SetMinSize(THEME.BUTTON_SIZE_NORMAL)
        self.button_back.SetBackgroundColour(THEME.BUTTON_BG_COLOR)
        self.button_back.SetForegroundColour(THEME.BUTTON_FG_COLOR)
        self.button_send.SetMinSize(THEME.BUTTON_SIZE_NORMAL)
        self.button_send.SetBackgroundColour(THEME.BUTTON_BG_COLOR)
        self.button_send.SetForegroundColour(THEME.BUTTON_FG_COLOR)
        self.pane_send2.SetBackgroundColour(THEME.WINDOW_BG_COLOR)
        self.pane_send2.Hide()
        self.label_11.SetForegroundColour(THEME.LABEL_FG_COLOR)
        self.label_11.SetFont(THEME.FONT_H1)
        self.combo_box_templates_2.SetSelection(0)
        self.pane_templates.SetBackgroundColour(THEME.WINDOW_BG_COLOR)
        self.label_6.SetForegroundColour(THEME.LABEL_FG_COLOR)
        self.label_6.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.text_ctrl_report.SetMinSize((750, 500))
        self.panel_3.SetBackgroundColour(THEME.WINDOW_BG_COLOR)
        self.label_7.SetForegroundColour(THEME.LABEL_FG_COLOR)
        self.text_ctrl_email.SetMinSize((250, 33))
        self.label_8.SetForegroundColour(THEME.LABEL_FG_COLOR)
        self.text_ctrl_email_passwd.SetMinSize((250, 33))
        self.button_cancel.SetMinSize(THEME.BUTTON_SIZE_NORMAL)
        self.button_cancel.SetBackgroundColour(THEME.BUTTON_BG_COLOR)
        self.button_cancel.SetForegroundColour(THEME.BUTTON_FG_COLOR)
        self.button_save.SetMinSize(THEME.BUTTON_SIZE_NORMAL)
        self.button_save.SetBackgroundColour(THEME.BUTTON_BG_COLOR)
        self.button_save.SetForegroundColour(THEME.BUTTON_FG_COLOR)
        self.panel_5.SetBackgroundColour(THEME.WINDOW_BG_COLOR)
        self.notebook_1.SetMinSize((400, 295))
        self.notebook_1.SetBackgroundColour(THEME.BUTTON_BG_COLOR)
        self.notebook_1.SetForegroundColour(THEME.WINDOW_FG_COLOR)
        #self.notebook_1.Hide()
        # end wxGlade
        
        self.checklist_ctrl_1.InsertColumn(0, 'Sl No', width=50)
        self.checklist_ctrl_1.InsertColumn(1, 'Name of Student', width=200)
        self.checklist_ctrl_1.InsertColumn(2, 'Name of Parent',width=200)
        self.checklist_ctrl_1.InsertColumn(3, 'Email',width=200)
        
        
        
        
        self.combo_box_class.Disable()
        self.combo_box_year.Disable()
        self.combo_box_div.Disable()
        self.button_add_email.Disable()
        self.button_next.Disable()
        self.button_clear_all.Disable()
        self.button_send.Disable()
        self.button_save.Disable()
        
        
        self.button_add_email.Hide()
        self.button_clear_all.Hide()
        self.text_ctrl_selected_email.Hide()
        

    def __do_layout(self):
        # begin wxGlade: email_dialog.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_29 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_30 = wx.BoxSizer(wx.VERTICAL)
        sizer_31 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_1 = wx.GridSizer(4, 2, 40, 25)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_14 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_4 = wx.GridSizer(1, 3, 0, 40)
        grid_sizer_8 = wx.GridSizer(1, 2, 0, 10)
        sizer_17 = wx.BoxSizer(wx.VERTICAL)
        sizer_15 = wx.BoxSizer(wx.VERTICAL)
        sizer_13 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_9 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_5 = wx.GridSizer(1, 3, 0, 0)
        grid_sizer_6 = wx.GridSizer(1, 2, 0, 20)
        grid_sizer_7 = wx.GridSizer(1, 2, 0, 0)
        sizer_11 = wx.BoxSizer(wx.VERTICAL)
        sizer_12 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_25 = wx.BoxSizer(wx.VERTICAL)
        sizer_37 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_3 = wx.GridSizer(1, 2, 10, 95)
        sizer_28 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_36 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_2 = wx.GridSizer(2, 2, 0, 0)
        grid_sizer_2.Add(self.combo_box_staff, 0, 0, 0)
        grid_sizer_2.Add(self.combo_box_year, 0, 0, 0)
        grid_sizer_2.Add(self.combo_box_class, 0, 0, 0)
        grid_sizer_2.Add(self.combo_box_div, 0, 0, 0)
        sizer_25.Add(grid_sizer_2, 1, wx.TOP | wx.EXPAND, 10)
        sizer_36.Add(self.checklist_ctrl_1, 1, 0, 0)
        sizer_36.Add(self.button_add_email, 0, wx.LEFT | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_25.Add(sizer_36, 3, 0, 0)
        sizer_28.Add(self.text_ctrl_selected_email, 0, 0, 0)
        sizer_28.Add(self.button_clear_all, 0, wx.LEFT | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_25.Add(sizer_28, 1, wx.EXPAND, 0)
        grid_sizer_3.Add(self.button_close, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_3.Add(self.button_next, 0, 0, 0)
        sizer_37.Add(grid_sizer_3, 1, wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_25.Add(sizer_37, 1, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_3.Add(sizer_25, 1, wx.ALL | wx.EXPAND, 10)
        self.pane_send1.SetSizer(sizer_3)
        sizer_12.Add(self.label_id, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_2.Add(sizer_12, 1, wx.EXPAND, 0)
        sizer_11.Add(self.combo_box_templates, 0, 0, 0)
        sizer_2.Add(sizer_11, 1, wx.EXPAND, 0)
        grid_sizer_7.Add(self.label_5, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_7.Add(self.label_10, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_2.Add(grid_sizer_7, 1, wx.EXPAND, 0)
        grid_sizer_6.Add(self.text_ctrl_msg, 0, wx.EXPAND, 0)
        grid_sizer_6.Add(self.html_preview_1, 0, wx.EXPAND, 0)
        sizer_2.Add(grid_sizer_6, 4, wx.EXPAND, 0)
        grid_sizer_5.Add(self.checkbox_1, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_5.Add(self.text_ctrl_attachment, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_5.Add(self.button_attachment, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_2.Add(grid_sizer_5, 1, wx.TOP | wx.BOTTOM | wx.EXPAND, 15)
        sizer_9.Add(self.label_4, 1, 0, 0)
        sizer_2.Add(sizer_9, 1, wx.EXPAND, 0)
        sizer_8.Add(self.button_back, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM, 30)
        sizer_8.Add(self.button_send, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM, 20)
        sizer_2.Add(sizer_8, 1, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_13.Add(sizer_2, 1, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 25)
        self.pane_send2.SetSizer(sizer_13)
        sizer_15.Add(self.label_11, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 30)
        sizer_14.Add(sizer_15, 1, wx.EXPAND, 0)
        sizer_17.Add(self.combo_box_templates_2, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_14.Add(sizer_17, 1, wx.EXPAND, 0)
        grid_sizer_8.Add(self.text_ctrl_msg_2, 0, wx.EXPAND, 0)
        grid_sizer_8.Add(self.html_preview_2, 0, wx.EXPAND, 0)
        sizer_14.Add(grid_sizer_8, 4, wx.ALL | wx.EXPAND, 20)
        grid_sizer_4.Add(self.button_delete_temp, 0, 0, 0)
        grid_sizer_4.Add(self.button_add_temp, 0, 0, 0)
        grid_sizer_4.Add(self.button_save_temp, 0, 0, 0)
        sizer_14.Add(grid_sizer_4, 2, wx.ALIGN_CENTER_HORIZONTAL, 0)
        self.pane_templates.SetSizer(sizer_14)
        sizer_6.Add(self.label_6, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_6.Add(self.text_ctrl_report, 0, wx.TOP | wx.ALIGN_CENTER_HORIZONTAL, 50)
        sizer_4.Add(sizer_6, 1, 0, 0)
        sizer_10.Add(sizer_4, 1, wx.ALIGN_CENTER_VERTICAL, 0)
        self.panel_3.SetSizer(sizer_10)
        sizer_5.Add(self.panel_3, 1, wx.EXPAND, 0)
        self.pane_report.SetSizer(sizer_5)
        grid_sizer_1.Add(self.label_7, 0, wx.ALIGN_CENTER_VERTICAL, 15)
        grid_sizer_1.Add(self.text_ctrl_email, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 30)
        grid_sizer_1.Add(self.label_8, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.text_ctrl_email_passwd, 0, wx.ALIGN_CENTER_VERTICAL, 52)
        grid_sizer_1.Add(self.button_cancel, 0, wx.RIGHT | wx.ALIGN_CENTER_HORIZONTAL, 30)
        grid_sizer_1.Add(self.button_save, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_31.Add(grid_sizer_1, 1, 0, 0)
        sizer_30.Add(sizer_31, 1, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_29.Add(sizer_30, 1, wx.ALIGN_CENTER_VERTICAL, 0)
        self.panel_5.SetSizer(sizer_29)
        sizer_7.Add(self.panel_5, 1, wx.EXPAND, 0)
        self.pane_password.SetSizer(sizer_7)
        self.notebook_1.AddPage(self.pane_send1, _("Send"))
        self.notebook_1.AddPage(self.pane_send2, _("Send"))
        self.notebook_1.AddPage(self.pane_templates, _("Templates"))
        self.notebook_1.AddPage(self.pane_report, _("Reports"))
        self.notebook_1.AddPage(self.pane_password, _("SMS Password"))
        sizer_1.Add(self.notebook_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade
    def on_check(self,index,flag):    #index is of the item selected, flag is boolean if selected or not
        
        self.SENDING_LIST=[]
        self.checked_indexes=[]
        
        if index==0 and flag==True:
                
            self.check_all()
                
        elif index==0 and flag==False:
            
            self.uncheck_all()
        
        # Updating the tuple of checked item indexes
        num = self.checklist_ctrl_1.GetItemCount()
        for i in range(num):
            
            if self.checklist_ctrl_1.IsChecked(i):
                
                
                email=self.checklist_ctrl_1.GetItem(i,3).GetText()
                
                try:
                    
                    self.SENDING_LIST.index(email)#Checks if the item is alreay added. In that case throw exception
            
                    
                except:
                    if email and self.V.validate_email(email)[0]:
                
                        self.SENDING_LIST.append(email) 
                        self.checked_indexes.append(i)
           
        
        if len(self.SENDING_LIST)>0:
            self.button_next.Enable()
        else:
            print "else"
            self.button_next.Disable()
            
        print self.SENDING_LIST
    def on_combo_staff(self, event):  # wxGlade: email_dialog.<event_handler>
        self.checklist_ctrl_1.DeleteAllItems()
        self.SENDING_LIST=[]
        self.button_next.Disable()
        if self.combo_box_staff.GetSelection()==2: # if student is selected
            
            self.load_year()
            self.combo_box_year.Enable(True)
        else:
            self.combo_box_year.Clear()
            self.combo_box_year.Append('Select Year')  
            self.combo_box_year.SetSelection(0)
            self.combo_box_class.SetSelection(0)
            self.combo_box_div.Clear()
            self.combo_box_div.Append('Select Division')  
            self.combo_box_div.SetSelection(0)
            self.combo_box_year.Enable(False)
            self.combo_box_class.Enable(False)
            self.combo_box_div.Enable(False)
            self.load_staff_info()
        event.Skip()

    def on_combo_year(self, event):  # wxGlade: email_dialog.<event_handler>
        self.SENDING_LIST=[]
        self.button_next.Disable()
        self.checklist_ctrl_1.DeleteAllItems()
        if self.combo_box_year.GetStringSelection()!="Select Year":
            
            self.YEAR=self.combo_box_year.Value.split('-')[0]
            self.combo_box_class.SetSelection(0)
            self.combo_box_div.Clear()
            self.combo_box_div.Append('Select Division') 
            self.combo_box_div.SetSelection(0)
            self.combo_box_div.Enable(False)
            
            
            self.combo_box_class.Enable(True)
        else:
            self.combo_box_div.Clear()
            self.combo_box_div.Append('Select Division')  
            self.combo_box_div.SetSelection(0)
            self.combo_box_class.SetSelection(0)
            self.combo_box_class.Enable(False)
            self.combo_box_div.Enable(False)
      
        event.Skip()

    def on_combo_class(self, event):  # wxGlade: email_dialog.<event_handler>
        self.SENDING_LIST=[]
        self.button_next.Disable()
        self.checklist_ctrl_1.DeleteAllItems()
        if self.combo_box_class.GetStringSelection()!="Select Standard":
            self.CLASS=self.combo_box_class.Value
            self.combo_box_div.Clear()
           
            self.load_div()
            self.combo_box_div.SetSelection(0)
            self.combo_box_div.Enable(True)
        else:
            self.combo_box_div.Clear()
            self.combo_box_div.Append('Select Division')  
            self.combo_box_div.SetSelection(0)
            
            self.combo_box_div.Enable(False)
        event.Skip()

    def on_combo_div(self, event):  # wxGlade: email_dialog.<event_handler>
        self.SENDING_LIST=[]
        self.button_next.Disable()
        
        self.DIV=self.combo_box_div.Value
        
       
        if self.combo_box_div.GetStringSelection()!="Select Division":
            
            print self.YEAR,self.CLASS,self.DIV
            
            self.load_students_info()
        event.Skip()

    def on_button_add_email(self, event):  # wxGlade: email_dialog.<event_handler>
        text=''
        invalid=''
        self.CHECK_LIST_ITEMS=[]
        
        for i in self.checked_indexes:
            
            email=self.checklist_ctrl_1.GetItem(i,3).GetText()
            
            
            if email and self.V.validate_email(email)[0]:
                
                ###if not staff
                father=self.checklist_ctrl_1.GetItem(i,2).GetText()
                name=self.checklist_ctrl_1.GetItem(i,1).GetText()
                text+=email+";"
                self.CHECK_LIST_ITEMS.append([name,father,email])
                
            else:
                self.NO_EMAIL_LIST
            
            
        
        
        self.text_ctrl_selected_email.Setself.Value(text)
        event.Skip()

        event.Skip()

    def on_button_clear_all(self, event):  # wxGlade: email_dialog.<event_handler>
        self.text_ctrl_selected_email.SetValue('')
        event.Skip()

    def on_button_close(self, event):  # wxGlade: email_dialog.<event_handler>
        self.Close()
        event.Skip()

    def on_button_next(self, event):  # wxGlade: email_dialog.<event_handler>
        #if self.validate_email():
        self.pane_send2.Show()
        self.pane_send2.SetFocus()
        self.pane_send1.Hide()
        self.notebook_1.SetSelection(1)
        msg=''
        if  len(self.NO_EMAIL_LIST):
            msg=str(len(self.NO_EMAIL_LIST))+" students/staff do not have valid Email!\n"
        msg+=str(len(self.SENDING_LIST))+" emails added to send list"
        dlg = wx.MessageDialog(self, msg, 'Error',wx.OK | wx.ICON_ERROR)                  
        dlg.ShowModal()
        dlg.Destroy()
        
        event.Skip()
        

    def on_combo_template_1(self, event):  # wxGlade: email_dialog.<event_handler>
        print "Event handler 'on_combo_template_1' not implemented!"
        event.Skip()

    def on_checkbox(self, event):  # wxGlade: email_dialog.<event_handler>
        print "Event handler 'on_checkbox' not implemented!"
        event.Skip()
    def on_button_email_passwd(self,event):# Button save email and password
        email=self.text_ctrl_email.Value
        passwd=self.text_ctrl_email_passwd.Value
        
        if not self.V.validate_email(email)[0]:
            msg="Invalid Email"
            dlg = wx.MessageDialog(self, msg, 'Error',wx.OK | wx.ICON_ERROR)                  
            dlg.ShowModal()
            dlg.Destroy()
            return 0
        self.DB.Set_SMS_Sender_Mail(email)
        self.DB.Set_SMS_Sender_Mail_Password(passwd)
        msg="Successfully Saved"
        dlg = wx.MessageDialog(self, msg, 'Success',wx.OK | wx.ICON_INFORMATION)                  
        dlg.ShowModal()
        dlg.Destroy()

        
        
    def on_button_attachments(self, event):  # wxGlade: email_dialog.<event_handler>
        wcd = 'All files (*)|*|Editor files (*.ef)|*.ef|'
        #dir = os.getcwd()
        open_dlg = wx.FileDialog(self, message='Choose a Attachmet file', defaultFile='',
        wildcard=wcd, style=wx.OPEN|wx.CHANGE_DIR)
        if open_dlg.ShowModal() == wx.ID_OK:
            path = open_dlg.GetPath()
            self.text_ctrl_attachment.SetValue(path)
        open_dlg.Destroy()
        event.Skip()

    def on_button_back(self, event):  # wxGlade: email_dialog.<event_handler>
        self.pane_send1.Show()
        
        self.notebook_1.SetSelection(0)
        self.pane_send2.Hide()
        event.Skip()

    def on_button_send(self, event):  # wxGlade: email_dialog.<event_handler>
        self.send_email()
        event.Skip()

    def on_combo_template_2(self, event):  # wxGlade: email_dialog.<event_handler>
        print "Event handler 'on_combo_template_2' not implemented!"
        event.Skip()

    def on_button_delete_temp(self, event):  # wxGlade: email_dialog.<event_handler>
        print "Event handler 'on_button_delete_temp' not implemented!"
        event.Skip()

    def on_button_add_temp(self, event):  # wxGlade: email_dialog.<event_handler>
        print "Event handler 'on_button_add_temp' not implemented!"
        event.Skip()

    def on_button_save_temp(self, event):  # wxGlade: email_dialog.<event_handler>
        print "Event handler 'on_button_save_temp' not implemented!"
        event.Skip()

    def on_email(self, event):  # wxGlade: email_dialog.<event_handler>
        if self.text_ctrl_email.Value and self.text_ctrl_email_passwd.Value:
            self.button_save.Enable()
        else:
            self.button_save.Disable()
        event.Skip()

    def on_email_password(self, event):  # wxGlade: email_dialog.<event_handler>
        
        if self.text_ctrl_email.Value and self.text_ctrl_email_passwd.Value:
            self.button_save.Enable()
        else:
            self.button_save.Disable()
        event.Skip()
        event.Skip()
    def on_msg_text(self,event):
        if self.text_ctrl_msg.Value:
            self.button_send.Enable()
            
        else:
            self.button_send.Disable()
            
        self.html_preview_1.SetPage(self.text_ctrl_msg.Value)

    def on_button_cancel(self, event):  # wxGlade: email_dialog.<event_handler>
        self.Close()
        event.Skip()
    def on_button_cancel2(self, event):  # wxGlade: sms_dialog.<event_handler>
        self.Close()
        event.Skip()
    def on_sending_list_text(self,event):
        
        if self.text_ctrl_selected_email.GetValue():
            
            self.button_clear_all.Enable()
            self.button_next.Enable()
        else:
            self.button_clear_all.Enable(False)
            self.button_next.Enable(False)

    def on_page_change(self, event):  # wxGlade: email_dialog.<event_handler>
        if self.notebook_1.GetSelection()==4:
            email=self.DB.Get_SMS_Sender_Mail()
            passwd=self.DB.Get_SMS_Sender_Mail_Password()
            self.text_ctrl_email.SetValue(email)
            self.text_ctrl_email_passwd.SetValue(passwd)
            
            
        
        event.Skip()
    def load_year(self):
        self.combo_box_year.Clear()
        self.combo_box_div.Clear()
        years=self.DB.get_academic_year_list()
        years.insert(0,"Select Year")

        
        for item in years:
            self.combo_box_year.Append(str(item))
            
        self.combo_box_year.SetSelection(0) 
        self.combo_box_class.SetSelection(0) 
        
    def load_div(self):
        # token 1 for one set of combos...token 2 for the other set
        self.combo_box_div.Clear()
            
        divs=self.DB.Get_Div(self.YEAR,self.CLASS)
        divs=['Select Division']+divs
        
        for item in divs:
            self.combo_box_div.Append(str(item))   
    def load_staff_info(self):
        self.checklist_ctrl_1.DeleteAllItems()
        self.CHECK_LIST_ITEMS=[]
        self.NO_EMAIL_LIST=[]
        
        self.checklist_ctrl_1.DeleteAllColumns()
        self.checklist_ctrl_1.InsertColumn(0, "Sl No", width=50)
        self.checklist_ctrl_1.InsertColumn(1, 'Name of Staff', width=220)
        self.checklist_ctrl_1.InsertColumn(2, 'Designation',width=220)
        self.checklist_ctrl_1.InsertColumn(3, 'Email',width=200)
        
        self.temp_list=self.DB.Get_Staff_Info()
        
        
        for each in self.temp_list:
            
            email=each[3]
            if not each[2]:email=''
            #print "mob",mobile,"        ",self.validate_mobile(mobile,silent=True)
            if email and self.V.validate_email(email)[0]:
                
                if not each[1]:each[1]=''
                
                self.CHECK_LIST_ITEMS.append([each[0],each[1],email])
            
          
        i= 0    
        
            
        for each in self.CHECK_LIST_ITEMS:
           
            
                
            
            
            if i==0:
                index = self.checklist_ctrl_1.InsertStringItem(0,'')
            
                self.checklist_ctrl_1.SetStringItem(index, 1, "Select All")
                i+=1
                #continue
                
            index = self.checklist_ctrl_1.InsertStringItem(sys.maxint, each[0])
            self.checklist_ctrl_1.SetStringItem(index, 0, str(i))
            self.checklist_ctrl_1.SetStringItem(index, 1, each[0])
            self.checklist_ctrl_1.SetStringItem(index, 2, each[1])
            self.checklist_ctrl_1.SetStringItem(index, 3, each[2])
            
            i+=1
    
    def load_students_info(self):
        
        #if self.checklist_ctrl_1.GetItemCount():
        self.checklist_ctrl_1.DeleteAllItems()
        self.CHECK_LIST_ITEMS=[]
        self.NO_EMAIL_LIST=[]
        
        
        self.checklist_ctrl_1.DeleteAllColumns()
        self.checklist_ctrl_1.InsertColumn(0, "Sl No", width=50)
        self.checklist_ctrl_1.InsertColumn(1, 'Name of Student', width=220)
        self.checklist_ctrl_1.InsertColumn(2, 'Name of Parent',width=220)
        self.checklist_ctrl_1.InsertColumn(3, 'Email',width=200)
        
        
        self.temp_list=self.DB.Get_Student_List(self.YEAR,self.combo_box_class.Value,self.combo_box_div.Value)
        
        
        for each in self.temp_list:
            
            mobile=self.DB.Get_Email(each[1])
            #print "mob",mobile,"        ",self.validate_mobile(mobile,silent=True)
            if mobile and self.V.validate_email(mobile)[0]:
                
                father=self.DB.Get_Father(each[1])
                self.CHECK_LIST_ITEMS.append([each[2],father,mobile])
            else:
                
                self.NO_EMAIL_LIST.append(each[2])
          
        i= 0    
        
            
        for each in self.CHECK_LIST_ITEMS:
           
            
                
            
            
            if i==0:
                index = self.checklist_ctrl_1.InsertStringItem(0,'')
            
                self.checklist_ctrl_1.SetStringItem(index, 1, "Select All")
                i+=1
                #continue
                
            index = self.checklist_ctrl_1.InsertStringItem(sys.maxint, each[0])
            self.checklist_ctrl_1.SetStringItem(index, 0, str(i))
            self.checklist_ctrl_1.SetStringItem(index, 1, each[0])
            self.checklist_ctrl_1.SetStringItem(index, 2, each[1])
            self.checklist_ctrl_1.SetStringItem(index, 3, each[2])
            
            i+=1
    
    def check_all(self):
        
        num = self.checklist_ctrl_1.GetItemCount()
        for i in range(num):
            self.checklist_ctrl_1.CheckItem(i)
            
    def uncheck_all(self):
        
        num = self.checklist_ctrl_1.GetItemCount()
        for i in range(num):
            self.checklist_ctrl_1.CheckItem(i,False)
            
    def validate_email(self):
        
        self.CHECK_LIST_ITEMS=[]
        
        sending_numbers=self.text_ctrl_selected_email.Value
        sending_numbers=sending_numbers.split(";")
        
        for email in sending_numbers:
            print email
            if not email:
                continue
            
            
            if self.V.validate_email(email)[0]:
                self.CHECK_LIST_ITEMS.append(email)
                
            else:
                #msg=email+" is invalid email id. Either edit or delete it to continue!"
                #dlg = wx.MessageDialog(self, msg, 'Error',wx.OK | wx.ICON_ERROR)                  
                #dlg.ShowModal()
                #dlg.Destroy()
                
                return 0
            
        return True
    
    def send_email(self):
        email=''
        passwd=''
        print "send email"
        S=send_gmail('asif.kodur@gmail.com','Asif@9656424182')
        
        S.send('asif.kodur@gmail.com','asif.kodur@gmail.com',msg='',attachments=['vertical.pdf'])
        
    def personalise_msg(self):
        text=self.text_ctrl_msg.Value
        
    # end of class email_dialog
if __name__ == "__main__":
    '''
    gettext.install("app") # replace with the appropriate catalog name

    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = email_dialog(None, wx.ID_ANY, "")
    app.SetTopWindow(frame_1)
    frame_1.ShowModal()
    app.MainLoop()
    frame_1.Destroy()
    '''
    temp=email_templates()
    temp.find_templates()