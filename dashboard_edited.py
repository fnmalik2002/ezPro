# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version 3.10.1-40-g8042f487)
# http://www.wxformbuilder.org/
# PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################
import datetime
import os
import platform
import subprocess
from datetime import datetime as dt
import code128
import fitz
import pandas as pd
import pymysql
import wx.grid
import yaml
import barcode_printer_new as bar_sheet
import configsheet_gui_edited as gui
import discontinued_items_management as discont
import inventory_search as inv
import login_edited
import user_management
from company_logo import *


class MyDiscontinueViewer(wx.Dialog):
    def __init__(self, parent, title, caption):
        style = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER
        super(MyDiscontinueViewer, self).__init__(parent, -1, title, style=style)
        text = wx.StaticText(self, -1, caption)
        inpt = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE)
        inpt.SetInitialSize((400, 700))
        buttons = self.CreateButtonSizer(wx.OK | wx.CANCEL)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(text, 0, wx.ALL, 5)
        sizer.Add(inpt, 1, wx.EXPAND | wx.ALL, 5)
        sizer.Add(buttons, 0, wx.EXPAND | wx.ALL, 5)
        self.SetSizerAndFit(sizer)
        inpt.SetFocus()
        self.input = inpt

        # self.input.SetFocus()

    def SetValue(self, value):
        for text in value:
            self.input.AppendText(text + "\n")

    def GetValue(self):
        return self.input.GetValue()


###########################################################################
# Class MyDashboard
###########################################################################
def get_config(file):
    with open(file, "r") as ymlfile:
        cfg = yaml.safe_load(ymlfile)

    for section in cfg:
        print(section)
    ip = cfg["database"]['ip']
    user = 'xxxx'  # cfg["database"]['user']
    password = 'xxxx'  # cfg["database"]['passwd']
    db = 'xxxx'  # cfg["database"]['db']
    bins = cfg["other"]['bins']
    to_email = cfg["other"]['to_email']
    out = {
        'ip': ip,
        'user': user,
        'pw': password,
        'db': db,
        'bins': bins,
        'to_email': to_email,
    }

    return out


class MyTextEntryDialog(wx.Dialog):
    """
    A custom dialog entry box with multiline text field
    """

    def __init__(self, parent, title, caption):
        style = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER
        super(MyTextEntryDialog, self).__init__(parent, -1, title, style=style)
        text = wx.StaticText(self, -1, caption)
        inpt = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE)
        inpt.SetInitialSize((800, 700))
        buttons = self.CreateButtonSizer(wx.OK | wx.CANCEL)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(text, 0, wx.ALL, 5)
        sizer.Add(inpt, 1, wx.EXPAND | wx.ALL, 5)
        sizer.Add(buttons, 0, wx.EXPAND | wx.ALL, 5)
        self.SetSizerAndFit(sizer)
        inpt.SetFocus()
        self.input = inpt

    def SetValue(self, value):
        self.input.SetValue(value)

    def GetValue(self):
        return self.input.GetValue()


class MyDashboard(wx.Frame):
    """
    The main entry point for the ezPro document flow management
    """
    today = str(dt.now().date())
    date_today = str(dt.now())
    try:
        conf = get_config(os.path.abspath('.\\templates\config.yml'))
    except:
        conf = get_config(os.path.abspath('./templates/config.yml'))
    ip = conf['ip']
    user = conf['user']
    password = conf['pw']
    db = conf['db']
    bins = conf['bins']
    to_email = conf['to_email']
    data_selected_sheet = {}
    configsheet_template_file_path = os.path.abspath('.\\templates\Ebay Config Sheet Rev1.5_template.pdf')
    configsheet_file_produced_path = os.path.abspath('.\\output\Ebay Config Sheet Rev1.5.pdf')
    version_number = "ezPro Ver 8.0"

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"ezPro - Dashboard", pos=wx.DefaultPosition,
                          size=wx.Size(-1, -1), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        # convert the embedded image bytes into images for use in gui
        self.logo_med = wx.Image(l_med.GetImage()).ConvertToBitmap()
        self.logo_lrg = wx.Image(l_lar.GetImage()).ConvertToBitmap()
        # sets icon for title bar for current frame
        self.SetIcon(wx.Icon(self.logo_lrg))
        self.program_log = ''
        # generates a sequence of numbers starting from 0 and everytime it is called it returns next number
        self.gen = self.infinite_sequence()
        self.loggedin_user = ''
        self.loggedin_user_id = 0
        self.loggedin_user_is_manager = False
        self.loggedin_user_is_active = False
        self.loggedin_user_is_tier2 = False
        self.loggedin_user_is_tier3 = False
        self.loggedin_user_first_name = ''
        self.loggedin_user_last_name = ''
        self.total_Number_of_rows_of_data_returned = []
        self.SetSizeHints(wx.Size(1000, 700), wx.DefaultSize)
        self.qty_n = ''

        bSizer_main = wx.BoxSizer(wx.HORIZONTAL)

        self.m_panel_button_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel_button_panel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)
        bSizer3.Add((0, 40), 0, wx.EXPAND, 5)
        self.m_bitmap1 = wx.StaticBitmap(self.m_panel_button_panel, wx.ID_ANY,
                                         wx.Bitmap(self.logo_lrg), wx.DefaultPosition, wx.DefaultSize,
                                         0)
        bSizer3.Add(self.m_bitmap1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer3.Add((0, 0), 0, wx.EXPAND, 5)

        bSizer2.Add(bSizer3, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        bSizer13 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer4.Add(bSizer13, 1, wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.m_staticText_welcome = wx.StaticText(self.m_panel_button_panel, wx.ID_ANY, u"    Welcome!",
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_welcome.Wrap(-1)

        self.m_staticText_welcome.SetFont(
            wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande"))
        self.m_staticText_welcome.SetForegroundColour(wx.Colour(76, 76, 76))

        bSizer4.Add(self.m_staticText_welcome, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        bSizer4.Add((0, 100), 1, wx.EXPAND, 5)
        self.m_button_all_sheets = wx.Button(self.m_panel_button_panel, wx.ID_ANY, u"    All Sheets",
                                             wx.DefaultPosition,
                                             wx.Size(130, -1), style=wx.BU_LEFT)
        bSizer4.Add(self.m_button_all_sheets, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 2)

        self.m_button_home = wx.Button(self.m_panel_button_panel, wx.ID_ANY, u"    My Sheets", wx.DefaultPosition,
                                       wx.Size(130, -1), style=wx.BU_LEFT)
        bSizer4.Add(self.m_button_home, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 2)

        self.m_button_add_new_sheet = wx.Button(self.m_panel_button_panel, wx.ID_ANY, u"    New Sheet...",
                                                wx.DefaultPosition, wx.Size(130, -1), style=wx.BU_LEFT)
        bSizer4.Add(self.m_button_add_new_sheet, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 2)
        self.m_button_my_sheets_pdf_today = wx.Button(self.m_panel_button_panel, wx.ID_ANY, u"    PDF Today",
                                                      wx.DefaultPosition,
                                                      wx.Size(130, -1), style=wx.BU_LEFT)
        bSizer4.Add(self.m_button_my_sheets_pdf_today, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 2)
        self.m_button_listed_excel_today = wx.Button(self.m_panel_button_panel, wx.ID_ANY, u"    Listed Today",
                                                      wx.DefaultPosition,
                                                      wx.Size(130, -1), style=wx.BU_LEFT)
        bSizer4.Add(self.m_button_listed_excel_today, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 2)
        bSizer4.Add((0, 30), 1, wx.EXPAND, 5)

        self.m_button_search_inv = wx.Button(self.m_panel_button_panel, wx.ID_ANY, u"    Inventory...",
                                             wx.DefaultPosition,
                                             wx.Size(130, -1), style=wx.BU_LEFT)
        bSizer4.Add(self.m_button_search_inv, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 2)

        self.m_button_show_discontinue = wx.Button(self.m_panel_button_panel, wx.ID_ANY, u"    Discontinued...",
                                                   wx.DefaultPosition,
                                                   wx.Size(130, -1), style=wx.BU_LEFT)
        bSizer4.Add(self.m_button_show_discontinue, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 2)

        self.m_button_show_log = wx.Button(self.m_panel_button_panel, wx.ID_ANY, u"    logs...",
                                           wx.DefaultPosition,
                                           wx.Size(130, -1), style=wx.BU_LEFT)
        bSizer4.Add(self.m_button_show_log, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 2)

        self.m_button_create_excel = wx.Button(self.m_panel_button_panel, wx.ID_ANY, u"    Excel...",
                                               wx.DefaultPosition,
                                               wx.Size(130, -1), style=wx.BU_LEFT)
        bSizer4.Add(self.m_button_create_excel, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 2)
        self.m_button_create_barcode = wx.Button(self.m_panel_button_panel, wx.ID_ANY, u"    Barcode...",
                                                 wx.DefaultPosition,
                                                 wx.Size(130, -1), style=wx.BU_LEFT)
        bSizer4.Add(self.m_button_create_barcode, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 2)
        self.m_button_user_management = wx.Button(self.m_panel_button_panel, wx.ID_ANY, u"    Users...",
                                                  wx.DefaultPosition,
                                                  wx.Size(130, -1), style=wx.BU_LEFT)
        bSizer4.Add(self.m_button_user_management, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 2)

        bSizer4.Add((0, 0), 2, wx.EXPAND, 5)

        bSizer4.Add((0, 0), 6, wx.EXPAND, 5)

        self.m_button_logout = wx.Button(self.m_panel_button_panel, wx.ID_ANY, u"Logout", wx.DefaultPosition,
                                         wx.Size(130, -1), 0)
        bSizer4.Add(self.m_button_logout, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 2)

        self.m_staticText_empty = wx.StaticText(self.m_panel_button_panel, wx.ID_ANY,
                                                u"\n\t    {}".format(self.version_number),
                                                wx.DefaultPosition, wx.Size(180, -1), 0)
        bSizer4.Add(self.m_staticText_empty, 0, wx.EXPAND | wx.ALL, 2)

        bSizer4.Add((0, 30), 0, wx.EXPAND, 5)

        bSizer2.Add(bSizer4, 0, wx.EXPAND, 5)

        self.m_panel_button_panel.SetSizer(bSizer2)
        self.m_panel_button_panel.Layout()
        bSizer2.Fit(self.m_panel_button_panel)
        bSizer_main.Add(self.m_panel_button_panel, 0, wx.ALL | wx.EXPAND, 0)

        self.m_panel_grid_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel_grid_panel.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.m_panel_grid_panel.SetMinSize(wx.Size(1480, 700))

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        bSizer101 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel6 = wx.Panel(self.m_panel_grid_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                 wx.TAB_TRAVERSAL)
        bSizer111 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer121 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_searchCtrl1 = wx.SearchCtrl(self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                           wx.Size(350, -1), wx.TE_PROCESS_ENTER)
        self.m_searchCtrl1.ShowSearchButton(True)
        self.m_searchCtrl1.ShowCancelButton(True)
        bSizer121.Add(self.m_searchCtrl1, 0, wx.ALL | wx.ALIGN_BOTTOM, 5)

        # self.m_button_search_last_ten_days = wx.Button(self.m_panel6, wx.ID_ANY, u"Last 10 days", wx.DefaultPosition,
        #                                  wx.Size(130, -1), 0)
        # bSizer121.Add(self.m_button_search_last_ten_days, 0, wx.ALL | wx.ALIGN_BOTTOM, 5)

        bSizer111.Add(bSizer121, 0, wx.EXPAND, 5)

        bSizer131 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText3 = wx.StaticText(self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText3.Wrap(-1)

        bSizer131.Add(self.m_staticText3, 0, wx.ALL, 5)

        bSizer111.Add(bSizer131, 1, wx.EXPAND, 5)
        # ---------------------------------------
        # bSizer14 = wx.BoxSizer(wx.VERTICAL)
        #
        # self.m_staticText_total_config_sheet_text = wx.StaticText(self.m_panel6, wx.ID_ANY, u" Total Config Sheets", wx.DefaultPosition,
        #                                                           wx.DefaultSize, 0 | wx.CLIP_CHILDREN)
        # self.m_staticText_total_config_sheet_text.Wrap(-1)
        #
        # self.m_staticText_total_config_sheet_text.SetFont(
        #     wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande"))
        # self.m_staticText_total_config_sheet_text.SetForegroundColour(wx.Colour(76, 76, 76))
        #
        # # bSizer14.Add(self.m_staticText_total_config_sheet_text, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)
        #
        # self.m_staticText_new_sheet_qty = wx.StaticText(self.m_panel6, wx.ID_ANY, u"", wx.DefaultPosition,
        #                                                 wx.DefaultSize, 0 | wx.BORDER_RAISED)
        # self.m_staticText_new_sheet_qty.Wrap(-1)
        #
        # self.m_staticText_new_sheet_qty.SetFont(
        #     wx.Font(36, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande"))
        # self.m_staticText_new_sheet_qty.SetForegroundColour(wx.Colour(255, 255, 255))
        # self.m_staticText_new_sheet_qty.SetBackgroundColour(wx.Colour(76, 76, 76))

        # bSizer14.Add(self.m_staticText_new_sheet_qty, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 0)

        # bSizer111.Add(bSizer14, 0, wx.ALIGN_CENTER_VERTICAL, 5)
        # ___________________________________________________________________
        self.m_panel6.SetSizer(bSizer111)
        self.m_panel6.Layout()
        bSizer111.Fit(self.m_panel6)
        bSizer101.Add(self.m_panel6, 0, wx.EXPAND | wx.ALL, 5)

        bSizer9.Add(bSizer101, 0, wx.EXPAND, 5)

        self.m_notebook2 = wx.Notebook(self.m_panel_grid_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.bookpanel_new = wx.Panel(self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL,
                                      name="new_tab")
        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        self.m_grid_new = wx.grid.Grid(self.bookpanel_new, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid_new.CreateGrid(10000, 8)
        self.m_grid_new.EnableEditing(True)
        self.m_grid_new.EnableGridLines(True)
        self.m_grid_new.EnableDragGridSize(True)
        self.m_grid_new.SetMargins(0, 0)

        # Columns
        self.m_grid_new.SetColSize(0, 60)
        self.m_grid_new.SetColSize(1, 90)
        self.m_grid_new.SetColSize(2, 60)
        self.m_grid_new.SetColSize(3, 70)
        self.m_grid_new.SetColSize(4, 100)
        self.m_grid_new.SetColSize(5, 200)
        self.m_grid_new.SetColSize(6, 750)
        self.m_grid_new.SetColSize(7, 260)

        self.m_grid_new.EnableDragColMove(False)
        self.m_grid_new.EnableDragColSize(True)
        self.m_grid_new.SetColLabelValue(0, u"Sheet #")
        self.m_grid_new.SetColLabelValue(1, u"Submit Date")
        self.m_grid_new.SetColLabelValue(2, u"Price")
        self.m_grid_new.SetColLabelValue(3, u"Qty")
        self.m_grid_new.SetColLabelValue(4, u"Classification")
        self.m_grid_new.SetColLabelValue(5, u"Model Number")
        self.m_grid_new.SetColLabelValue(6, u"Title")
        self.m_grid_new.SetColLabelValue(7, u"PO Number")

        self.m_grid_new.SetColLabelSize(wx.grid.GRID_AUTOSIZE)
        self.m_grid_new.SetColLabelAlignment(wx.ALIGN_LEFT, wx.ALIGN_LEFT)

        # Rows

        self.m_grid_new.EnableDragRowSize(True)
        self.m_grid_new.SetRowLabelSize(wx.grid.GRID_AUTOSIZE)
        self.m_grid_new.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults

        self.m_grid_new.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer10.Add(self.m_grid_new, 1, wx.ALL | wx.EXPAND, 5)

        self.bookpanel_new.SetSizer(bSizer10)
        self.bookpanel_new.Layout()
        bSizer10.Fit(self.bookpanel_new)
        self.m_notebook2.AddPage(self.bookpanel_new, u"New", True)

        # Listed Tab creation
        self.bookpanel_listed = wx.Panel(self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                         wx.TAB_TRAVERSAL, name="listed_tab")
        bSizer11 = wx.BoxSizer(wx.VERTICAL)
        self.m_grid_listed = wx.grid.Grid(self.bookpanel_listed, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid_listed.CreateGrid(10000, 10)
        self.m_grid_listed.EnableEditing(True)
        self.m_grid_listed.EnableGridLines(True)
        self.m_grid_listed.EnableDragGridSize(True)
        self.m_grid_listed.SetMargins(0, 0)

        # Columns
        self.m_grid_listed.SetColSize(0, 60)
        self.m_grid_listed.SetColSize(1, 90)
        self.m_grid_listed.SetColSize(2, 80)
        self.m_grid_listed.SetColSize(3, 80)
        self.m_grid_listed.SetColSize(4, 80)
        self.m_grid_listed.SetColSize(5, 70)
        self.m_grid_listed.SetColSize(6, 100)
        self.m_grid_listed.SetColSize(7, 200)
        self.m_grid_listed.SetColSize(8, 750)
        self.m_grid_listed.SetColSize(9, 260)

        self.m_grid_listed.EnableDragColMove(False)
        self.m_grid_listed.EnableDragColSize(True)
        self.m_grid_listed.SetColLabelValue(0, u"Sheet #")
        self.m_grid_listed.SetColLabelValue(1, u"Listed Date")
        self.m_grid_listed.SetColLabelValue(2, u"EZ Part")
        self.m_grid_listed.SetColLabelValue(3, u"Bin Number")
        self.m_grid_listed.SetColLabelValue(4, u"Qty Listed")
        self.m_grid_listed.SetColLabelValue(5, u"Sold")
        self.m_grid_listed.SetColLabelValue(6, u"Classification")
        self.m_grid_listed.SetColLabelValue(7, u"Model Number")
        self.m_grid_listed.SetColLabelValue(8, u"Title")
        self.m_grid_listed.SetColLabelValue(9, u"PO Number")
        self.m_grid_listed.SetColLabelSize(wx.grid.GRID_AUTOSIZE)
        self.m_grid_listed.SetColLabelAlignment(wx.ALIGN_LEFT, wx.ALIGN_LEFT)

        # Rows
        self.m_grid_listed.EnableDragRowSize(True)
        self.m_grid_listed.SetRowLabelSize(wx.grid.GRID_AUTOSIZE)
        self.m_grid_listed.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.m_grid_listed.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer11.Add(self.m_grid_listed, 0, wx.ALL | wx.EXPAND, 5)

        self.bookpanel_listed.SetSizer(bSizer11)
        self.bookpanel_listed.Layout()
        bSizer11.Fit(self.bookpanel_listed)
        self.m_notebook2.AddPage(self.bookpanel_listed, u"Listed", False)

        # Rejected Tab creation
        self.bookpanel_rejected = wx.Panel(self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.TAB_TRAVERSAL, name="rejected_tab")
        bSizer12 = wx.BoxSizer(wx.VERTICAL)

        self.m_grid_rejected = wx.grid.Grid(self.bookpanel_rejected, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid_rejected.CreateGrid(10000, 8)
        self.m_grid_rejected.EnableEditing(True)
        self.m_grid_rejected.EnableGridLines(True)
        self.m_grid_rejected.EnableDragGridSize(True)
        self.m_grid_rejected.SetMargins(0, 0)

        # Columns
        self.m_grid_rejected.SetColSize(0, 60)
        self.m_grid_rejected.SetColSize(1, 90)
        self.m_grid_rejected.SetColSize(2, 60)
        self.m_grid_rejected.SetColSize(3, 70)
        self.m_grid_rejected.SetColSize(4, 100)
        self.m_grid_rejected.SetColSize(5, 200)
        self.m_grid_rejected.SetColSize(6, 750)
        self.m_grid_rejected.SetColSize(7, 260)

        self.m_grid_rejected.EnableDragColMove(False)
        self.m_grid_rejected.EnableDragColSize(True)
        self.m_grid_rejected.SetColLabelValue(0, u"Sheet #")
        self.m_grid_rejected.SetColLabelValue(1, u"Rejected Date")
        self.m_grid_rejected.SetColLabelValue(2, u"Price")
        self.m_grid_rejected.SetColLabelValue(3, u"Qty")
        self.m_grid_rejected.SetColLabelValue(4, u"Classification")
        self.m_grid_rejected.SetColLabelValue(5, u"Model Number")
        self.m_grid_rejected.SetColLabelValue(6, u"Title")
        self.m_grid_rejected.SetColLabelValue(7, u"PO Number")

        self.m_grid_rejected.SetColLabelSize(wx.grid.GRID_AUTOSIZE)
        self.m_grid_rejected.SetColLabelAlignment(wx.ALIGN_LEFT, wx.ALIGN_LEFT)

        # Rows
        self.m_grid_rejected.EnableDragRowSize(True)
        self.m_grid_rejected.SetRowLabelSize(wx.grid.GRID_AUTOSIZE)
        self.m_grid_rejected.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.m_grid_rejected.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer12.Add(self.m_grid_rejected, 0, wx.ALL | wx.EXPAND, 5)

        self.bookpanel_rejected.SetSizer(bSizer12)
        self.bookpanel_rejected.Layout()
        bSizer12.Fit(self.bookpanel_rejected)
        self.m_notebook2.AddPage(self.bookpanel_rejected, u"Rejected", False)

        # _____________
        # Archived Tab creation
        self.bookpanel_archived = wx.Panel(self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.TAB_TRAVERSAL, name="archived_tab")
        bSizer1111 = wx.BoxSizer(wx.VERTICAL)
        self.m_grid_archived = wx.grid.Grid(self.bookpanel_archived, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid_archived.CreateGrid(10000, 10)
        self.m_grid_archived.EnableEditing(True)
        self.m_grid_archived.EnableGridLines(True)
        self.m_grid_archived.EnableDragGridSize(True)
        self.m_grid_archived.SetMargins(0, 0)

        # Columns
        self.m_grid_archived.SetColSize(0, 60)
        self.m_grid_archived.SetColSize(1, 90)
        self.m_grid_archived.SetColSize(2, 80)
        self.m_grid_archived.SetColSize(3, 80)
        self.m_grid_archived.SetColSize(4, 80)
        self.m_grid_archived.SetColSize(5, 70)
        self.m_grid_archived.SetColSize(6, 100)
        self.m_grid_archived.SetColSize(7, 200)
        self.m_grid_archived.SetColSize(8, 750)
        self.m_grid_archived.SetColSize(9, 260)

        self.m_grid_archived.EnableDragColMove(False)
        self.m_grid_archived.EnableDragColSize(True)
        self.m_grid_archived.SetColLabelValue(0, u"Sheet #")
        self.m_grid_archived.SetColLabelValue(1, u"Archived Date")
        self.m_grid_archived.SetColLabelValue(2, u"EZ Part")
        self.m_grid_archived.SetColLabelValue(3, u"Bin Number")
        self.m_grid_archived.SetColLabelValue(4, u"Qty Listed")
        self.m_grid_archived.SetColLabelValue(5, u"Sold")
        self.m_grid_archived.SetColLabelValue(6, u"Classification")
        self.m_grid_archived.SetColLabelValue(7, u"Model Number")
        self.m_grid_archived.SetColLabelValue(8, u"Title")
        self.m_grid_archived.SetColLabelValue(9, u"PO Number")
        self.m_grid_archived.SetColLabelSize(wx.grid.GRID_AUTOSIZE)
        self.m_grid_archived.SetColLabelAlignment(wx.ALIGN_LEFT, wx.ALIGN_LEFT)

        # Rows
        self.m_grid_archived.EnableDragRowSize(True)
        self.m_grid_archived.SetRowLabelSize(wx.grid.GRID_AUTOSIZE)
        self.m_grid_archived.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.m_grid_archived.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer1111.Add(self.m_grid_archived, 0, wx.ALL | wx.EXPAND, 5)

        self.bookpanel_archived.SetSizer(bSizer1111)
        self.bookpanel_archived.Layout()
        bSizer1111.Fit(self.bookpanel_archived)
        self.m_notebook2.AddPage(self.bookpanel_archived, u"Archived", False)
        # _______________

        bSizer9.Add(self.m_notebook2, 0, wx.ALL | wx.EXPAND, 0)

        self.m_panel_grid_panel.SetSizer(bSizer9)
        self.m_panel_grid_panel.Layout()
        bSizer9.Fit(self.m_panel_grid_panel)
        bSizer_main.Add(self.m_panel_grid_panel, 1, wx.ALL | wx.EXPAND, 1)

        self.SetSizer(bSizer_main)
        self.Layout()
        bSizer_main.Fit(self)
        # add icons to buttons
        self.m_button_all_sheets.SetBitmap(wx.Bitmap(wx.Image(all_sheets.GetImage()).ConvertToBitmap()))
        self.m_button_home.SetBitmap(wx.Bitmap(wx.Image(my_sheets.GetImage()).ConvertToBitmap()))
        self.m_button_my_sheets_pdf_today.SetBitmap(wx.Bitmap(wx.Image(pdf.GetImage()).ConvertToBitmap()))
        self.m_button_add_new_sheet.SetBitmap(wx.Bitmap(wx.Image(new_sheet.GetImage()).ConvertToBitmap()))
        self.m_button_search_inv.SetBitmap(wx.Bitmap(wx.Image(inventory.GetImage()).ConvertToBitmap()))
        self.m_button_show_discontinue.SetBitmap(wx.Bitmap(wx.Image(discontinue.GetImage()).ConvertToBitmap()))
        self.m_button_user_management.SetBitmap(wx.Bitmap(wx.Image(manage_users.GetImage()).ConvertToBitmap()))
        self.m_button_show_log.SetBitmap(wx.Bitmap(wx.Image(logit.GetImage()).ConvertToBitmap()))
        self.m_button_logout.SetBitmap(wx.Bitmap(wx.Image(logout.GetImage()).ConvertToBitmap()))
        self.m_button_create_excel.SetBitmap(wx.Bitmap(wx.Image(excel_png.GetImage()).ConvertToBitmap()))
        self.m_button_create_barcode.SetBitmap(wx.Bitmap(wx.Image(barcode_png.GetImage()).ConvertToBitmap()))
        self.m_button_listed_excel_today.SetBitmap(wx.Bitmap(wx.Image(excel_png.GetImage()).ConvertToBitmap()))

        self.Centre(wx.BOTH)

        # Connect Events

        # self.m_notebook2.Bind(wx.EVT_BOOKCTRL_PAGE_CHANGED, self.on_tab_change)
        self.m_notebook2.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.on_tab_change)
        self.m_button_all_sheets.Bind(wx.EVT_BUTTON, self.show_all_sheets)
        self.m_button_home.Bind(wx.EVT_BUTTON, self.on_home)
        self.m_button_my_sheets_pdf_today.Bind(wx.EVT_BUTTON, self.my_todays_pdf)
        self.m_button_logout.Bind(wx.EVT_BUTTON, self.logout)
        self.m_button_add_new_sheet.Bind(wx.EVT_BUTTON, self.new_sheet)
        self.m_button_user_management.Bind(wx.EVT_BUTTON, self.user_management)
        self.m_searchCtrl1.Bind(wx.EVT_SEARCHCTRL_SEARCH_BTN, self.search)
        self.m_button_show_log.Bind(wx.EVT_BUTTON, self.show_log)
        self.m_button_create_excel.Bind(wx.EVT_BUTTON, self.create_excel)
        self.m_button_create_barcode.Bind(wx.EVT_BUTTON, self.create_barcode_sheet)
        self.m_button_listed_excel_today.Bind(wx.EVT_BUTTON, self.create_listed_today_excel)
        # self.m_searchCtrl1.Bind(wx.EVT_TEXT, self.search)

        # self.bookpanel_new.Bind(wx.EVT_CONTEXT_MENU, self.OnShowPopup)

        self.m_button_search_inv.Bind(wx.EVT_BUTTON, self.search_inv)
        self.m_button_show_discontinue.Bind(wx.EVT_BUTTON, self.discontinue_viewer)

        self.m_grid_new.Bind(wx.grid.EVT_GRID_LABEL_LEFT_CLICK, self.sort_by_this_column)
        self.m_grid_new.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.new_cell_clicked)
        self.m_grid_new.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.new_cell_double_clicked)
        self.m_grid_new.Bind(wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.new_cell_right_clicked)
        self.m_grid_new.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.new_cell_left_click)

        self.m_grid_listed.Bind(wx.grid.EVT_GRID_LABEL_LEFT_CLICK, self.sort_by_this_column)
        self.m_grid_listed.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.listed_cell_double_clicked)
        self.m_grid_listed.Bind(wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.listed_cell_right_clicked)
        self.m_grid_listed.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.listed_cell_left_click)

        self.m_grid_rejected.Bind(wx.grid.EVT_GRID_LABEL_LEFT_CLICK, self.sort_by_this_column)
        self.m_grid_rejected.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.rejected_cell_double_clicked)
        self.m_grid_rejected.Bind(wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.rejected_cell_right_clicked)
        self.m_grid_rejected.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.rejected_cell_left_click)

        self.m_grid_archived.Bind(wx.grid.EVT_GRID_LABEL_LEFT_CLICK, self.sort_by_this_column)
        self.m_grid_archived.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.archived_cell_double_clicked)
        # self.m_grid_archived.Bind(wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.archived_cell_right_clicked)
        self.m_grid_archived.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.archived_cell_left_click)

        self.clicks = []
        self.model_selected = ''
        self.sh_id = None
        self.addlog("ip address of database : " + self.ip)
        self.row_data = []
        # create status bar
        self.statusBar = self.CreateStatusBar(style=wx.BORDER_NONE)
        # set text to status bar
        self.statusBar.SetStatusText("Nothing to show here for now...")

    def create_barcode_sheet(self, event):
        print("create barcode sheet is invoked")
        frame = bar_sheet.LabelSheetPrinter(self)
        frame.Show()

    def query_database(self, qry="", val=""):

        cursor = pymysql.cursors.DictCursor
        conn = pymysql.connect(host=self.ip,
                               user=self.user,
                               password=self.password,
                               db=self.db,
                               charset='utf8mb4',
                               cursorclass=cursor)

        try:
            with conn.cursor() as cur:
                cur.execute(qry, val)
                results = cur.fetchall()  # .groupby(['sheet_id'])

        except pymysql.err.OperationalError as error:
            print(error)
            # wx.MessageBox("No connection to the database.", "Error!", wx.ICON_ERROR)
        finally:
            conn.close()
        return results

    def my_todays_pdf(self, event):
        event.Skip()

        my_qry = "SELECT sheet_id FROM ConfigSheet WHERE (tech_id = {} AND new = True AND listed = False AND rejected = False AND date_submitted = '{}') ORDER BY sheet_id".format(
            self.loggedin_user_id, self.today)
        data = self.query_database(my_qry)
        print(len(data), data)

        frm = gui.MyConfigSheet(self)
        frm.ip = self.ip
        frm.user = self.user
        frm.db = self.db
        frm.password = self.password
        frm.bins = self.bins
        frm.to_email = self.to_email
        for i in data:
            print(i['sheet_id'], i)
            frm.create_pdf_on_right_click(i['sheet_id'])
            self.addlog("pdf created, now adding barcode to it.")
            self.add_barcode(str(i['sheet_id']) + "-" + self.qty_n, self.configsheet_file_produced_path)
            self.addlog("Add barcode command finished.")
            # time.sleep(1)
            if os.path.exists(self.configsheet_file_produced_path):
                outpath = ("_{}.pdf".format(next(self.gen))).join(self.configsheet_file_produced_path.split('.pdf'))
                os.rename(self.configsheet_file_produced_path, outpath)
            else:
                print("The file does not exist")
            # time.sleep(1)

    def create_listed_today_excel(self, event):
        event.Skip()
        values = [{"Sheet ID": int(self.m_grid_listed.GetCellValue(row, 0)), "Part No": self.m_grid_listed.GetCellValue(row, 2),"Bin No": self.m_grid_listed.GetCellValue(row, 3),}
                  for row in range(self.m_grid_listed.GetNumberRows()) if self.m_grid_listed.GetCellValue(row, 1)== self.today]
        print(values)
        print('col 1 = ',self.m_grid_listed.GetCellValue(0, 1))
        df = pd.DataFrame(values)
        excel_file = "output\\Config Sheets listed on {}.xlsx".format(datetime.datetime.now().date().today())
        print(excel_file)
        try:
            df.to_excel(excel_file, index=False,
                        header=["Sheet No", "Part No ", "Bin No"])
            print(df)
        except Exception as e:
            print(e)


    def create_excel(self, event):
        """Creates ecel file from list of rows added to row_data using right click option in the grid"""
        print("excel to be created from data :", self.row_data)
        if len(self.row_data) < 1:
            print("No row selected to print Excel sheet for")
            dlg = wx.MessageDialog(self, 'Please select at least one row to create Excel sheet', 'No Data...')
            if dlg.ShowModal() == wx.ID_OK:
                dlg.Destroy()
                return
        df = pd.DataFrame(data=self.row_data)

        dlg = wx.TextEntryDialog(self, 'Please enter Excel file name :', 'Excel File Name')
        dlg.SetValue("")
        if dlg.ShowModal() == wx.ID_OK:
            file_name = dlg.GetValue().lstrip()
            print('You entered: %s\n' % dlg.GetValue())
        else:
            file_name = ''
        dlg.Destroy()

        file = file_name + "_{}.xlsx".format(datetime.datetime.now().date().today())
        excel_file = "output\\" + file

        print(excel_file)

        df.to_excel(excel_file, index=False,
                    header=["REF", "PO #", "QTY", "MODEL", " SPECS", "EZ PN #"])
        print(df)
        # After printing excel file, it clears the row_data list so that new entries can be made to create next excel file
        self.row_data.clear()

    def get_icon(self, txt):
        add_itm = wx.Bitmap(wx.Image(add_item.GetImage()).ConvertToBitmap())
        retrn = wx.Bitmap(wx.Image(return_back.GetImage()).ConvertToBitmap())
        grps = wx.Bitmap(wx.Image(group_it.GetImage()).ConvertToBitmap())
        list_it = wx.Bitmap(wx.Image(listit.GetImage()).ConvertToBitmap())
        rej = wx.Bitmap(wx.Image(trash.GetImage()).ConvertToBitmap())
        delt = wx.Bitmap(wx.Image(delete_icon.GetImage()).ConvertToBitmap())
        prnt = wx.Bitmap(wx.Image(printer.GetImage()).ConvertToBitmap())
        pdf_icon = wx.Bitmap(wx.Image(pdf.GetImage()).ConvertToBitmap())
        discon_icon = wx.Bitmap(wx.Image(discontinue.GetImage()).ConvertToBitmap())
        Excel_icon = wx.Bitmap(wx.Image(excel_png.GetImage()).ConvertToBitmap())

        icns = {
            "Group": grps,
            "List": list_it,
            "Reject": rej,
            "Delete": delt,
            "Print": prnt,
            "Pdf": pdf_icon,
            "Return": retrn,
            "Add": add_itm,
            "discontinued": discon_icon,
            "Excel": Excel_icon,
            "Archive": grps,
        }
        return icns[txt]

    def discontinue_viewer(self, event):
        viewer = discont.DiscontinuedViewer(self)
        viewer.ip = self.ip
        viewer.user = self.user
        viewer.db = self.db
        viewer.password = self.password
        viewer.bins = self.bins
        print(viewer.ip, viewer.user, viewer.password, viewer.db)
        viewer.on_load_grid()

    def search_inv(self, event):
        """ opens up the search gui frame that shows the current inventory"""
        frm = inv.Search_Inventory_items(self)
        frm.set_window_size()
        frm.ip = self.ip
        frm.user = self.user
        frm.password = self.password
        frm.db = self.db
        frm.bins = self.bins
        frm.loggedin_user_id = self.loggedin_user_id
        frm.loggedin_user_username = self.loggedin_user
        frm.loggedin_user_is_manager = self.loggedin_user_is_manager
        frm.loggedin_user_is_active = self.loggedin_user_is_active
        frm.loggedin_user_is_tier2 = self.loggedin_user_is_tier2
        frm.loggedin_user_is_tier3 = self.loggedin_user_is_tier3
        frm.loggedin_user_first_name = self.loggedin_user_first_name
        frm.loggedin_user_last_name = self.loggedin_user_last_name
        frm.search_unsold(event=wx.EVT_BUTTON)
        frm.Show()
        frm.m_textCtrl_search_bar.SetFocus()

    def addlog(self, msg):
        """
        :param msg: Adds log entries
        :return:
        """
        self.program_log = self.program_log + msg + "\n"

    def show_log(self, event):
        """Shows log entries"""
        dlg = MyTextEntryDialog(self, 'Program logs', 'Here are the saved log enteries')
        dlg.SetValue(self.program_log)

        if dlg.ShowModal() == wx.ID_OK:
            dlg.Destroy()

    def add_barcode(self, barcode_txt, src_pdf, rect=(270, 0, 370, 210)):
        """
        :param barcode_txt: add barcode to an existing pdf file at a specific location
        :param src_pdf:
        :param rect:
        :return:
        """
        self.addlog("Text received for encoding barcode : {}".format(barcode_txt))
        src_pdf_filename = src_pdf
        self.addlog("Source pdf file name : " + src_pdf_filename)
        self.addlog("Entering code for barcode image file generation")

        code128.image(barcode_txt).save("generated_barcode.png")  # with PIL present
        self.addlog("barcode created")

        img_rect = fitz.Rect(rect)
        document = fitz.open(src_pdf_filename)

        # We'll put image on first page only but you could put it elsewhere
        page = document[0]
        file_name = os.path.abspath('generated_barcode.png')
        page.insert_image(img_rect, filename=file_name)

        self.addlog("barcode image inserted on pdf page")
        document.saveIncr()
        self.addlog("pdf incremental save command executed")
        document.close()
        self.addlog("pdf document closed")
        self.addlog("rv file like object is closed")
        self.addlog("barcoded pdf saved")
        if os.path.exists(file_name):
            os.remove(file_name)
            self.addlog("deleted generated_barcode.png")
        else:
            print("The barcode_img file does not exist")

    def infinite_sequence(self):
        """Generates a series of numbers starting from 0 and returns next number one level up whenever it is called"""
        num = 0
        while True:
            yield num
            num += 1

    def sort_by_this_column(self, event):
        """
        Sort the columns when column head is clicked
        :param event:
        :return:
        """
        db_fields = ['sheet_id', 'date_submitted', 'item_price_researched', "", "", "", 'model_no']
        col_ind = [0, 1, 2, 6]
        field = ''
        ord = 'DESC'
        col = event.GetCol()
        self.clicks.append(1)
        if len(self.clicks) % 2 == 0:
            ord = 'DESC'
        else:
            ord = 'ASC'
        print(event.GetCol())
        if event.GetCol() in col_ind:
            field = db_fields[event.GetCol()]
        else:
            field = 'sheet_id'
        self.addlog("Logged-in user & ID = " + self.loggedin_user + "  " + str(self.loggedin_user_id))
        print("Logged-in user & ID = ", self.loggedin_user, self.loggedin_user_id)
        if not self.loggedin_user_is_manager:
            self.m_button_user_management.Hide()
            qry1 = "SELECT * FROM ConfigSheet WHERE (tech_id = {} AND new = True AND listed = False AND rejected = False AND is_archived = False) ORDER BY {} {} LIMIT 9999".format(
                self.loggedin_user_id, field, ord)
            qry2 = "SELECT * FROM ConfigSheet WHERE (tech_id = {} AND new = False AND listed = True AND rejected = False AND is_archived = False) ORDER BY {} {} LIMIT 9999".format(
                self.loggedin_user_id, field, ord)
            qry3 = "SELECT * FROM ConfigSheet WHERE (tech_id = {} AND new = False AND listed = False AND rejected = True AND is_archived = False) ORDER BY {} {} LIMIT 9999".format(
                self.loggedin_user_id, field, ord)
            qry = [qry1, qry2, qry3]
            grids = [self.m_grid_new, self.m_grid_listed, self.m_grid_rejected]
        else:
            self.m_button_user_management.Show()
            qry1 = "SELECT * FROM ConfigSheet WHERE (new = True AND listed = False AND rejected = False AND is_archived = False) ORDER BY {} {} LIMIT 9999".format(
                field, ord)
            qry2 = "SELECT * FROM ConfigSheet WHERE (new = False AND listed = True AND rejected = False AND is_archived = False) ORDER BY {} {} LIMIT 9999".format(
                field, ord)
            qry3 = "SELECT * FROM ConfigSheet WHERE (new = False AND listed = False AND rejected = True AND is_archived = False) ORDER BY {} {} LIMIT 9999".format(
                field, ord)

            qry = [qry1, qry2, qry3]
            grids = [self.m_grid_new, self.m_grid_listed, self.m_grid_rejected]
        val = ''
        self.load_data(qry, grids, val)

    def new_cell_right_clicked(self, event):
        """
        Logic for context menu that appears when a cell in new tab is right clicked
        :param event:
        :return:
        """

        print("new cell right clicked")
        print("Logged-in user & ID = ", self.loggedin_user, self.loggedin_user_id)
        self.sh_id = str(self.m_grid_new.GetCellValue(event.GetRow(), 0))
        self.model_selected = str(self.m_grid_new.GetCellValue(event.GetRow(), 5).lstrip())
        qtty = str(self.m_grid_new.GetCellValue(event.GetRow(), 3)).split('\t')

        def get_po(po):
            x = None
            if po:
                if ' ' in po and ',' in po:
                    try:
                        x = po.split(',')
                    except Exception as e:
                        print(e)
                        print("Can not split for some reason. String has both space and comma")
                else:
                    if ' ' in po:
                        try:
                            x = po.split(' ')
                        except Exception as e2:
                            print(e2)
                    elif ',' in po:
                        try:
                            x = po.split(',')
                        except Exception as e:
                            print(e)
                    else:
                        x = po
            else:
                x = ''

            print(type(po), x)
            y = ['\'', ]
            if type(x) == list:
                for i in x:
                    y.append(i + '\n')
                return " ".join(y)
            else:
                return x

        po_for_excel = get_po(self.m_grid_new.GetCellValue(event.GetRow(), 7))
        print(po_for_excel)

        def get_qty(qty):
            out = qty.split('\t')[0]
            print(type(out), out)
            return int(out)

        def refined_title(title):
            stopwords = ['CORE', 'Core', 'RAM', 'Ram', 'DDR3', 'MacOS', 'MACOS', 'MACBOOK', 'IMAC', 'MAC', 'MINI',
                         'AIR', 'PRO', 'APPLE', 'APLLE', 'MacBook', 'iMac', 'Mac', 'Mini', 'Air', 'Pro', 'Apple',
                         self.m_grid_new.GetCellValue(event.GetRow(), 5)]
            titlewords = title.split()
            resultwords = [w for w in titlewords if w not in stopwords]
            result = '-'.join(resultwords)

            rslt = result.replace("with", '==>')
            rsl = rslt.replace("w/", "==>")
            print(rsl)
            return rsl

        values = {
            "sheet_id": int(self.m_grid_new.GetCellValue(event.GetRow(), 0)),
            "po": po_for_excel,
            "qty": get_qty(self.m_grid_new.GetCellValue(event.GetRow(), 3)),
            "model": self.m_grid_new.GetCellValue(event.GetRow(), 5),
            "title": refined_title(self.m_grid_new.GetCellValue(event.GetRow(), 6)),
            "EZ Part #": "",
        }
        self.row_data.append(values)
        try:
            if qtty[1] == ' lot' or qtty[1] == ' lots':
                self.qty_n = qtty[0]
            elif qtty[1] == ' unit' or qtty[1] == ' units':
                self.qty_n = qtty[0]
            else:
                self.qty_n = qtty[0]
        except Exception as e:
            print(e)
            self.qty_n = '0'
        print(self.sh_id, self.model_selected, self.qty_n)

        self.popupmenu = wx.Menu()
        if self.sh_id != '':

            if self.loggedin_user_is_manager:
                lst = ["Archive", "Excel", "Group", "List", "Reject", "Delete", "Print", "Pdf"]
            elif self.loggedin_user_is_tier2:
                lst = ["Delete", "Print", "Pdf"]
            else:
                lst = ["Excel", "Group", "List", "Delete", "Print", "Pdf"]

            for text in lst:
                item = self.popupmenu.Append(-1, "    " + text)
                item.SetBitmap(self.get_icon(text))

                self.Bind(wx.EVT_MENU, self.OnPopupItemSelected, item)
            # print(item)
            self.bookpanel_new.Bind(wx.EVT_CONTEXT_MENU, self.OnShowPopup_new)
            if platform.system() == 'Darwin':
                self.OnShowPopup_new(event=event)
        else:
            print('No sheet selected')
            dlg = wx.MessageDialog(self, "No sheet found. Please try again.", "Error",
                                   wx.ICON_ERROR)
            if dlg.ShowModal() == wx.ID_OK:
                dlg.Destroy()
            return
            # if not self.loggedin_user_is_manager:
            #     lst = ["Group", "List", "Delete", "Print", "Pdf"]
            # else:
            #     lst = ["Group", "List", "Reject", "Delete", "Print", "Pdf"]
            # for text in lst:
            #     item = self.popupmenu.Append(-1, "    " + text)
            #     item.SetBitmap(self.get_icon(text))
            #     item.Enable(False)
            #     self.Bind(wx.EVT_MENU, self.OnPopupItemSelected, item)
            # self.bookpanel_new.Bind(wx.EVT_CONTEXT_MENU, self.OnShowPopup_new)
            # if platform.system() == 'Darwin':
            #     self.OnShowPopup_new(event=event)

    def OnShowPopup_new(self, event):
        """
        logic for what will happen when context menu item is clicked in new tab only
        :param event:
        :return:
        """
        pos1 = event.GetPosition()
        if platform.system() == 'Darwin':
            x, y = pos1
            print("x = ", x, "y = ", y)
            pos = self.bookpanel_new.ScreenToClient(x + 170, y + 170)
        elif platform.system() == 'Windows':
            pos = self.bookpanel_new.ScreenToClient(pos1)
        else:
            print(platform.system())

        self.bookpanel_new.PopupMenu(self.popupmenu, pos)

    def OnShowPopup_listed(self, event):
        """
        logic for what will happen when context menu item is clicked in listed tab only
        :param event:
        :return:
        """
        pos1 = event.GetPosition()
        if platform.system() == 'Darwin':
            x, y = pos1
            print("x = ", x, "y = ", y)
            pos = self.bookpanel_listed.ScreenToClient(x + 170, y + 170)
        elif platform.system() == 'Windows':
            pos = self.bookpanel_listed.ScreenToClient(pos1)
        else:
            print(platform.system())

        self.bookpanel_listed.PopupMenu(self.popupmenu, pos)

    def OnShowPopup_rejected(self, event):
        """
        logic for what will happen when context menu item is clicked in listed tab only
        :param event:
        :return:
        """
        pos1 = event.GetPosition()
        if platform.system() == 'Darwin':
            x, y = pos1
            print("x = ", x, "y = ", y)
            pos = self.bookpanel_rejected.ScreenToClient(x + 170, y + 170)
        elif platform.system() == 'Windows':
            pos = self.bookpanel_rejected.ScreenToClient(pos1)
        else:
            print(platform.system())

        self.bookpanel_rejected.PopupMenu(self.popupmenu, pos)

    def get_ez(self):
        """
        Presents a dialogbox to get ez part number from user
        :return:
        """
        dlg = wx.TextEntryDialog(self, 'Please enter ez part number', 'Part# Required')
        dlg.SetValue("")
        if dlg.ShowModal() == wx.ID_OK:
            ez = dlg.GetValue().lstrip()
            print('You entered: %s\n' % dlg.GetValue())
        else:
            ez = ''
        dlg.Destroy()
        return ez

    def OnPopupItemSelected(self, event):

        """
        Logic for actions of each item clicked in context menu in both new and listed tabs
        :param event:
        :return:
        """
        item = self.popupmenu.FindItemById(event.GetId())
        text_clicked = item.GetItemLabel()
        print(item, text_clicked)

        if text_clicked == "    Add":
            print("Add selected")
            dlg = wx.TextEntryDialog(self, 'Enter bin number', 'Location')
            dlg.SetValue("")
            if dlg.ShowModal() == wx.ID_OK:
                print('You entered: %s\n' % dlg.GetValue())
                resp = dlg.GetValue().lstrip()
                dlg.Destroy()
                if resp.upper() in self.bins:
                    data = self.data_selected_sheet
                    print(data)
                    if data:
                        # Connect to the database
                        cursor = pymysql.cursors.DictCursor
                        connection = pymysql.connect(host=self.ip,
                                                     user=self.user,
                                                     password=self.password,
                                                     db=self.db,
                                                     charset='utf8mb4',
                                                     cursorclass=cursor)
                        try:
                            with connection.cursor() as cursor:
                                """find if record already exists for this item id number"""
                                sql = "SELECT * FROM item_to_bin WHERE item_id='{}'".format(data['itms'][0])
                                cursor.execute(sql)

                                # gets the number of rows returned by database for the above sql command
                                row_count = cursor.rowcount

                                # row_count = 0
                                print("number of rows returned by database for this item: {}".format(row_count))

                                if row_count == 0:
                                    """Create a new record if no previous record found"""

                                    items_list = data['itms']
                                    print("List of items = ", items_list)
                                    for i in items_list:
                                        if i != '':  # Filter out empty items from SN list and add all SN to the table
                                            item_id = i
                                            tech_sql = "INSERT INTO `item_to_bin` (date_added, bin_number, item_id, sheet_id, ez_no, added_by) VALUES (%s, %s, %s, %s, %s, %s)"
                                            tech_val = (data['date_today'],
                                                        resp.upper(),
                                                        i,
                                                        data['sht_id'],
                                                        data['ez_no'],
                                                        data['username'],
                                                        )
                                            cursor.execute(tech_sql, tech_val)

                                            # connection is not autocommit by default.So you must commit to save
                                            # your changes.
                                            connection.commit()
                                            print('Connection committed')
                                        else:
                                            print("Empty items found in SN list")
                                    txt = "All items in sheet {} are successfully added to bin#  {}".format(
                                        data['sht_id'],
                                        data['bin_no'])
                                    print(txt)
                                else:
                                    d = cursor.fetchall()[0]
                                    # print(d)
                                    msg1 = "This item {} with EZ # {} is already placed in bin # {}".format(
                                        data['itms'][0],
                                        data['ez_no'],
                                        d['bin_number'])
                                    wx.MessageBox(msg1, "STOP!",
                                                  wx.OK | wx.ICON_STOP, )


                        except pymysql.err.OperationalError as error:
                            print(error)

                        finally:
                            connection.close()
                    else:
                        print("Some data is missing")
                else:
                    print("this bin number does not exist")
                    wx.MessageBox("This bin number does not exist", "Error!",
                                  wx.OK | wx.ICON_ERROR, )
                    return
            self.on_load_grid()

        elif text_clicked == "    Archive":
            dlg = wx.MessageDialog(self, "This will archive the sheet. Do you want to proceed?", "Caution", wx.YES_NO | wx.ICON_QUESTION)

            result = dlg.ShowModal() == wx.ID_YES
            dlg.Destroy()
            print(result)

            if result:
                sql_lst = "UPDATE `ConfigSheet` SET is_archived = True, date_archived = %s WHERE sheet_id = %s"
                val_lst = (self.today, self.sh_id)
                print('sheet = ', self.sh_id)
                cursor = pymysql.cursors.DictCursor
                connection = pymysql.connect(host=self.ip,
                                             user=self.user,
                                             password=self.password,
                                             db=self.db,
                                             charset='utf8mb4',
                                             cursorclass=cursor)
                try:
                    with connection.cursor() as cursor:
                        # if self.loggedin_user_is_manager:
                        cursor.execute(sql_lst, val_lst)
                        connection.commit()

                        # Some things that are done to the form after the submission of data to database
                        print('Connection committed')

                        # msg = "Config Sheet {} successfully marked as listed".format(self.sh_id)
                        # abc = wx.MessageBox(msg, "Success!",
                        #                     wx.OK | wx.ICON_INFORMATION, )
                        self.refresh()

                except pymysql.err.OperationalError as error:
                    print(error)
                finally:
                    connection.close()
            else:
                dlg = wx.MessageDialog(self, 'No changes made', 'Archive', wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()
                dlg.Destroy()
                return

        elif text_clicked == "    Group":
            if not self.loggedin_user_is_manager:

                qry1 = "SELECT * FROM ConfigSheet WHERE (tech_id = {} AND new = True AND listed = False AND rejected = False AND is_archived = False AND model_no = {}) ORDER BY sheet_id ASC LIMIT 9999".format(
                    self.loggedin_user_id, self.model_selected)
                qry2 = "SELECT * FROM ConfigSheet WHERE (tech_id = {} AND new = False AND listed = True AND rejected = False AND is_archived = False AND model_no = {}) ORDER BY sheet_id ASC LIMIT 9999".format(
                    self.loggedin_user_id, self.model_selected)
                qry3 = "SELECT * FROM ConfigSheet WHERE (tech_id = {} AND new = False AND listed = False AND rejected = True AND is_archived = False AND model_no = {}) ORDER BY sheet_id ASC LIMIT 9999".format(
                    self.loggedin_user_id, self.model_selected)
                qry = [qry1, qry2, qry3]
                grids = [self.m_grid_new, self.m_grid_listed, self.m_grid_rejected]
            else:

                qry1 = "SELECT * FROM ConfigSheet WHERE (new = True AND listed = False AND rejected = False AND AND is_archived = False model_no = '{}') ORDER BY sheet_id ASC LIMIT 9999".format(
                    self.model_selected)
                qry2 = "SELECT * FROM ConfigSheet WHERE (new = False AND listed = True AND rejected = False AND AND is_archived = False model_no = '{}') ORDER BY sheet_id ASC LIMIT 9999".format(
                    self.model_selected)
                qry3 = "SELECT * FROM ConfigSheet WHERE (new = False AND listed = False AND rejected = True AND is_archived = False AND model_no = '{}') ORDER BY sheet_id ASC LIMIT 9999".format(
                    self.model_selected)

                qry = [qry1, qry2, qry3]
                grids = [self.m_grid_new, self.m_grid_listed, self.m_grid_rejected]
            val = ''
            self.load_data(qry, grids, val)

        elif text_clicked == "    List":

            resp = self.get_ez()
            if resp != '':
                sql_lst = "UPDATE `ConfigSheet` SET ez_part_number = %s, listed = True, new = False, processed = True, date_listed = %s WHERE sheet_id = %s"
                val_lst = (resp.upper(), self.today, self.sh_id)
                print('sheet = ', self.sh_id)
                cursor = pymysql.cursors.DictCursor
                connection = pymysql.connect(host=self.ip,
                                             user=self.user,
                                             password=self.password,
                                             db=self.db,
                                             charset='utf8mb4',
                                             cursorclass=cursor)
                try:
                    with connection.cursor() as cursor:
                        # if self.loggedin_user_is_manager:
                        cursor.execute(sql_lst, val_lst)
                        connection.commit()

                        # Some things that are done to the form after the submission of data to database
                        print('Connection committed')

                        # msg = "Config Sheet {} successfully marked as listed".format(self.sh_id)
                        # abc = wx.MessageBox(msg, "Success!",
                        #                     wx.OK | wx.ICON_INFORMATION, )
                        self.refresh()

                except pymysql.err.OperationalError as error:
                    print(error)
                finally:
                    connection.close()
            else:
                dlg = wx.TextEntryDialog(self, 'Please enter ez part number', 'Part # Required')
                return

        elif text_clicked == "    Reject":
            sql_rej = "UPDATE `ConfigSheet` SET rejected = True, new = False, listed = False, processed = True, date_rejected = %s WHERE sheet_id = %s"
            val_rej = (self.today, self.sh_id)
            print('sheet = ', self.sh_id)
            cursor = pymysql.cursors.DictCursor
            connection = pymysql.connect(host=self.ip,
                                         user=self.user,
                                         password=self.password,
                                         db=self.db,
                                         charset='utf8mb4',
                                         cursorclass=cursor)
            try:
                with connection.cursor() as cursor:
                    # if self.loggedin_user_is_manager:
                    cursor.execute(sql_rej, val_rej)
                    connection.commit()

                    # Some things that are done to the form after the submission of data to database
                    print('Connection committed')

                    msg = "Config Sheet {} successfully marked as rejected".format(self.sh_id)
                    abc = wx.MessageBox(msg, "Success!",
                                        wx.OK | wx.ICON_INFORMATION, )
                    self.refresh()

            except pymysql.err.OperationalError as error:
                print(error)
            finally:
                connection.close()

        elif text_clicked == "    Delete":
            data_got = self.query_database(f"select * from `ConfigSheet` WHERE sheet_id={self.sh_id}")
            tech_id = int(data_got[0]['tech_id'])
            sql1 = "UPDATE ConfigSheet SET new = %s,listed=%s, rejected=%s,  is_deleted = %s WHERE sheet_id = %s"
            val1 = (False, False, False, True, self.sh_id)
            print('sheet = ', self.sh_id)
            print("logged in user id: ", self.loggedin_user_id)
            print("This sheet created by user id: ", tech_id)
            cursor = pymysql.cursors.DictCursor
            connection = pymysql.connect(host=self.ip,
                                         user=self.user,
                                         password=self.password,
                                         db=self.db,
                                         charset='utf8mb4',
                                         cursorclass=cursor)
            try:
                with connection.cursor() as cursor:
                    if self.loggedin_user_is_manager or self.loggedin_user_id == tech_id:
                        cursor.execute(sql1, val1)
                        connection.commit()

                        # Some things that are done to the form after the submission of data to database
                        print('Connection committed')
                        msg = "Config Sheet {} successfully marked as deleted".format(self.sh_id)
                        wx.MessageBox(msg, "Success!",wx.OK | wx.ICON_INFORMATION, )
                        self.refresh()
                    else:
                        wx.MessageBox("Only original creator or manager can delete a config sheet", "Stop!",
                                      wx.OK | wx.ICON_ERROR, )


            except pymysql.err.OperationalError as error:
                print(error)
            finally:
                connection.close()

        elif text_clicked == "    Print":
            if os.path.exists(self.configsheet_file_produced_path):
                os.remove(self.configsheet_file_produced_path)
            else:
                print("The file does not exist")
            frm = gui.MyConfigSheet(self)
            frm.ip = self.ip
            frm.user = self.user
            frm.db = self.db
            frm.password = self.password
            frm.bins = self.bins
            frm.to_email = self.to_email
            frm.create_pdf_on_right_click(self.sh_id)
            self.add_barcode(self.sh_id + "-" + self.qty_n, self.configsheet_file_produced_path)

            if platform.system() == 'Darwin':
                cmd_open = """open \output\Ebay\ Config\ Sheet\ Rev1.5.pdf"""  # open pdf file in default pdf reader
                cmd_del = """rm - rf output.pdf"""
                self.runcommand(cmd_open)
                # self.runcommand(cmd_del)
            elif platform.system() == 'Windows':
                cmd_open = 'start Acrobat.exe /t "{}"'.format(
                    self.configsheet_file_produced_path)  # open pdf file in Acrobat pdf reader ( must be installed on windows already) and prints it and closes pdf reader
                # cmd_open = """start Acrobat.exe "Ebay Config Sheet Rev1.5.pdf"""""  # open pdf file in Acrobat pdf reader ( must be installed on windows already)
                self.runcommand(cmd_open)
            else:
                print(platform.system())

        elif text_clicked == "    Pdf":
            frm = gui.MyConfigSheet(self)
            frm.ip = self.ip
            frm.user = self.user
            frm.db = self.db
            frm.password = self.password
            frm.bins = self.bins
            frm.to_email = self.to_email
            frm.create_pdf_on_right_click(self.sh_id)
            self.addlog("pdf created, now adding barcode to it.")
            self.add_barcode(self.sh_id + "-" + self.qty_n, self.configsheet_file_produced_path)
            self.addlog("Add barcode command finished.")
            if os.path.exists(self.configsheet_file_produced_path):
                outpath = ("_{}.pdf".format(next(self.gen))).join(self.configsheet_file_produced_path.split('.pdf'))
                os.rename(self.configsheet_file_produced_path, outpath)
            else:
                print("The file does not exist")

        elif text_clicked == "    Return":
            if self.data_selected_sheet['bin_no'] == '':
                # sql1 = "UPDATE ConfigSheet SET processed = %, new = %s,  listed = %s WHERE sheet_id = %s"
                sql1 = "UPDATE `ConfigSheet` SET ez_part_number = '', listed = False, new = True, processed = False, rejected = False WHERE sheet_id = %s"
                val1 = (self.sh_id)
                print('sheet = ', self.sh_id)
                cursor = pymysql.cursors.DictCursor
                connection = pymysql.connect(host=self.ip,
                                             user=self.user,
                                             password=self.password,
                                             db=self.db,
                                             charset='utf8mb4',
                                             cursorclass=cursor)
                try:
                    with connection.cursor() as cursor:
                        if self.loggedin_user_is_manager:
                            cursor.execute(sql1, val1)
                            connection.commit()

                            # Some things that are done to the form after the submission of data to database
                            print('Connection committed')

                            msg = "Config Sheet {} successfully returned to new configsheet tab".format(self.sh_id)
                            abc = wx.MessageBox(msg, "Success!",
                                                wx.OK | wx.ICON_INFORMATION, )
                            self.refresh()

                except pymysql.err.OperationalError as error:
                    print(error)
                finally:
                    connection.close()
            else:
                dlg = wx.MessageDialog(self, "Please remove it from bin number first and then try again", "Stop",
                                       wx.ICON_STOP)
                if dlg.ShowModal() == wx.ID_OK:
                    dlg.Destroy()

        elif text_clicked == "    Excel":
            print("Excel Clicked")

            print(self.row_data)

    def runcommand(self, cmd):
        '''this function runs terminal commands in the background, which are given to it as input when it is called'''
        getcore = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        out, err = getcore.communicate()  # type: (str, str)
        if err:
            print(err)
        return out

    def query_database(self, qry):
        cursor = pymysql.cursors.DictCursor
        conn = pymysql.connect(host=self.ip,
                               user=self.user,
                               password=self.password,
                               db=self.db,
                               charset='utf8mb4',
                               cursorclass=cursor)

        try:
            with conn.cursor() as cur:
                cur.execute(qry)
                data = cur.fetchall()

        except pymysql.err.OperationalError as error:
            print(error)
            # wx.MessageBox("No connection to the database.", "Error!", wx.ICON_ERROR)
        finally:
            conn.close()
        return data

    def listed_cell_right_clicked(self, event):
        """"
        Logic for context menu that appears when a cell in listed tab is right clicked
        :param event:
        :return:
        """
        event.Skip()
        print("listed cell right clicked")
        #
        print("Logged-in user & ID = ", self.loggedin_user, self.loggedin_user_id)
        self.sh_id = str(self.m_grid_listed.GetCellValue(event.GetRow(), 0))
        self.model_selected = str(self.m_grid_listed.GetCellValue(event.GetRow(), 7).lstrip())
        qtty = str(self.m_grid_listed.GetCellValue(event.GetRow(), 4)).split('\t')
        try:
            if qtty[1] == ' lot' or qtty[1] == ' lots':
                self.qty_n = qtty[0]
            elif qtty[1] == ' unit' or qtty[1] == ' units':
                self.qty_n = qtty[0]
            else:
                self.qty_n = qtty[0]
        except Exception as e:
            print(e)
            print("field is empty")
            self.qty_n = '0'
        print(self.sh_id, self.model_selected, self.qty_n)
        dt = self.date_today
        ez = str(self.m_grid_listed.GetCellValue(event.GetRow(), 2).lstrip())
        us_name = self.loggedin_user.upper()
        sheet_id = self.m_grid_listed.GetCellValue(event.GetRow(), 0).lstrip()
        # itm_id = [ sheet_id + "-" + self.qty_n + "-" + str(i + 1) for i in range(int(self.qty_n)) ]
        try:
            sheet_detail = self.query_database(f'SELECT * from ConfigSheet WHERE sheet_id={sheet_id}')
            itm_id = sheet_detail[0]['item_sn_list'].split('\n')
            print("SN of items in this config sheet: ", itm_id)
        except Exception as e:
            print(e)
            return


        bin_n = self.m_grid_listed.GetCellValue(event.GetRow(), 3).lstrip().upper()
        self.data_selected_sheet = {
            'date_today': dt,
            'ez_no': ez.upper(),
            'sht_id': sheet_id,
            'qty': self.qty_n,
            'username': us_name,
            'itms': itm_id,
            'bin_no': bin_n,
        }

        self.popupmenu = wx.Menu()
        if self.sh_id != '':

            if self.loggedin_user_is_manager:
                lst = ["Archive", "Add", "Group", "Return", "Print", "Pdf"]
            elif not self.loggedin_user_is_tier2:
                lst = ["Add", "Group", "Print", "Pdf"]
            else:
                lst = ["Print", "Pdf"]
            for text in lst:
                item = self.popupmenu.Append(-1, "    " + text)
                item.SetBitmap(self.get_icon(text))
                self.Bind(wx.EVT_MENU, self.OnPopupItemSelected, item)
            self.bookpanel_listed.Bind(wx.EVT_CONTEXT_MENU, self.OnShowPopup_listed)
            if platform.system() == 'Darwin':
                self.OnShowPopup_listed(event=event)
        else:
            print('No sheet selected')
            dlg = wx.MessageDialog(self, "No sheet found. Please try again.", "Error",
                                   wx.ICON_ERROR)
            if dlg.ShowModal() == wx.ID_OK:
                dlg.Destroy()
            return
            # if not self.loggedin_user_is_manager:
            #     lst = ["Add", "Group", "Print", "Pdf"]
            # else:
            #     lst = ["Add", "Group", "Return", "Print", "Pdf"]
            # for text in lst:
            #     item = self.popupmenu.Append(-1, "    " + text)
            #     item.SetBitmap(self.get_icon(text))
            #     item.Enable(False)
            #     self.Bind(wx.EVT_MENU, self.OnPopupItemSelected, item)
            # self.bookpanel_listed.Bind(wx.EVT_CONTEXT_MENU, self.OnShowPopup_listed)
            # if platform.system() == 'Darwin':
            #     self.OnShowPopup_listed(event=event)

    def rejected_cell_right_clicked(self, event):
        """
                Logic for context menu that appears when a cell in rejected tab is right clicked
                :param event:
                :return:
                """
        event.Skip()
        print("rejected cell right clicked")
        """"
                Logic for context menu that appears when a cell in listed tab is right clicked
                :param event:
                :return:
                """
        event.Skip()
        print("Rejected cell right clicked")
        #
        print("Logged-in user & ID = ", self.loggedin_user, self.loggedin_user_id)
        self.sh_id = str(self.m_grid_rejected.GetCellValue(event.GetRow(), 0))
        self.model_selected = str(self.m_grid_rejected.GetCellValue(event.GetRow(), 5).lstrip())
        qtty = str(self.m_grid_rejected.GetCellValue(event.GetRow(), 3)).split('\t')
        try:
            if qtty[1] == ' lot' or qtty[1] == ' lots':
                self.qty_n = qtty[0]
            elif qtty[1] == ' unit' or qtty[1] == ' units':
                self.qty_n = qtty[0]
            else:
                self.qty_n = qtty[0]
        except Exception as e:
            print(e)
            self.qty_n = '0'
        print(self.sh_id, self.model_selected, self.qty_n)

        self.popupmenu = wx.Menu()
        if self.sh_id != '':

            if self.loggedin_user_is_manager:
                lst = ["Group", "Delete", "Print", "Pdf"]
            elif not self.loggedin_user_is_tier2:
                lst = ["Group", "Print", "Pdf"]
            else:
                lst = ["Print", "Pdf"]
            for text in lst:
                item = self.popupmenu.Append(-1, "    " + text)
                item.SetBitmap(self.get_icon(text))
                self.Bind(wx.EVT_MENU, self.OnPopupItemSelected, item)
            self.bookpanel_rejected.Bind(wx.EVT_CONTEXT_MENU, self.OnShowPopup_rejected)
            if platform.system() == 'Darwin':
                self.OnShowPopup_rejected(event=event)
        else:
            print('No sheet selected')
            dlg = wx.MessageDialog(self, "No sheet found. Please try again.", "Error",
                                   wx.ICON_ERROR)
            if dlg.ShowModal() == wx.ID_OK:
                dlg.Destroy()
            return
            # if not self.loggedin_user_is_manager:
            #     lst = ["Group", "Print", "Pdf"]
            # else:
            #     lst = ["Group", "Print", "Pdf"]
            # for text in lst:
            #     item = self.popupmenu.Append(-1, "    " + text)
            #     item.SetBitmap(self.get_icon(text))
            #     item.Enable(False)
            #     self.Bind(wx.EVT_MENU, self.OnPopupItemSelected, item)
            # self.bookpanel_rejected.Bind(wx.EVT_CONTEXT_MENU, self.OnShowPopup_rejected)
            # if platform.system() == 'Darwin':
            #     self.OnShowPopup_rejected(event=event)

    def new_cell_left_click(self, event):
        """
        Shows whole row as selected when any cell in a row is left clicked in new tab
        :param event:
        :return:
        """
        print("cell left clicked ")
        tab = event.EventObject.GetChildren()[event.Selection].GetName()
        print("you selected tab " + tab)
        self.m_grid_new.SelectRow(event.GetRow(), False)

    def listed_cell_left_click(self, event):
        """
                Shows whole row as selected when any cell in a row is left clicked in listed tab
                :param event:
                :return:
                """
        print("cell left clicked ")
        tab = event.EventObject.GetChildren()[event.Selection].GetName()
        print("you selected tab " + tab)
        self.m_grid_listed.SelectRow(event.GetRow(), False)

    def rejected_cell_left_click(self, event):
        """
                Shows whole row as selected when any cell in a row is left clicked in rejected tab
                :param event:
                :return:
                """
        print("cell left clicked ")
        tab = event.EventObject.GetChildren()[event.Selection].GetName()
        print("you selected tab " + tab)
        self.m_grid_rejected.SelectRow(event.GetRow(), False)

    def archived_cell_left_click(self, event):
        """
        Shows whole row as selected when any cell in a row is left clicked in new tab
        :param event:
        :return:
        """
        print("cell left clicked ")
        tab = event.EventObject.GetChildren()[event.Selection].GetName()
        print("you selected tab " + tab)
        self.m_grid_archived.SelectRow(event.GetRow(), False)

    def new_cell_clicked(self, event):
        print()

    def on_tab_change(self, event):
        """
        updates the counter when user switches tabs in the book
        :param event:
        :return:
        """
        event.Skip()
        # Works on Windows, Linux and Mac
        # current_page = self.m_notebook2.GetPage(event.GetSelection())
        tab = event.EventObject.GetChildren()[event.Selection].GetName()
        print("you selected tab " + tab)

        if tab == 'new_tab':
            try:
                qty_of_sheets = (4 - len(str(self.total_Number_of_rows_of_data_returned[0]))) * "0" + str(
                    self.total_Number_of_rows_of_data_returned[0])
                print(qty_of_sheets)
                # set text to status bar
                self.statusBar.SetStatusText(f"Number of sheets: {self.total_Number_of_rows_of_data_returned[0]}")
            except Exception as e:
                print(e)
                self.statusBar.SetStatusText(f"Number of sheets: 0")
        elif tab == 'listed_tab':
            try:
                self.statusBar.SetStatusText(f"Number of sheets: {self.total_Number_of_rows_of_data_returned[1]}")
            except Exception as e:
                print(e)
                self.statusBar.SetStatusText(f"Number of sheets: 0")
        elif tab == 'rejected_tab':
            try:
                self.statusBar.SetStatusText(f"Number of sheets: {self.total_Number_of_rows_of_data_returned[2]}")
            except Exception as e:
                print(e)
                self.statusBar.SetStatusText(f"Number of sheets: 0")
        elif tab == 'archived_tab':
            try:

                self.statusBar.SetStatusText(f"Number of sheets: {self.total_Number_of_rows_of_data_returned[3]}")
            except Exception as e:
                print(e)
                self.statusBar.SetStatusText(f"Number of sheets: 0")

    def call_login(self):
        """
        Calls for user to login
        :return:
        """
        print(self.loggedin_user)
        # Ask user to login
        if self.loggedin_user == '':
            dlg = login_edited.MyLogin(self)
            dlg.ip = self.ip
            dlg.user = self.user
            dlg.password = self.password
            dlg.db = self.db
            dlg.bins = self.bins
            dlg.Title = self.version_number
            dlg.ShowModal()
            authenticated = dlg.logged_in
            if not authenticated:
                self.Close()
            else:
                # print(dlg.data)
                self.loggedin_user = dlg.user_name
                self.loggedin_user_id = dlg.data[0][0]['user_id']
                self.loggedin_user_is_manager = dlg.data[0][0]['user_is_manager']
                self.loggedin_user_is_active = dlg.data[0][0]['user_is_active']
                self.loggedin_user_is_tier2 = dlg.data[0][0]['user_is_tier2']
                self.loggedin_user_is_tier3 = dlg.data[0][0]['user_is_tier3']
                self.loggedin_user_first_name = dlg.data[0][0]['first_name']
                self.loggedin_user_last_name = dlg.data[0][0]['last_name']
                # self.m_staticText_welcome.SetLabel(
                #     "   Welcome !\n\n" + self.loggedin_user_first_name + " " + self.loggedin_user_last_name)
                self.m_staticText_welcome.SetLabel(
                    "   Welcome " + self.loggedin_user_first_name.capitalize() + "!")
                # self.SetTitle("Dashboard - " + self.loggedin_user_first_name + " " + self.loggedin_user_last_name)
                self.m_button_logout.SetLabel("Logout")

                self.on_load_grid()
        else:
            print("Stop! You need to logout first before you can login as another user.")

    def __del__(self):
        pass

    def logout(self, event):
        """
        logic for logout
        :param event:
        :return:
        """
        self.m_searchCtrl1.SetValue("")
        self.clear_row_color(self.m_grid_listed.GetNumberRows())
        self.clear_row_color(self.m_grid_archived.GetNumberRows())
        event.Skip()
        self.loggedin_user = ''
        self.loggedin_user_id = ''
        self.loggedin_user_is_manager = False
        self.loggedin_user_is_active = False
        self.loggedin_user_is_tier2 = False
        self.loggedin_user_is_tier3 = False
        self.loggedin_user_first_name = ''
        self.loggedin_user_last_name = ''
        # self.SetTitle("Dashboard " + "")
        # self.m_staticText_welcome.SetLabel("\tPlease login")
        self.m_button_logout.SetLabel("Logged out")
        # self.m_staticText_new_sheet_qty.SetLabel("0000")
        self.statusBar.SetStatusText("Number of sheets: 0")
        self.m_grid_new.ClearGrid()
        self.m_grid_listed.ClearGrid()
        self.m_grid_rejected.ClearGrid()
        self.m_grid_archived.ClearGrid()
        self.call_login()

    def user_management(self, event):
        """
        Opens user management module from dashboard
        :param event:
        :return:
        """
        event.Skip()
        user_frame = user_management.UserManagement(self)
        user_frame.ip = self.ip
        user_frame.user = self.user
        user_frame.password = self.password
        user_frame.db = self.db
        user_frame.bins = self.bins
        user_frame.on_load_grid()
        user_frame.Show()

    def search(self, event):
        """
        Logic for search in the dashboard grid
        :param event:
        :return:
        """
        event.Skip()
        print("Logged in user : ", self.loggedin_user)
        val = '%' + str(
            self.m_searchCtrl1.GetValue().lstrip()) + '%'  # this value will make sure to show all names that have characters input by user
        if self.loggedin_user_is_tier2 or self.loggedin_user_is_tier3:
            qry1 = "SELECT * FROM `ConfigSheet` WHERE tech_id = {} AND new = True AND is_archived = False AND (sheet_id LIKE %s OR date_submitted LIKE %s OR title LIKE %s OR model_no LIKE %s OR ez_part_number LIKE %s) ORDER BY sheet_id DESC".format(
                self.loggedin_user_id)
            qry2 = "SELECT * FROM `ConfigSheet` WHERE tech_id = {} AND listed = True AND is_archived = False AND (sheet_id LIKE %s OR date_submitted LIKE %s OR title LIKE %s OR model_no LIKE %s OR ez_part_number LIKE %s) ORDER BY sheet_id DESC".format(
                self.loggedin_user_id)
            qry3 = "SELECT * FROM `ConfigSheet` WHERE tech_id = {} AND rejected = True AND is_archived = False AND (sheet_id LIKE %s OR date_submitted LIKE %s OR title LIKE %s OR model_no LIKE %s OR ez_part_number LIKE %s) ORDER BY sheet_id DESC".format(
                self.loggedin_user_id)
            qry4 = "SELECT * FROM `ConfigSheet` WHERE tech_id = {} AND is_archived = True AND (sheet_id LIKE %s OR date_submitted LIKE %s OR title LIKE %s OR model_no LIKE %s OR ez_part_number LIKE %s) ORDER BY sheet_id DESC".format(
                self.loggedin_user_id)

        else:
            qry1 = "SELECT * FROM `ConfigSheet` WHERE new = True AND is_archived = False AND (sheet_id LIKE %s OR date_submitted LIKE %s OR title LIKE %s OR model_no LIKE %s OR ez_part_number LIKE %s) ORDER BY sheet_id DESC"
            qry2 = "SELECT * FROM `ConfigSheet` WHERE listed = True AND is_archived = False AND (sheet_id LIKE %s OR date_submitted LIKE %s OR title LIKE %s OR model_no LIKE %s OR ez_part_number LIKE %s) ORDER BY sheet_id DESC"
            qry3 = "SELECT * FROM `ConfigSheet` WHERE rejected = True AND is_archived = False AND (sheet_id LIKE %s OR date_submitted LIKE %s OR title LIKE %s OR model_no LIKE %s OR ez_part_number LIKE %s) ORDER BY sheet_id DESC"
            qry4 = "SELECT * FROM `ConfigSheet` WHERE is_archived = True AND (sheet_id LIKE %s OR date_submitted LIKE %s OR title LIKE %s OR model_no LIKE %s OR ez_part_number LIKE %s) ORDER BY sheet_id DESC"
        qry = [qry1, qry2, qry3, qry4]
        val2 = (val, val, val, val, val)

        grids = [self.m_grid_new, self.m_grid_listed, self.m_grid_rejected, self.m_grid_archived]
        # print(val, val2)
        self.load_data(qry, grids, val2)

    def new_sheet(self, event):
        """
        Calls configsheet module with some default values preloaded
        :param event:
        :return:
        """
        event.Skip()
        new_frame = gui.MyConfigSheet(self)
        new_frame.ip = self.ip
        new_frame.user = self.user
        new_frame.password = self.password
        new_frame.db = self.db
        new_frame.bins = self.bins
        new_frame.to_email = self.to_email
        new_frame.loggedin_user_id = self.loggedin_user_id
        new_frame.loggedin_user_username = self.loggedin_user
        new_frame.loggedin_user_is_manager = self.loggedin_user_is_manager
        new_frame.loggedin_user_is_active = self.loggedin_user_is_active
        new_frame.loggedin_user_first_name = self.loggedin_user_first_name
        new_frame.loggedin_user_last_name = self.loggedin_user_last_name
        new_frame.load_form_with_defaults()
        new_frame.SetTitle("ezPro - New Configsheet")
        new_frame.m_textCtrl_defects.SetValue('SCRATCHES FROM NORMAL USE')
        new_frame.m_textCtrl_test_results.SetValue(
            """- UNIT IS TESTED TO POWER ON \n- \n- UNIT IS RESTORED TO FACTORY DEFAULTS\n- NO FURTHER TESTING DONE\n""")
        new_frame.m_button_create_new_from_it.Hide()
        if platform.system() == "Windows":
            # new_frame.adjust_configsheet()
            new_frame.set_window_size()
        new_frame.Show()

    def new_cell_double_clicked(self, event):
        """
        opens up the prefilled config sheet gui with specific sheet id taken when user double clicks any cell in a row
        :param event:
        :return:
        """

        print("new_cell_double_clicked")
        sheet_id = str(self.m_grid_new.GetCellValue(event.GetRow(), 0))
        print(event.GetCol())
        try:
            loaded_frame = gui.MyConfigSheet(self)
            loaded_frame.ip = self.ip
            print(loaded_frame.ip)
            loaded_frame.user = self.user
            loaded_frame.password = self.password
            loaded_frame.db = self.db
            loaded_frame.bins = self.bins
            loaded_frame.to_email = self.to_email
            loaded_frame.loggedin_user_id = self.loggedin_user_id
            loaded_frame.loggedin_user_username = self.loggedin_user
            loaded_frame.loggedin_user_is_manager = self.loggedin_user_is_manager
            loaded_frame.loggedin_user_is_active = self.loggedin_user_is_active
            loaded_frame.loggedin_user_first_name = self.loggedin_user_first_name
            loaded_frame.loggedin_user_last_name = self.loggedin_user_last_name
            loaded_frame.m_button_submit.Disable()
            loaded_frame.load_gui_form_from_database(sheet_id)
            loaded_frame.set_window_size()
            loaded_frame.SetTitle("ezPro - Configsheet ( # " + sheet_id + " )")
            loaded_frame.Show()
        except Exception as e:
            print(e)

    def archived_cell_double_clicked(self, event):
        """
                        opens up the prefilled config sheet gui with specific sheet id taken when user double clicks any cell in a row
                        :param event:
                        :return:
                        """
        print("archived_cell_double_clicked")
        sheet_id = str(self.m_grid_archived.GetCellValue(event.GetRow(), 0))

        print(sheet_id)

        if event.GetCol() == 2 or event.GetCol() == 3 or event.GetCol() == 4 or event.GetCol() == 5:
            ez_cell = str(self.m_grid_archived.GetCellValue(event.GetRow(), 2))
            print(ez_cell)
            if not self.loggedin_user_is_tier2 or self.loggedin_user_is_tier3:
                try:
                    frm = inv.Search_Inventory_items(self)
                    frm.set_window_size()
                    frm.ip = self.ip
                    frm.user = self.user
                    frm.password = self.password
                    frm.db = self.db
                    frm.bins = self.bins
                    frm.loggedin_user_id = self.loggedin_user_id
                    frm.loggedin_user_username = self.loggedin_user
                    frm.loggedin_user_is_manager = self.loggedin_user_is_manager
                    frm.loggedin_user_is_active = self.loggedin_user_is_active
                    frm.loggedin_user_first_name = self.loggedin_user_first_name
                    frm.loggedin_user_last_name = self.loggedin_user_last_name
                    sql = "SELECT * FROM item_to_bin WHERE ez_no LIKE %s ORDER BY bin_number ASC"
                    val = (ez_cell)
                    # Connect to the database
                    frm.load_grid(sql, val)
                    frm.Show()
                    frm.m_textCtrl_search_bar.SetFocus()
                except Exception as e:
                    print(e)
            else:
                print("Tier 2 Tech is not allowed to view the inventory status")
                pass

        else:

            try:
                archived_frame = gui.MyConfigSheet(self)
                archived_frame.ip = self.ip
                archived_frame.user = self.user
                archived_frame.password = self.password
                archived_frame.db = self.db
                archived_frame.bins = self.bins
                archived_frame.to_email = self.to_email
                archived_frame.loggedin_user_id = self.loggedin_user_id
                archived_frame.loggedin_user_id = self.loggedin_user_id
                archived_frame.loggedin_user_username = self.loggedin_user
                archived_frame.loggedin_user_is_manager = self.loggedin_user_is_manager
                archived_frame.loggedin_user_is_active = self.loggedin_user_is_active
                archived_frame.loggedin_user_first_name = self.loggedin_user_first_name
                archived_frame.loggedin_user_last_name = self.loggedin_user_last_name
                archived_frame.load_gui_form_from_database(sheet_id)
                archived_frame.set_window_size()
                archived_frame.SetTitle("ezPro - Configsheet ( # " + sheet_id + " )")
                archived_frame.m_button_submit.Disable()
                archived_frame.Show()
            except Exception as e:
                print(e)

    def listed_cell_double_clicked(self, event):
        """
                opens up the prefilled config sheet gui with specific sheet id taken when user double clicks any cell in a row
                :param event:
                :return:
                """
        print("listed_cell_double_clicked")
        sheet_id = str(self.m_grid_listed.GetCellValue(event.GetRow(), 0))

        print(sheet_id)
        if not self.loggedin_user_is_tier2:
            if event.GetCol() == 2 or event.GetCol() == 3 or event.GetCol() == 4 or event.GetCol() == 5:
                ez_cell = str(self.m_grid_listed.GetCellValue(event.GetRow(), 2))
                print(ez_cell)
                try:
                    frm = inv.Search_Inventory_items(self)
                    frm.set_window_size()
                    frm.ip = self.ip
                    frm.user = self.user
                    frm.password = self.password
                    frm.db = self.db
                    frm.bins = self.bins
                    frm.loggedin_user_id = self.loggedin_user_id
                    frm.loggedin_user_username = self.loggedin_user
                    frm.loggedin_user_is_manager = self.loggedin_user_is_manager
                    frm.loggedin_user_is_active = self.loggedin_user_is_active
                    frm.loggedin_user_first_name = self.loggedin_user_first_name
                    frm.loggedin_user_last_name = self.loggedin_user_last_name
                    sql = "SELECT * FROM item_to_bin WHERE ez_no LIKE %s ORDER BY bin_number ASC"
                    val = (ez_cell)
                    # Connect to the database
                    frm.load_grid(sql, val)
                    frm.Show()
                    frm.m_textCtrl_search_bar.SetFocus()
                except Exception as e:
                    print(e)
            else:

                try:
                    listed_frame = gui.MyConfigSheet(self)
                    listed_frame.ip = self.ip
                    listed_frame.user = self.user
                    listed_frame.password = self.password
                    listed_frame.db = self.db
                    listed_frame.bins = self.bins
                    listed_frame.to_email = self.to_email
                    listed_frame.loggedin_user_id = self.loggedin_user_id
                    listed_frame.loggedin_user_id = self.loggedin_user_id
                    listed_frame.loggedin_user_username = self.loggedin_user
                    listed_frame.loggedin_user_is_manager = self.loggedin_user_is_manager
                    listed_frame.loggedin_user_is_active = self.loggedin_user_is_active
                    listed_frame.loggedin_user_first_name = self.loggedin_user_first_name
                    listed_frame.loggedin_user_last_name = self.loggedin_user_last_name
                    listed_frame.load_gui_form_from_database(sheet_id)
                    listed_frame.set_window_size()
                    listed_frame.SetTitle("ezPro - Configsheet ( # " + sheet_id + " )")
                    listed_frame.Show()
                except Exception as e:
                    print(e)
        else:
            print("Tier 2 Tech is not allowed to view the inventory status")
            pass

    def rejected_cell_double_clicked(self, event):
        """
                opens up the prefilled config sheet gui with specific sheet id taken when user double clicks any cell in a row
                :param event:
                :return:
                """
        print("rejected_cell_double_clicked")
        sheet_id = str(self.m_grid_rejected.GetCellValue(event.GetRow(), 0))

        print(sheet_id)
        try:
            rejected_frame = gui.MyConfigSheet(self)
            rejected_frame.ip = self.ip
            rejected_frame.user = self.user
            rejected_frame.password = self.password
            rejected_frame.db = self.db
            rejected_frame.bins = self.bins
            rejected_frame.to_email = self.to_email
            rejected_frame.loggedin_user_id = self.loggedin_user_id
            rejected_frame.loggedin_user_username = self.loggedin_user
            rejected_frame.loggedin_user_is_manager = self.loggedin_user_is_manager
            rejected_frame.loggedin_user_is_active = self.loggedin_user_is_active
            rejected_frame.loggedin_user_first_name = self.loggedin_user_first_name
            rejected_frame.loggedin_user_last_name = self.loggedin_user_last_name
            rejected_frame.load_gui_form_from_database(sheet_id)
            rejected_frame.set_window_size()
            rejected_frame.SetTitle("ezPro - Configsheet ( # " + sheet_id + " )")
            rejected_frame.Show()
        except Exception as e:
            print(e)

    def load_data(self, query, grid, value):
        self.clear_row_color(self.m_grid_listed.GetNumberRows())
        self.clear_row_color(self.m_grid_archived.GetNumberRows())
        """
        Loads grid with values from database
        :param query:
        :param grid:
        :param value:
        :return:
        """
        # load item_to_bin table and find # of sold units per config sheet
        cursor = pymysql.cursors.DictCursor
        conn = pymysql.connect(host=self.ip,
                               user=self.user,
                               password=self.password,
                               db=self.db,
                               charset='utf8mb4',
                               cursorclass=cursor)

        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM item_to_bin")
                df = pd.DataFrame(cur.fetchall())  # .groupby(['sheet_id'])

        except pymysql.err.OperationalError as error:
            print(error)
            # wx.MessageBox("No connection to the database.", "Error!", wx.ICON_ERROR)
        finally:
            conn.close()
        try:
            sold_units = df[df['is_sold'] == True]['sheet_id'].value_counts()
            total_items_per_sheet = df['sheet_id'].value_counts()
        except:
            pass

        def get_percent_sold(i):
            if i in sold_units:
                # percent = (sold_units[i] / total_items_per_sheet[i]) * 100
                if sold_units[i] > 1:
                    sold_out = str(sold_units[i]) + " units"
                else:
                    sold_out = str(sold_units[i]) + " unit"
            else:
                # percent = 0
                sold_out = ''
            # return str('%g' % percent) + " %"
            return sold_out

        def get_bin_no(sh_id):
            try:
                bin_no = df[df['sheet_id'] == sh_id]['bin_number']
                print(bin_no.values[0])
                return bin_no.values[0]
            except:
                return ""

        self.total_Number_of_rows_of_data_returned = []
        qry = query
        grids = grid
        val = value
        print(qry, "\n", grids)
        self.m_grid_new.ClearGrid()
        self.m_grid_listed.ClearGrid()
        self.m_grid_rejected.ClearGrid()
        self.m_grid_archived.ClearGrid()
        # self.clear_row_color()
        i = 0

        while i < len(qry):
            print(i)
            # Connect to the database
            cursor = pymysql.cursors.DictCursor
            connection = pymysql.connect(host=self.ip,
                                         user=self.user,
                                         password=self.password,
                                         db=self.db,
                                         charset='utf8mb4',
                                         cursorclass=cursor)

            try:
                with connection.cursor() as cur:
                    if val != '':
                        cur.execute(
                            qry[i], val,
                        )
                        row_count = cur.rowcount
                        data = cur.fetchall()

                        self.total_Number_of_rows_of_data_returned.append(
                            len(data))  # stores total rows returned to variable

                        n = 0
                        r = 0
                    else:
                        cur.execute(
                            qry[i]
                        )
                        row_count = cur.rowcount
                        data = cur.fetchall()
                        # print(data)
                        self.total_Number_of_rows_of_data_returned.append(
                            len(data))  # stores total rows returned to variable
                        print("total rows returned to variable", self.total_Number_of_rows_of_data_returned[i])

                        n = 0
                        r = 0
                    # self.m_staticText_new_sheet_qty.SetLabel((4-len(str(self.total_Number_of_rows_of_data_returned[i])))*"0"+str(self.total_Number_of_rows_of_data_returned[i]))
                    while n < len(data) and r < row_count:
                        lst = data[n]
                        print("lst value :\n", lst)

                        if lst[u'new_sealed']:
                            classification = 'Sealed Box'
                        elif lst[u'new_open_box']:
                            classification = 'Open Box'
                        elif lst[u'used']:
                            classification = 'Used'
                        elif lst[u'seller_refurbished']:
                            classification = 'Refurb'
                        # print(grids[ i ])
                        grids[i].SetCellValue(r, 0, str(lst[u'sheet_id']))
                        if i == 0:
                            grids[i].SetCellValue(r, 1, str(lst[u'date_submitted']))
                        elif i == 1:
                            grids[i].SetCellValue(r, 1, str(lst[u'date_listed']))
                        elif i == 2:
                            grids[i].SetCellValue(r, 1, str(lst[u'date_rejected']))
                        else:
                            grids[i].SetCellValue(r, 1, str(lst[u'date_archived']))

                        if i not in (1, 3):
                            p = '%g' % lst[u'item_price_researched']  # converts e.g 10.0 into 10
                            grids[i].SetCellValue(r, 2, "$ " + str(p))
                        else:
                            grids[i].SetCellValue(r, 2, lst['ez_part_number'])
                        if i not in (1, 3):
                            if lst[u'sell_as_lot']:
                                if lst[u'number_of_lots'] > 1:
                                    x = ' lots'
                                else:
                                    x = ' lot'
                                itms_per_lot = str(lst['items_per_lot'])
                                grids[i].SetCellValue(r, 3, str(
                                    lst[u'number_of_lots']) + "\t" + x + " of " + itms_per_lot)
                            else:
                                if lst[u'number_of_items'] > 1:
                                    y = ' units'
                                else:
                                    y = ' unit'
                                grids[i].SetCellValue(r, 3, str(lst[u'number_of_items']) + "\t" + y)
                        else:
                            b_n = str(get_bin_no(lst[u'sheet_id']))
                            grids[i].SetCellValue(r, 3, b_n)
                            if b_n == '':
                                attr = grids[i].GetOrCreateCellAttr(r, 1)
                                if i != 3:
                                    attr.SetBackgroundColour(wx.Colour(255, 200, 20))
                                    grids[i].SetRowAttr(r, attr)
                                # grids[i].SetCellBackgroundColour(r, 3, "PINK")
                            if lst[u'sell_as_lot']:
                                if lst[u'number_of_lots'] > 1:
                                    x = ' lots'
                                else:
                                    x = ' lot'
                                itms_per_lot = str(lst['items_per_lot'])
                                grids[i].SetCellValue(r, 4, str(
                                    lst[u'number_of_lots']) + "\t" + x + " of " + itms_per_lot)
                            else:
                                if lst[u'number_of_items'] > 1:
                                    y = ' units'
                                else:
                                    y = ' unit'
                                grids[i].SetCellValue(r, 4, str(lst[u'number_of_items']) + "\t" + y)

                        if i not in (1, 3):
                            grids[i].SetCellValue(r, 4, classification)
                            grids[i].SetCellValue(r, 5, lst[u'model_no'])
                            grids[i].SetCellValue(r, 6, lst[u'title'])
                            grids[i].SetCellValue(r, 7, lst[u'po_number'])
                        else:
                            try:
                                perc = get_percent_sold(lst[u'sheet_id'])
                                grids[i].SetCellValue(r, 5, perc)
                                # attr = grids[i].GetOrCreateCellAttr(r, 4)
                                if perc == '100 %':
                                    attr = grids[i].GetOrCreateCellAttr(r, 1)
                                    attr.SetBackgroundColour(wx.Colour(113, 230, 113))
                                    grids[i].SetRowAttr(r, attr)

                                    # grids[i].SetCellBackgroundColour(r, 5, "GREEN")

                            except Exception as e:
                                print(e)
                                grids[i].SetCellValue(r, 5, '0 %')

                            grids[i].SetCellValue(r, 6, classification)
                            grids[i].SetCellValue(r, 7, lst[u'model_no'])
                            grids[i].SetCellValue(r, 8, lst[u'title'])
                            grids[i].SetCellValue(r, 9, lst[u'po_number'])

                        r = r + 1
                        n = n + 1

            except pymysql.err.OperationalError as error:
                print(error)
                # wx.MessageBox("No connection to the database.", "Error!", wx.ICON_ERROR)
            finally:
                connection.close()

            i += 1
            print(self.total_Number_of_rows_of_data_returned)
            try:
                # self.m_staticText_new_sheet_qty.SetLabel(
                #     (4 - len(str(self.total_Number_of_rows_of_data_returned[ 0 ]))) * "0" + str(
                #         self.total_Number_of_rows_of_data_returned[ 0 ]))
                self.statusBar.SetStatusText(f"Number of sheets: {self.total_Number_of_rows_of_data_returned[0]}")
            except Exception as e:
                print(e)
                # self.m_staticText_new_sheet_qty.SetLabel("0000")
                self.statusBar.SetStatusText("Number of sheets: 0")
        return len(data)

    def row_color(self, row_number, color):
        r = row_number
        # change row colors
        # attr = wx.grid.GridCellAttr()
        attr1 = self.m_grid_listed.GetOrCreateCellAttr(r, 1)
        attr2 = self.m_grid_archived.GetOrCreateCellAttr(r, 1)
        attr1.SetBackgroundColour(color)
        attr2.SetBackgroundColour(color)
        self.m_grid_listed.SetRowAttr(r, attr1)
        self.m_grid_archived.SetRowAttr(r, attr2)

    def clear_row_color(self, total_rows_in_grid):
        i = 0
        while i < total_rows_in_grid:
            self.row_color(i, "white")
            i = i + 1

    def on_load_grid(self):
        """
        creates queries to be used for loading grids in each tab
        :return:
        """
        print("on load grid user & ID = ", self.loggedin_user, self.loggedin_user_id)

        if self.loggedin_user_is_tier2:
            self.m_button_listed_excel_today.Hide()
            self.m_button_add_new_sheet.Show()
            self.m_button_home.Show()
            self.m_button_my_sheets_pdf_today.Hide()
            self.m_button_create_barcode.Hide()
            self.m_button_create_excel.Hide()
            self.m_button_user_management.Hide()
            self.m_button_show_log.Hide()
            self.m_button_all_sheets.Hide()
            self.m_button_search_inv.Hide()
            self.m_button_show_discontinue.Hide()
            qry1 = "SELECT * FROM ConfigSheet WHERE (tech_id = {} AND new = True AND listed = False AND rejected = False AND is_archived = False) ORDER BY sheet_id DESC LIMIT 9999".format(
                self.loggedin_user_id)
            qry2 = "SELECT * FROM ConfigSheet WHERE (tech_id = {} AND new = False AND listed = True AND rejected = False AND is_archived = False) ORDER BY sheet_id DESC LIMIT 9999".format(
                self.loggedin_user_id)
            qry3 = "SELECT * FROM ConfigSheet WHERE (tech_id = {} AND new = False AND listed = False AND rejected = True AND is_archived = False) ORDER BY sheet_id DESC LIMIT 9999".format(
                self.loggedin_user_id)
            qry4 = "SELECT * FROM ConfigSheet WHERE (tech_id = {} AND is_archived = True) ORDER BY sheet_id DESC LIMIT 9999".format(
                self.loggedin_user_id)
            qry = [qry1, qry2, qry3, qry4]
            grids = [self.m_grid_new, self.m_grid_listed, self.m_grid_rejected, self.m_grid_archived]
            val = ''
        elif self.loggedin_user_is_tier3:
            self.m_button_listed_excel_today.Hide()
            self.m_button_search_inv.Show()
            self.m_button_my_sheets_pdf_today.Hide()
            self.m_button_create_barcode.Hide()
            self.m_button_create_excel.Hide()
            self.m_button_user_management.Hide()
            self.m_button_show_log.Hide()
            self.m_button_all_sheets.Hide()
            self.m_button_add_new_sheet.Hide()
            self.m_button_home.Hide()
            self.m_button_show_discontinue.Hide()
            qry1 = "SELECT * FROM ConfigSheet WHERE (tech_id = {} AND new = True AND listed = False AND rejected = False AND is_archived = False) ORDER BY sheet_id DESC LIMIT 9999".format(
                self.loggedin_user_id)
            qry2 = "SELECT * FROM ConfigSheet WHERE (tech_id = {} AND new = False AND listed = True AND rejected = False AND is_archived = False) ORDER BY sheet_id DESC LIMIT 9999".format(
                self.loggedin_user_id)
            qry3 = "SELECT * FROM ConfigSheet WHERE (tech_id = {} AND new = False AND listed = False AND rejected = True AND is_archived = False) ORDER BY sheet_id DESC LIMIT 9999".format(
                self.loggedin_user_id)
            qry4 = "SELECT * FROM ConfigSheet WHERE (tech_id = {} AND is_archived = True) ORDER BY sheet_id DESC LIMIT 9999".format(
                self.loggedin_user_id)
            qry = [qry1, qry2, qry3, qry4]
            grids = [self.m_grid_new, self.m_grid_listed, self.m_grid_rejected, self.m_grid_archived]
            val = ''
        else:
            if self.loggedin_user_is_manager:
                self.m_button_user_management.Show()
                self.m_button_create_barcode.Show()



            else:
                self.m_button_user_management.Hide()
                self.m_button_create_barcode.Hide()
            self.m_button_listed_excel_today.Show()
            self.m_button_show_log.Show()
            self.m_button_my_sheets_pdf_today.Show()
            self.m_button_create_excel.Show()
            self.m_button_all_sheets.Show()
            self.m_button_home.Show()
            self.m_button_search_inv.Show()
            self.m_button_show_discontinue.Show()
            self.m_button_add_new_sheet.Show()

            qry1 = "SELECT * FROM ConfigSheet WHERE (tech_id = {} AND new = True AND listed = False AND rejected = False AND is_archived = False) ORDER BY sheet_id DESC LIMIT 9999".format(
                self.loggedin_user_id)
            qry2 = "SELECT * FROM ConfigSheet WHERE (tech_id = {} AND new = False AND listed = True AND rejected = False AND is_archived = False) ORDER BY sheet_id DESC LIMIT 9999".format(
                self.loggedin_user_id)
            qry3 = "SELECT * FROM ConfigSheet WHERE (tech_id = {} AND new = False AND listed = False AND rejected = True AND is_archived = False) ORDER BY sheet_id DESC LIMIT 9999".format(
                self.loggedin_user_id)
            qry4 = "SELECT * FROM ConfigSheet WHERE (tech_id = {} AND is_archived = True) ORDER BY sheet_id DESC LIMIT 9999".format(
                self.loggedin_user_id)
            qry = [qry1, qry2, qry3, qry4]
            grids = [self.m_grid_new, self.m_grid_listed, self.m_grid_rejected, self.m_grid_archived]
            val = ''

        self.load_data(qry, grids, val)

    def show_all_sheets(self, event):
        """
        shows data from all users instead of only logged in user in each grid in each tab
        :param event:
        :return:
        """
        event.Skip()
        self.m_searchCtrl1.SetValue("")
        qry1 = "SELECT * FROM ConfigSheet WHERE (new = True AND listed = False AND rejected = False AND is_archived = False) ORDER BY sheet_id DESC LIMIT 9999"
        qry2 = "SELECT * FROM ConfigSheet WHERE (new = False AND listed = True AND rejected = False AND is_archived = False) ORDER BY sheet_id DESC LIMIT 9999"
        qry3 = "SELECT * FROM ConfigSheet WHERE (new = False AND listed = False AND rejected = True AND is_archived = False) ORDER BY sheet_id DESC LIMIT 9999"
        qry4 = "SELECT * FROM ConfigSheet WHERE (is_archived = True) ORDER BY sheet_id DESC LIMIT 9999"
        qry = [qry1, qry2, qry3, qry4]
        grids = [self.m_grid_new, self.m_grid_listed, self.m_grid_rejected, self.m_grid_archived]
        val = ''
        self.load_data(qry, grids, val)

    def on_home(self, event):
        """
        loads only currently logged in users data in grid
        :param event:
        :return:
        """
        event.Skip()
        self.m_searchCtrl1.SetValue("")
        self.on_load_grid()

    def refresh(self):
        """This function is called form child sheets"""
        self.on_load_grid()


if __name__ == '__main__':
    app = wx.App(False)
    frame = MyDashboard(None)
    frame.call_login()
    frame.Show()
    frame.m_searchCtrl1.SetFocus()
    app.MainLoop()
