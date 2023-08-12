# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version 3.10.1-40-g8042f487)
# http://www.wxformbuilder.org/
#
# PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import os
import platform
import re
import smtplib
import subprocess
from datetime import datetime as dt
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pandas as pd

from ez_barcode_generator import MyEZBarcode as ezbar
import time
import code128
import fitz
import pdfrw
import pyautogui
import pygame.camera
import pymysql
import wx.xrc

from company_logo import *
from smbShare import SMBShare as smb


class MyTextEntryDialog(wx.Dialog):
    def __init__(self, parent, title, caption):
        style = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER
        super(MyTextEntryDialog, self).__init__(parent, -1, title, style=style)
        text = wx.StaticText(self, -1, caption)
        inpt = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE)
        inpt.SetInitialSize((400, 300))
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
        self.input.SetValue(value)

    def GetValue(self):
        return self.input.GetValue()


###########################################################################
## Class MyConfigSheet
###########################################################################

class MyConfigSheet(wx.Frame):
    date_today = str(dt.now().date())
    ip = ''  # IP address of the database server
    user = ''  # limited access username of the database
    password = ''  # limited access user's pw
    db = ''  # database name
    bins = []
    to_email = ''
    item_price_researched = 0.00  # item price default value
    sheetID = ''
    # list_it = False
    # reject_it = False

    loggedin_user_id = 0
    loggedin_user_username = ''
    loggedin_user_is_manager = False
    loggedin_user_is_active = False
    loggedin_user_first_name = ''
    loggedin_user_last_name = ''
    researched_item_price = 0.00

    tech_note = ''
    sn_of_items_tested = ''
    link_to_pics = ''
    processed = False
    bin_no = ''
    label_printed = False

    configsheet_template_file_path = os.path.abspath('.\\templates\Ebay Config Sheet Rev1.5_template.pdf')
    configsheet_file_produced_path = os.path.abspath('.\\output\Ebay Config Sheet Rev1.5.pdf')
    ezlabel_template_file_path = os.path.abspath('.\\templates\ez_label_sticker_template.pdf')
    ezlabel_file_produced_path = os.path.abspath('.\\output\ez_label_sticker.pdf')

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title="ezPro - Config Sheet", pos=wx.DefaultPosition,
                          size=wx.Size(1220, 720), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.logo_med = wx.Image(l_med.GetImage()).ConvertToBitmap()
        self.logo_lrg = wx.Image(l_lar.GetImage()).ConvertToBitmap()
        self.SetIcon(wx.Icon(self.logo_lrg))
        self.blue_color = wx.Colour(128, 212, 255)
        self.sold_as_individual = None
        self.lot_items_qty = None
        self.lots = None
        self.SetSizeHints(wx.DefaultSize, wx.Size(1220, 1180))

        bSizer1 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_panel2 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel2.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_panel4 = wx.Panel(self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), wx.TAB_TRAVERSAL)
        self.m_panel4.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        bSizer7.Add((0, 20), 0, wx.EXPAND, 5)

        self.m_bitmap1 = wx.StaticBitmap(self.m_panel4, wx.ID_ANY, wx.Bitmap(self.logo_lrg),
                                         wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.m_bitmap1, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer7.Add((0, 20), 0, 0, 5)
        # bSizer7.Add((0, 30), 1, wx.EXPAND, 5)

        self.m_button_add_note = wx.Button(self.m_panel4, wx.ID_ANY, u"Add Note", wx.DefaultPosition, wx.Size(130, -1),
                                           0)
        bSizer7.Add(self.m_button_add_note, 0, wx.ALIGN_CENTER | wx.ALL, 2)

        self.m_button_add_sn = wx.Button(self.m_panel4, wx.ID_ANY, u"Add SN #", wx.DefaultPosition, wx.Size(130, -1), 0)
        bSizer7.Add(self.m_button_add_sn, 0, wx.ALIGN_CENTER | wx.ALL, 2)

        self.m_button_add_researched_price = wx.Button(self.m_panel4, wx.ID_ANY, u"Add Price", wx.DefaultPosition,
                                                       wx.Size(130, -1), 0)
        bSizer7.Add(self.m_button_add_researched_price, 0, wx.ALIGN_CENTER | wx.ALL, 2)

        self.m_button_add_pics = wx.Button(self.m_panel4, wx.ID_ANY, u"Take Pics", wx.DefaultPosition, wx.Size(130, -1),
                                           0)
        bSizer7.Add(self.m_button_add_pics, 0, wx.ALIGN_CENTER | wx.ALL, 2)

        bSizer7.Add((0, 20), 0, wx.EXPAND, 5)

        self.m_button_list_it = wx.Button(self.m_panel4, wx.ID_ANY, u"List", wx.DefaultPosition, wx.Size(130, -1), 0)
        bSizer7.Add(self.m_button_list_it, 0, wx.ALIGN_CENTER | wx.ALL, 2)

        self.m_button_reject = wx.Button(self.m_panel4, wx.ID_ANY, u"Reject", wx.DefaultPosition, wx.Size(130, -1),
                                         0)
        bSizer7.Add(self.m_button_reject, 0, wx.ALIGN_CENTER | wx.ALL, 2)

        self.m_button_edit = wx.Button(self.m_panel4, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.Size(130, -1), 0)
        bSizer7.Add(self.m_button_edit, 0, wx.ALIGN_CENTER | wx.ALL, 2)
        bSizer7.Add((0, 20), 0, wx.EXPAND, 5)
        self.m_button_create_pdf = wx.Button(self.m_panel4, wx.ID_ANY, u"Create PDF", wx.DefaultPosition,
                                             wx.Size(130, -1), 0)
        bSizer7.Add(self.m_button_create_pdf, 0, wx.ALIGN_CENTER | wx.ALL, 2)

        self.m_button_print_ez_label = wx.Button(self.m_panel4, wx.ID_ANY, u"Print ez Label", wx.DefaultPosition,
                                                 wx.Size(130, -1), 0)
        bSizer7.Add(self.m_button_print_ez_label, 0, wx.ALIGN_CENTER | wx.ALL, 2)
        self.m_button_print_item_label = wx.Button(self.m_panel4, wx.ID_ANY, u"Print Labels", wx.DefaultPosition,
                                                   wx.Size(130, -1), 0)
        bSizer7.Add(self.m_button_print_item_label, 0, wx.ALIGN_CENTER | wx.ALL, 2)

        self.m_button_print = wx.Button(self.m_panel4, wx.ID_ANY, u"Print Sheet", wx.DefaultPosition, wx.Size(130, -1),
                                        0)
        bSizer7.Add(self.m_button_print, 0, wx.ALIGN_CENTER | wx.ALL, 2)

        self.m_button_email_pdf = wx.Button(self.m_panel4, wx.ID_ANY, u"Email Sheet", wx.DefaultPosition,
                                            wx.Size(130, -1),
                                            0)
        bSizer7.Add(self.m_button_email_pdf, 0, wx.ALIGN_CENTER | wx.ALL, 2)

        self.m_button_create_new_from_it = wx.Button(self.m_panel4, wx.ID_ANY, u"Create New", wx.DefaultPosition,
                                                     wx.Size(130, -1), 0)
        bSizer7.Add(self.m_button_create_new_from_it, 0, wx.ALIGN_CENTER | wx.ALL, 2)

        self.m_button_submit = wx.Button(self.m_panel4, wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.Size(130, -1), 0)
        bSizer7.Add(self.m_button_submit, 0, wx.ALIGN_CENTER | wx.ALL, 2)
        bSizer7.Add((0, 20), 0, wx.EXPAND, 5)

        self.m_button_update = wx.Button(self.m_panel4, wx.ID_ANY, u"Update", wx.DefaultPosition, wx.Size(130, -1), 0)
        bSizer7.Add(self.m_button_update, 0, wx.ALIGN_CENTER | wx.ALL, 2)

        self.m_panel4.SetSizer(bSizer7)
        self.m_panel4.Layout()
        bSizer7.Fit(self.m_panel4)
        bSizer4.Add(self.m_panel4, 0, wx.ALL | wx.EXPAND, 0)

        self.m_panel5 = wx.Panel(self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.Size(1050, -1), wx.TAB_TRAVERSAL)
        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        # self.m_panel5.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))

        self.m_scrolledWindow1 = wx.ScrolledWindow(self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.Size(1050, 800),
                                                   wx.BORDER_DEFAULT | wx.HSCROLL | wx.VSCROLL)
        self.m_scrolledWindow1.SetScrollRate(5, 5)
        self.m_scrolledWindow1.SetMaxSize(wx.Size(1050, 1080))

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        bSizer_top_row = wx.BoxSizer(wx.HORIZONTAL)

        bSizer_top_left = wx.BoxSizer(wx.VERTICAL)

        bSizer12 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText_ez_pn = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"EZ PART # :", wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.m_staticText_ez_pn.Wrap(-1)

        self.m_staticText_ez_pn.SetFont(
            wx.Font(13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande"))

        bSizer12.Add(self.m_staticText_ez_pn, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_ez_pn = wx.TextCtrl(self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.Size(170, -1), 0)
        bSizer12.Add(self.m_textCtrl_ez_pn, 0, wx.ALL, 5)

        bSizer_top_left.Add(bSizer12, 0, wx.EXPAND, 5)

        bSizer_top_left.Add((0, 40), 0, wx.EXPAND, 5)

        bSizer13 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText2 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"Evaluating Tech :", wx.DefaultPosition,
                                           wx.Size(110, -1), 0)
        self.m_staticText2.Wrap(-1)

        bSizer13.Add(self.m_staticText2, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_tech_name = wx.TextCtrl(self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                wx.Size(140, -1), 0)
        bSizer13.Add(self.m_textCtrl_tech_name, 0, wx.ALL, 5)

        bSizer_top_left.Add(bSizer13, 0, wx.EXPAND, 0)

        bSizer131 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText21 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"Date Received :", wx.DefaultPosition,
                                            wx.Size(110, -1), 0)
        self.m_staticText21.Wrap(-1)

        bSizer131.Add(self.m_staticText21, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_tech_date_received = wx.TextCtrl(self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString,
                                                         wx.DefaultPosition, wx.Size(140, -1), 0)
        bSizer131.Add(self.m_textCtrl_tech_date_received, 0, wx.ALL, 5)

        bSizer_top_left.Add(bSizer131, 0, wx.EXPAND, 0)

        bSizer_top_row.Add(bSizer_top_left, 1, wx.EXPAND, 5)

        bSizer_top_middle = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText35 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"ABC Company - eBay", wx.DefaultPosition,
                                            wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText35.Wrap(-1)

        self.m_staticText35.SetFont(
            wx.Font(18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande"))

        bSizer_top_middle.Add(self.m_staticText35, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText36 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"Config / Spec Sheet",
                                            wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText36.Wrap(-1)

        self.m_staticText36.SetFont(
            wx.Font(18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande"))

        bSizer_top_middle.Add(self.m_staticText36, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        #
        bSizer_top_middle.Add((0, 30), 0, wx.EXPAND, 5)
        self.m_staticText_msg = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.m_staticText_msg.Wrap(-1)
        self.m_staticText_msg.SetFont(
            wx.Font(13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande"))
        bSizer_top_middle.Add(self.m_staticText_msg, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.m_staticText_msg.SetForegroundColour(wx.Colour(176, 76, 176))
        #

        bSizer_top_row.Add(bSizer_top_middle, 1, wx.EXPAND, 5)

        bSizer_top_right = wx.BoxSizer(wx.VERTICAL)

        bSizer34 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText37 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"ITEM : $", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText37.Wrap(-1)

        self.m_staticText37.SetFont(
            wx.Font(13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande"))

        bSizer34.Add(self.m_staticText37, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_item_dollar_by_manager = wx.TextCtrl(self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString,
                                                             wx.DefaultPosition,
                                                             wx.Size(200, -1), 0)
        bSizer34.Add(self.m_textCtrl_item_dollar_by_manager, 0, wx.ALL, 5)

        bSizer_top_right.Add(bSizer34, 0, wx.ALIGN_RIGHT, 5)

        bSizer341 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText371 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"SHIPOUT : $", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText371.Wrap(-1)

        self.m_staticText371.SetFont(
            wx.Font(13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande"))

        bSizer341.Add(self.m_staticText371, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_shipout_dollar_by_manager = wx.TextCtrl(self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString,
                                                                wx.DefaultPosition, wx.Size(170, -1), 0)
        bSizer341.Add(self.m_textCtrl_shipout_dollar_by_manager, 0, wx.ALL, 5)

        bSizer_top_right.Add(bSizer341, 0, wx.ALIGN_RIGHT, 5)

        bSizer38 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText43 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText43.Wrap(-1)

        bSizer38.Add(self.m_staticText43, 0, wx.ALL, 5)

        bSizer39 = wx.BoxSizer(wx.VERTICAL)

        self.m_checkBox_is_auction = wx.CheckBox(self.m_scrolledWindow1, wx.ID_ANY, u"AUCTION ", wx.DefaultPosition,
                                                 wx.DefaultSize, wx.ALIGN_RIGHT)
        bSizer39.Add(self.m_checkBox_is_auction, 0, wx.ALL, 5)

        bSizer41 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText40 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"$", wx.DefaultPosition, wx.DefaultSize,
                                            wx.ALIGN_RIGHT)
        self.m_staticText40.Wrap(-1)

        bSizer41.Add(self.m_staticText40, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_auction_dollar = wx.TextCtrl(self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString,
                                                     wx.DefaultPosition, wx.Size(63, -1), 0)
        bSizer41.Add(self.m_textCtrl_auction_dollar, 0, wx.ALL, 5)

        bSizer39.Add(bSizer41, 0, wx.ALIGN_RIGHT, 5)

        bSizer38.Add(bSizer39, 0, wx.ALL, 5)

        bSizer40 = wx.BoxSizer(wx.VERTICAL)

        self.m_checkBox_is_buynow = wx.CheckBox(self.m_scrolledWindow1, wx.ID_ANY, u"BUY NOW", wx.DefaultPosition,
                                                wx.DefaultSize, wx.ALIGN_RIGHT)
        bSizer40.Add(self.m_checkBox_is_buynow, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        bSizer411 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText401 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"$", wx.DefaultPosition,
                                             wx.DefaultSize, wx.ALIGN_RIGHT)
        self.m_staticText401.Wrap(-1)

        bSizer411.Add(self.m_staticText401, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_buy_now_dollar = wx.TextCtrl(self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString,
                                                     wx.DefaultPosition, wx.Size(63, -1), 0)
        bSizer411.Add(self.m_textCtrl_buy_now_dollar, 0, wx.ALL, 5)

        bSizer40.Add(bSizer411, 1, 0, 5)

        bSizer38.Add(bSizer40, 0, wx.ALL, 5)

        bSizer_top_right.Add(bSizer38, 1, wx.ALIGN_RIGHT, 5)

        bSizer_top_row.Add(bSizer_top_right, 1, wx.EXPAND, 5)

        bSizer5.Add(bSizer_top_row, 0, wx.EXPAND, 5)

        bSizer_item_info_row = wx.BoxSizer(wx.VERTICAL)

        bSizer_item_info_row.Add((0, 20), 0, wx.EXPAND, 5)

        self.m_staticText5 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"Item Info", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)

        self.m_staticText5.SetFont(
            wx.Font(13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande"))

        bSizer_item_info_row.Add(self.m_staticText5, 0, wx.ALL, 5)

        bSizer17 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_checkBox_sold_lot = wx.CheckBox(self.m_scrolledWindow1, wx.ID_ANY, u"Sold as a lot", wx.DefaultPosition,
                                               wx.DefaultSize, wx.ALIGN_RIGHT)
        bSizer17.Add(self.m_checkBox_sold_lot, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer17.Add((70, 0), 0, wx.EXPAND, 5)

        self.m_staticText6 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"Number of lots :  ", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)

        bSizer17.Add(self.m_staticText6, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_lot_numbers = wx.TextCtrl(self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                  wx.Size(50, -1), 0)
        bSizer17.Add(self.m_textCtrl_lot_numbers, 0, wx.ALL, 5)

        bSizer17.Add((0, 0), 0, wx.EXPAND, 5)

        self.m_staticText10 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"Items / lot :", wx.DefaultPosition,
                                            wx.Size(118, -1), wx.ALIGN_RIGHT)
        self.m_staticText10.Wrap(-1)

        bSizer17.Add(self.m_staticText10, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_ietms_per_lot = wx.TextCtrl(self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString,
                                                    wx.DefaultPosition, wx.Size(50, -1), 0)
        bSizer17.Add(self.m_textCtrl_ietms_per_lot, 0, wx.ALL, 5)
        bSizer17.Add((25, 0), 0, wx.EXPAND, 5)
        # ----
        self.m_staticText101 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"Function Category:",
                                             wx.DefaultPosition,
                                             wx.Size(122, -1), wx.ALIGN_RIGHT)
        self.m_staticText101.Wrap(-1)

        bSizer17.Add(self.m_staticText101, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        # self.m_textCtrl_func_cat = wx.TextCtrl(self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString,
        #                                             wx.DefaultPosition, wx.Size(50, -1), 0)
        # bSizer17.Add(self.m_textCtrl_func_cat, 0, wx.ALL, 5)
        functions = ['F1', 'F2', 'F3', 'F4', 'F5', 'F6']
        self.function_category_selector = wx.ComboBox(self.m_scrolledWindow1, choices=list(functions), value='F3')
        bSizer17.Add(self.function_category_selector, 0, wx.ALL, 5)
        # ----
        self.m_staticText101 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"Cosmetic Category:",
                                             wx.DefaultPosition,
                                             wx.Size(122, -1), wx.ALIGN_RIGHT)
        self.m_staticText101.Wrap(-1)

        bSizer17.Add(self.m_staticText101, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        # self.m_textCtrl_cosmetic_cat = wx.TextCtrl(self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString,
        #                                        wx.DefaultPosition, wx.Size(50, -1), 0)
        # bSizer17.Add(self.m_textCtrl_cosmetic_cat, 0, wx.ALL, 5)
        cosmetic = ['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9']
        self.cosmetic_category_selector = wx.ComboBox(self.m_scrolledWindow1, choices=list(cosmetic), value='C3')
        bSizer17.Add(self.cosmetic_category_selector, 0, wx.ALL, 5)
        # ----

        bSizer_item_info_row.Add(bSizer17, 1, wx.EXPAND, 5)

        bSizer18 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText7 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"Quantity :", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)

        bSizer18.Add(self.m_staticText7, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_single_qty = wx.TextCtrl(self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                 wx.Size(50, -1), 0)
        bSizer18.Add(self.m_textCtrl_single_qty, 0, wx.ALL, 5)

        bSizer18.Add((55, 0), 0, wx.EXPAND, 5)

        self.m_staticText8 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"Weight per item :", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)

        bSizer18.Add(self.m_staticText8, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_weight = wx.TextCtrl(self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                             wx.Size(50, -1), 0)
        bSizer18.Add(self.m_textCtrl_weight, 0, wx.ALL, 5)

        self.m_staticText9 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"lbs", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)

        bSizer18.Add(self.m_staticText9, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        bSizer18.Add((7, 0), 1, wx.EXPAND, 5)

        self.m_staticText11 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"PO # :", wx.DefaultPosition,
                                            wx.Size(90, -1), wx.ALIGN_RIGHT)
        self.m_staticText11.Wrap(-1)

        bSizer18.Add(self.m_staticText11, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_po_number = wx.TextCtrl(self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                wx.Size(500, -1), 0)
        bSizer18.Add(self.m_textCtrl_po_number, 0, wx.ALL, 5)

        bSizer_item_info_row.Add(bSizer18, 1, wx.EXPAND, 5)

        bSizer181 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText71 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"Brand / Manufacturer :  ",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText71.Wrap(-1)

        bSizer181.Add(self.m_staticText71, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_brand = wx.TextCtrl(self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.Size(200, -1), 0)
        bSizer181.Add(self.m_textCtrl_brand, 0, wx.ALL, 5)

        bSizer181.Add((29, 0), 1, wx.EXPAND, 5)

        self.m_staticText81 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"Model # :", wx.DefaultPosition,
                                            wx.Size(90, -1), wx.ALIGN_RIGHT)
        self.m_staticText81.Wrap(-1)

        bSizer181.Add(self.m_staticText81, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_model_number = wx.TextCtrl(self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString,
                                                   wx.DefaultPosition,
                                                   wx.Size(500, -1), 0)
        bSizer181.Add(self.m_textCtrl_model_number, 0, wx.ALL, 5)

        bSizer_item_info_row.Add(bSizer181, 1, wx.EXPAND, 5)

        bSizer1811 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText711 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"Title :", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText711.Wrap(-1)

        bSizer1811.Add(self.m_staticText711, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_title = wx.TextCtrl(self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.Size(980, -1), 0)
        bSizer1811.Add(self.m_textCtrl_title, 0, wx.ALL, 5)

        bSizer_item_info_row.Add(bSizer1811, 1, wx.EXPAND, 5)

        bSizer5.Add(bSizer_item_info_row, 0, wx.EXPAND, 5)

        bSizer_classification = wx.BoxSizer(wx.VERTICAL)

        bSizer_classification.Add((0, 20), 0, wx.EXPAND, 5)

        self.m_staticText25 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"Classification", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText25.Wrap(-1)

        self.m_staticText25.SetFont(
            wx.Font(13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande"))

        bSizer_classification.Add(self.m_staticText25, 0, wx.ALL, 5)

        bSizer27 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_checkBox_new_box = wx.CheckBox(self.m_scrolledWindow1, wx.ID_ANY, u"New / Sealed Box",
                                              wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT)
        bSizer27.Add(self.m_checkBox_new_box, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer27.Add((30, 0), 0, wx.EXPAND, 5)

        self.m_checkBox_open_box = wx.CheckBox(self.m_scrolledWindow1, wx.ID_ANY, u"New / Open Box", wx.DefaultPosition,
                                               wx.DefaultSize, wx.ALIGN_RIGHT)
        bSizer27.Add(self.m_checkBox_open_box, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer27.Add((30, 0), 0, wx.EXPAND, 5)

        self.m_checkBox_used = wx.CheckBox(self.m_scrolledWindow1, wx.ID_ANY, u" Used", wx.DefaultPosition,
                                           wx.DefaultSize, wx.ALIGN_RIGHT)
        self.m_checkBox_used.SetValue(True)
        bSizer27.Add(self.m_checkBox_used, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer27.Add((30, 0), 0, wx.EXPAND, 5)

        self.m_checkBox_refurb = wx.CheckBox(self.m_scrolledWindow1, wx.ID_ANY, u"Seller Refurbished",
                                             wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT)
        bSizer27.Add(self.m_checkBox_refurb, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer_classification.Add(bSizer27, 1, wx.EXPAND, 5)

        bSizer5.Add(bSizer_classification, 0, wx.EXPAND, 5)

        bSizer_additional = wx.BoxSizer(wx.VERTICAL)

        bSizer_additional.Add((0, 20), 0, wx.EXPAND, 5)

        bSizer28 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer29 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText27 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"Additional Pieces Included",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText27.Wrap(-1)

        self.m_staticText27.SetFont(
            wx.Font(13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande"))

        bSizer29.Add(self.m_staticText27, 0, wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl_additional_pieces = wx.TextCtrl(self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString,
                                                        wx.DefaultPosition, wx.Size(-1, 200),
                                                        wx.TE_MULTILINE | wx.TE_PROCESS_TAB)
        bSizer29.Add(self.m_textCtrl_additional_pieces, 1, wx.ALL | wx.EXPAND, 5)

        bSizer28.Add(bSizer29, 1, wx.EXPAND, 5)

        bSizer30 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText28 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"Pieces Missing", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText28.Wrap(-1)

        self.m_staticText28.SetFont(
            wx.Font(13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande"))

        bSizer30.Add(self.m_staticText28, 0, wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl_missing_pieces = wx.TextCtrl(self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString,
                                                     wx.DefaultPosition, wx.Size(-1, 200),
                                                     wx.TE_MULTILINE | wx.TE_PROCESS_TAB)
        bSizer30.Add(self.m_textCtrl_missing_pieces, 1, wx.ALL | wx.EXPAND, 5)

        bSizer28.Add(bSizer30, 1, wx.EXPAND, 5)

        bSizer_additional.Add(bSizer28, 0, wx.EXPAND, 5)

        bSizer5.Add(bSizer_additional, 0, wx.EXPAND, 5)

        bSizer_defects = wx.BoxSizer(wx.VERTICAL)
        bSizer_defects.Add((0, 20), 0, wx.EXPAND, 5)

        self.m_staticText29 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"Defects", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText29.Wrap(-1)

        self.m_staticText29.SetFont(
            wx.Font(13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande"))

        bSizer_defects.Add(self.m_staticText29, 0, wx.ALL, 5)

        self.m_textCtrl_defects = wx.TextCtrl(self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                              wx.Size(-1, 100), wx.TE_MULTILINE | wx.TE_PROCESS_TAB)
        bSizer_defects.Add(self.m_textCtrl_defects, 0, wx.ALL | wx.EXPAND, 5)

        bSizer5.Add(bSizer_defects, 0, wx.EXPAND, 5)

        bSizer_testing = wx.BoxSizer(wx.VERTICAL)
        bSizer_testing.Add((0, 20), 0, wx.EXPAND, 5)

        self.m_staticText30 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"Key Functions Test Results",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText30.Wrap(-1)

        self.m_staticText30.SetFont(
            wx.Font(13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande"))

        bSizer_testing.Add(self.m_staticText30, 0, wx.ALL, 5)

        self.m_textCtrl_test_results = wx.TextCtrl(self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString,
                                                   wx.DefaultPosition, wx.Size(-1, 200),
                                                   wx.TE_MULTILINE | wx.TE_PROCESS_TAB)
        bSizer_testing.Add(self.m_textCtrl_test_results, 0, wx.ALL | wx.EXPAND, 5)

        bSizer5.Add(bSizer_testing, 0, wx.EXPAND, 5)

        bSizer_bottom = wx.BoxSizer(wx.VERTICAL)

        bSizer33 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText32 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"04/13/2022        Rev 1.4",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText32.Wrap(-1)

        self.m_staticText32.SetFont(
            wx.Font(11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Lucida Grande"))

        bSizer33.Add(self.m_staticText32, 3, wx.ALL, 5)

        self.m_staticText33 = wx.StaticText(self.m_scrolledWindow1, wx.ID_ANY, u"ABC Company, Inc.",
                                            wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT)
        self.m_staticText33.Wrap(-1)

        self.m_staticText33.SetFont(
            wx.Font(11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Lucida Grande"))

        bSizer33.Add(self.m_staticText33, 1, wx.ALL, 5)

        bSizer_bottom.Add(bSizer33, 1, wx.EXPAND, 5)

        bSizer5.Add(bSizer_bottom, 0, wx.EXPAND, 5)

        self.m_scrolledWindow1.SetSizer(bSizer5)
        self.m_scrolledWindow1.Layout()
        bSizer8.Add(self.m_scrolledWindow1, 1, wx.ALL | wx.EXPAND, 5)

        self.m_panel5.SetSizer(bSizer8)
        self.m_panel5.Layout()
        bSizer8.Fit(self.m_panel5)
        bSizer4.Add(self.m_panel5, 0, wx.ALL | wx.EXPAND, 5)

        self.m_panel2.SetSizer(bSizer4)
        self.m_panel2.Layout()
        bSizer4.Fit(self.m_panel2)
        bSizer1.Add(self.m_panel2, 1, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        # self.m_textCtrl_model_number.Bind(wx.EVT_KILL_FOCUS, self.verify_discontinue)

        self.m_button_create_pdf.Bind(wx.EVT_BUTTON, self.create_pdf)
        self.m_button_list_it.Bind(wx.EVT_BUTTON, self.list_it)
        self.m_button_reject.Bind(wx.EVT_BUTTON, self.reject_it)
        self.m_button_edit.Bind(wx.EVT_BUTTON, self.edit)
        self.m_button_print_ez_label.Bind(wx.EVT_BUTTON, self.print_ez_label)
        self.m_button_print_item_label.Bind(wx.EVT_BUTTON, self.print_item_labels)
        self.m_button_email_pdf.Bind(wx.EVT_BUTTON, self.email_pdf)
        self.m_button_print.Bind(wx.EVT_BUTTON, self.print)
        self.m_button_submit.Bind(wx.EVT_BUTTON, self.submit)
        self.m_button_create_new_from_it.Bind(wx.EVT_BUTTON, self.create_new_from_it)
        self.m_button_update.Bind(wx.EVT_BUTTON, self.update)
        self.m_button_add_note.Bind(wx.EVT_BUTTON, self.add_note)
        self.m_button_add_sn.Bind(wx.EVT_BUTTON, self.add_serial_numbers)
        self.m_button_add_researched_price.Bind(wx.EVT_BUTTON, self.add_researched_price)
        self.m_button_add_pics.Bind(wx.EVT_BUTTON, self.add_pictures)
        self.m_button_update.Hide()
        self.m_button_list_it.Hide()
        self.m_button_reject.Hide()
        self.m_button_edit.Hide()
        # Adding icons to buttons
        self.m_button_add_note.SetBitmap(wx.Bitmap(wx.Image(note.GetImage()).ConvertToBitmap()))
        self.m_button_add_sn.SetBitmap(wx.Bitmap(wx.Image(sn.GetImage()).ConvertToBitmap()))
        self.m_button_add_pics.SetBitmap(wx.Bitmap(wx.Image(pics.GetImage()).ConvertToBitmap()))
        self.m_button_add_researched_price.SetBitmap(wx.Bitmap(wx.Image(price.GetImage()).ConvertToBitmap()))
        self.m_button_list_it.SetBitmap(wx.Bitmap(wx.Image(listit.GetImage()).ConvertToBitmap()))
        self.m_button_reject.SetBitmap(wx.Bitmap(wx.Image(trash.GetImage()).ConvertToBitmap()))
        self.m_button_print.SetBitmap(wx.Bitmap(wx.Image(printer.GetImage()).ConvertToBitmap()))
        self.m_button_print_ez_label.SetBitmap(wx.Bitmap(wx.Image(ez_label.GetImage()).ConvertToBitmap()))
        self.m_button_print_item_label.SetBitmap(wx.Bitmap(wx.Image(small_label.GetImage()).ConvertToBitmap()))
        self.m_button_email_pdf.SetBitmap(wx.Bitmap(wx.Image(email.GetImage()).ConvertToBitmap()))
        self.m_button_create_pdf.SetBitmap(wx.Bitmap(wx.Image(pdf.GetImage()).ConvertToBitmap()))
        self.m_button_submit.SetBitmap(wx.Bitmap(wx.Image(submit.GetImage()).ConvertToBitmap()))
        self.m_button_create_new_from_it.SetBitmap(wx.Bitmap(wx.Image(reuse_sheet.GetImage()).ConvertToBitmap()))
        self.m_button_edit.SetBitmap(wx.Bitmap(wx.Image(editit.GetImage()).ConvertToBitmap()))

    def __del__(self):
        pass

    def add_barcode(self, barcode_txt, src_pdf, rect=(270, 0, 370, 210)):
        src_pdf_filename = src_pdf
        code128.image(barcode_txt).save("generated_barcode.png")  # with PIL present
        #
        # with open("generated_barcode.svg", "w") as f:
        #     f.write(code128.svg(barcode_txt))
        img_rect = fitz.Rect(rect)
        document = fitz.open(src_pdf_filename)

        # We'll put image on first page only but you could put it elsewhere
        page = document[0]
        file_name = os.path.abspath('generated_barcode.png')
        page.insert_image(img_rect, filename=file_name)
        document.saveIncr()
        document.close()
        if os.path.exists(file_name):
            os.remove(file_name)

        else:
            print("The barcode_img file does not exist")

    def make_smb_dir(self):
        mysmb = smb('RHEL8', '192.168.1.14', 'Anonymous')
        mysmb.connect_with_smb_share()
        pic_dir = mysmb.create_new_dir(self.sheetID)
        mysmb.close_connection()
        print("Created pic directory = {}".format(pic_dir))
        return pic_dir

    def load_form_with_defaults(self):
        self.set_window_size()
        if self.loggedin_user_is_active:
            print("user is active")
            if self.loggedin_user_is_manager:
                print("user is manager")

            else:
                print("user is not manager or user is a tech")
                self.m_textCtrl_ez_pn.Disable()
                self.m_textCtrl_shipout_dollar_by_manager.Disable()
                self.m_textCtrl_item_dollar_by_manager.Disable()
                self.m_textCtrl_buy_now_dollar.Disable()
                self.m_textCtrl_auction_dollar.Disable()
                self.m_checkBox_is_buynow.Disable()
                self.m_checkBox_is_auction.Disable()
                # self.m_button_print_ez_label.Hide()
                # self.m_button_print_item_label.Hide()
        else:
            print("user is not active")

        self.m_textCtrl_tech_name.SetValue(self.loggedin_user_username.upper())
        self.m_textCtrl_tech_date_received.SetValue(self.date_today)
        self.m_button_print_ez_label.Disable()
        self.m_textCtrl_ez_pn.SetValue("")
        self.m_button_print_item_label.Disable()
        self.m_button_print.Disable()
        self.m_button_create_pdf.Disable()
        self.m_button_email_pdf.Disable()
        self.m_button_add_pics.Disable()

    def read_manager_form(self):
        fields = ['item_dollar_by_manager', 'shipout_dollar_by_manager', 'auction_dollar', 'buynow_dollar']
        ctrls = [self.m_textCtrl_item_dollar_by_manager, self.m_textCtrl_shipout_dollar_by_manager,
                 self.m_textCtrl_auction_dollar, self.m_textCtrl_buy_now_dollar]
        dtype = ['float', 'float', 'float', 'float']
        if self.m_textCtrl_item_dollar_by_manager.GetValue().lstrip() != '':
            idbm = float(self.m_textCtrl_item_dollar_by_manager.GetValue().lstrip())
        else:
            idbm = 0.0

        if self.m_textCtrl_shipout_dollar_by_manager.GetValue().lstrip() != '':
            sdbm = float(
                self.m_textCtrl_shipout_dollar_by_manager.GetValue().lstrip())
        else:
            sdbm = 0.0

        if self.m_textCtrl_auction_dollar.GetValue().lstrip() != '':
            sd = float(self.m_textCtrl_auction_dollar.GetValue().lstrip())
        else:
            sd = 0.0

        if self.m_textCtrl_buy_now_dollar.GetValue().lstrip() != '':
            bd = float(self.m_textCtrl_buy_now_dollar.GetValue().lstrip())
        else:
            bd = 0.0

        manager_data = {
            'ez_pn': self.m_textCtrl_ez_pn.GetValue().lstrip().upper(),
            'item_dollar_by_manager': idbm,
            'shipout_dollar_by_manager': sdbm,
            'auction_dollar': sd,
            'buynow_dollar': bd,
            'is_auction': self.m_checkBox_is_auction.GetValue(),
            'is_buynow': self.m_checkBox_is_buynow.GetValue(),
        }
        #  try:
        # except:
        #     manager_data = {
        #         'ez_pn': '',
        #         'item_dollar_by_manager': 0,
        #         'shipout_dollar_by_manager': 0,
        #         'is_auction': self.m_checkBox_is_auction.GetValue(),
        #         'is_buynow': self.m_checkBox_is_buynow.GetValue(),
        #         'auction_dollar': 0,
        #         'buynow_dollar': 0,
        #     }
        print(manager_data)
        return manager_data

    def read_tech_form(self):
        if not self.m_checkBox_sold_lot.GetValue():
            self.sold_as_individual = True
            self.lots = 0
            self.lot_items_qty = 0
            self.single_quantity = int(self.m_textCtrl_single_qty.GetValue().lstrip())
        else:
            self.sold_as_individual = False
            self.lots = int(self.m_textCtrl_lot_numbers.GetValue().lstrip())
            self.lot_items_qty = int(self.m_textCtrl_ietms_per_lot.GetValue().lstrip())
            self.single_quantity = 0

        """This function reads the vlaues from all text control fields in the new config sheet form and return it as dictionary"""
        tech_data = {
            'item_sn_list': self.sn_of_items_tested,
            'function_category': self.function_category_selector.GetValue(),
            'cosmetic_category': self.cosmetic_category_selector.GetValue(),
            'tech_id': self.loggedin_user_id,
            'tech_name': self.m_textCtrl_tech_name.GetValue().lstrip().upper(),
            'date_submitted': self.date_today,
            'sold_as_lot': self.m_checkBox_sold_lot.GetValue(),
            'sold_as_individual': self.sold_as_individual,
            'number_of_lots': self.lots,
            'items_per_lot': self.lot_items_qty,
            'single_quantity': self.single_quantity,
            'weight': float(self.m_textCtrl_weight.GetValue().lstrip()),
            'po_number': self.m_textCtrl_po_number.GetValue().lstrip(),
            'brand_name': self.m_textCtrl_brand.GetValue().lstrip().upper(),
            'model_number': self.m_textCtrl_model_number.GetValue().lstrip(),
            'item_title': self.m_textCtrl_title.GetValue().lstrip(),
            'is_new_box': self.m_checkBox_new_box.GetValue(),
            'is_open_box': self.m_checkBox_open_box.GetValue(),
            'is_used': self.m_checkBox_used.GetValue(),
            'is_refurb': self.m_checkBox_refurb.GetValue(),
            'additional_pieces': self.m_textCtrl_additional_pieces.GetValue().lstrip(),
            'missing_pieces': self.m_textCtrl_missing_pieces.GetValue().lstrip(),
            'defects': self.m_textCtrl_defects.GetValue().lstrip(),
            'test_results': self.m_textCtrl_test_results.GetValue().lstrip(),
            'tech_note': self.tech_note,
            'researched_item_price': self.researched_item_price,
            'photo_folder_address': self.link_to_pics,

        }
        print(tech_data)
        return tech_data

    def edit(self, event):

        print(self.m_button_edit.GetLabel())
        if self.m_button_edit.GetLabel() == "Cancel":

            self.m_button_edit.SetLabel("Edit")
            # self.m_button_edit.SetSize(wx.Size(130, -1))
            if self.loggedin_user_is_active:
                if self.loggedin_user_is_manager:
                    self.m_button_update.Hide()
                    self.m_button_list_it.Show()
                    self.m_button_reject.Show()
                else:
                    if not self.processed:
                        self.m_button_update.Hide()
                        self.m_button_print_ez_label.Show()
                        self.m_button_print_item_label.Show()
            else:
                print(
                    "This user {} can not access this resource as user is not active".format(
                        self.loggedin_user_username))

            self.m_button_submit.SetLabel("Submit New")
            self.m_button_add_sn.SetLabel("Show SN #")
            self.m_button_add_note.SetLabel("Show Note")
            self.m_button_add_pics.SetLabel("Show Pics")
            self.m_button_add_researched_price.SetLabel("Show Price")
            self.m_button_create_new_from_it.Show()
            self.m_button_submit.Show()
            self.m_button_print.Enable()
            self.m_button_create_pdf.Enable()
            self.m_button_print_ez_label.Enable()
            self.m_button_print_item_label.Enable()
            self.m_button_email_pdf.Enable()
            self.lock_fields()

        elif self.m_button_edit.GetLabel() == "Edit":
            if self.loggedin_user_username.upper() == self.m_textCtrl_tech_name.GetValue().lstrip().upper():
                pass
            else:
                if not self.loggedin_user_is_manager:
                    msg = "You can edit only your own sheets"
                    wx.MessageBox(msg, 'Stop!',
                                  wx.OK | wx.ICON_STOP)
                    return
                else:
                    pass
            self.m_button_edit.SetLabel("Cancel")
            sql_chk = "SELECT sheet_id, COUNT(*) FROM `ConfigSheet` WHERE sheet_id = {} GROUP BY sheet_id".format(
                self.sheetID)
            sql_upd = "UPDATE `ConfigSheet` SET edited = True WHERE sheet_id = {}".format(
                self.sheetID)
            # print(sql_chk, "\n", sql_upd)

            if self.loggedin_user_is_active:
                if self.loggedin_user_is_manager:
                    self.m_button_update.Show()
                    self.m_button_list_it.Hide()
                    self.m_button_reject.Hide()
                    self.update_database(sql_chk, sql_upd)
                else:
                    if not self.processed:
                        if self.loggedin_user_username.upper() == self.m_textCtrl_tech_name.GetValue().lstrip().upper():
                            self.m_button_update.Show()
                            # self.m_button_print_label.Hide()
                            self.update_database(sql_chk, sql_upd)
                        else:
                            msg = "You can edit only your own sheets"
                            wx.MessageBox(msg, 'Stop!',
                                          wx.OK | wx.ICON_STOP)
                    else:
                        print("This sheet is already processed so it can no longer be edited")
                        mesge = "This sheet is already processed so it can no longer be edited"
                        wx.MessageBox(mesge, 'Stop!',
                                      wx.OK | wx.ICON_STOP)
            else:
                print(
                    "This user {} can not access this resource as it is not active".format(self.loggedin_user_username))

            self.m_button_submit.SetLabel("Submit New")
            self.m_button_add_sn.SetLabel("Edit SN #")
            self.m_button_add_note.SetLabel("Edit Note")
            self.m_button_add_pics.SetLabel("Take Pics")
            self.m_button_add_researched_price.SetLabel("Edit Price")
            self.m_button_create_new_from_it.Hide()
            self.m_button_submit.Hide()
            self.unlock_fields()
            self.m_button_print.Disable()
            self.m_button_create_pdf.Disable()
            self.m_button_print_ez_label.Disable()
            self.m_button_print_item_label.Disable()
            self.m_button_email_pdf.Disable()

    def update(self, event):
        print("processed = ", self.processed)
        tech_form_data = self.read_tech_form()  # a dict object
        manager_form_data = self.read_manager_form()  # a dict object
        quantity = int(self.get_qty())
        print("Total items or lots in this sheet: ", quantity)
        sn_in_sn_list = self.get_sn_list_entered(tech_form_data)
        print("Serial numbers entered : ", sn_in_sn_list)
        if quantity != len(sn_in_sn_list):
            mesg = f"Qty of SN scanned are not equal to number of items in this sheet!\nNumber of items: {quantity}\nNumber of SN# scanned: {len(sn_in_sn_list)}."
            wx.MessageBox(mesg, 'Mismatch', wx.OK | wx.ICON_STOP)

            return
        else:
            pass
        if not self.processed:
            new_val = True

            sql_chk = "SELECT sheet_id, COUNT(*) FROM `ConfigSheet` WHERE sheet_id = {} GROUP BY sheet_id".format(
                self.sheetID)
            sql_upd_manager = "UPDATE ConfigSheet SET buy_now_price = %s, auction_price = %s, selling_as_buynow = %s, selling_as_auction = %s, ez_part_number = %s, item_price_by_manager = %s, shipout_price_by_manager = %s, item_sn_list = %s, function_category = %s, cosmetic_category = %s,photo_folder = %s, item_price_researched = %s, sell_as_lot = %s, sell_as_individual = %s, number_of_lots = %s, items_per_lot = %s, number_of_items = %s, item_weight = %s, po_number = %s, brand_mfg_name = %s, model_no = %s, title = %s, new_sealed = %s, new_open_box = %s, used = %s, seller_refurbished = %s, additional_pieces_included = %s, pieces_missing = %s, defects = %s, key_functions_test_results = %s, tech_note = %s WHERE sheet_id = %s"
            manager_val = (manager_form_data['buynow_dollar'],
                           manager_form_data['auction_dollar'], manager_form_data['is_buynow'],
                           manager_form_data['is_auction'], manager_form_data['ez_pn'],
                           manager_form_data['item_dollar_by_manager'],
                           manager_form_data['shipout_dollar_by_manager'],
                           tech_form_data['item_sn_list'], tech_form_data['function_category'],
                           tech_form_data['cosmetic_category'],
                           tech_form_data['photo_folder_address'], tech_form_data['researched_item_price'],
                           tech_form_data['sold_as_lot'], tech_form_data['sold_as_individual'],
                           tech_form_data['number_of_lots'], tech_form_data['items_per_lot'],
                           tech_form_data['single_quantity'],
                           tech_form_data['weight'], tech_form_data['po_number'], tech_form_data['brand_name'],
                           tech_form_data['model_number'], tech_form_data['item_title'],
                           tech_form_data['is_new_box'], tech_form_data['is_open_box'], tech_form_data['is_used'],
                           tech_form_data['is_refurb'], tech_form_data['additional_pieces'],
                           tech_form_data['missing_pieces'], tech_form_data['defects'],
                           tech_form_data['test_results'], tech_form_data['tech_note'],
                           self.sheetID)

            sql_upd_tech = "UPDATE ConfigSheet SET item_sn_list = %s, function_category = %s, cosmetic_category = %s,photo_folder = %s, item_price_researched = %s, sell_as_lot = %s, sell_as_individual = %s, number_of_lots = %s, items_per_lot = %s, number_of_items = %s, item_weight = %s, po_number = %s, brand_mfg_name = %s, model_no = %s, title = %s, new_sealed = %s, new_open_box = %s, used = %s, seller_refurbished = %s, additional_pieces_included = %s, pieces_missing = %s, defects = %s, key_functions_test_results = %s, tech_note = %s WHERE sheet_id = %s"
            tech_val = (tech_form_data['item_sn_list'], tech_form_data['function_category'],
                        tech_form_data['cosmetic_category'],
                        tech_form_data['photo_folder_address'], tech_form_data['researched_item_price'],
                        tech_form_data['sold_as_lot'], tech_form_data['sold_as_individual'],
                        tech_form_data['number_of_lots'], tech_form_data['items_per_lot'],
                        tech_form_data['single_quantity'],
                        tech_form_data['weight'], tech_form_data['po_number'], tech_form_data['brand_name'],
                        tech_form_data['model_number'], tech_form_data['item_title'],
                        tech_form_data['is_new_box'], tech_form_data['is_open_box'], tech_form_data['is_used'],
                        tech_form_data['is_refurb'], tech_form_data['additional_pieces'],
                        tech_form_data['missing_pieces'], tech_form_data['defects'],
                        tech_form_data['test_results'], tech_form_data['tech_note'],
                        self.sheetID)

            # print(sql_upd_tech)
            # print(tech_val)

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
                    """find if record already exists for this sheet number"""

                    cursor.execute(sql_chk)

                    # gets the number of rows returned by database for the above sql command
                    row_count = cursor.rowcount
                    print("number of rows returned by database for this sheet number: {}".format(row_count))

                    if row_count == 0:
                        print("No record found for this sheet")

                    else:
                        """Update the record """

                        if self.loggedin_user_is_manager:
                            cursor.execute(sql_upd_manager, manager_val)
                        else:
                            cursor.execute(sql_upd_tech, tech_val)
                        # connection is not autocommit by default.So you must commit to save your changes.
                        connection.commit()
                        # Some things that are done to the form after the submission of data to database
                        print('Connection committed')
                        mesg = "This config sheet is successfully updated"
                        print(mesg)
                        wx.MessageBox(mesg, 'Success',
                                      wx.OK | wx.ICON_INFORMATION)

            # except pymysql.err.OperationalError as error:
            except pymysql.err.OperationalError as error:
                print(error)

            finally:
                connection.close()
            self.Parent.refresh()
            self.Destroy()
        else:
            if self.loggedin_user_is_manager:
                new_val = True
                tech_form_data = self.read_tech_form()  # a dict object
                manager_form_data = self.read_manager_form()  # a dict object
                sql_chk = "SELECT sheet_id, COUNT(*) FROM `ConfigSheet` WHERE sheet_id = {} GROUP BY sheet_id".format(
                    self.sheetID)
                sql_upd_manager = "UPDATE ConfigSheet SET buy_now_price = %s, auction_price = %s, selling_as_buynow = %s, selling_as_auction = %s, ez_part_number = %s, item_price_by_manager = %s, shipout_price_by_manager = %s, item_sn_list = %s, function_category = %s, cosmetic_category = %s,photo_folder = %s, item_price_researched = %s, sell_as_lot = %s, sell_as_individual = %s, number_of_lots = %s, items_per_lot = %s, number_of_items = %s, item_weight = %s, po_number = %s, brand_mfg_name = %s, model_no = %s, title = %s, new_sealed = %s, new_open_box = %s, used = %s, seller_refurbished = %s, additional_pieces_included = %s, pieces_missing = %s, defects = %s, key_functions_test_results = %s, tech_note = %s WHERE sheet_id = %s"
                manager_val = (manager_form_data['buynow_dollar'],
                               manager_form_data['auction_dollar'], manager_form_data['is_buynow'],
                               manager_form_data['is_auction'], manager_form_data['ez_pn'],
                               manager_form_data['item_dollar_by_manager'],
                               manager_form_data['shipout_dollar_by_manager'],
                               tech_form_data['item_sn_list'], tech_form_data['function_category'],
                               tech_form_data['cosmetic_category'],
                               tech_form_data['photo_folder_address'], tech_form_data['researched_item_price'],
                               tech_form_data['sold_as_lot'], tech_form_data['sold_as_individual'],
                               tech_form_data['number_of_lots'], tech_form_data['items_per_lot'],
                               tech_form_data['single_quantity'],
                               tech_form_data['weight'], tech_form_data['po_number'], tech_form_data['brand_name'],
                               tech_form_data['model_number'], tech_form_data['item_title'],
                               tech_form_data['is_new_box'], tech_form_data['is_open_box'], tech_form_data['is_used'],
                               tech_form_data['is_refurb'], tech_form_data['additional_pieces'],
                               tech_form_data['missing_pieces'], tech_form_data['defects'],
                               tech_form_data['test_results'], tech_form_data['tech_note'],
                               self.sheetID)

                sql_upd_tech = "UPDATE ConfigSheet SET item_sn_list = %s, function_category = %s, cosmetic_category = %s,photo_folder = %s, item_price_researched = %s, sell_as_lot = %s, sell_as_individual = %s, number_of_lots = %s, items_per_lot = %s, number_of_items = %s, item_weight = %s, po_number = %s, brand_mfg_name = %s, model_no = %s, title = %s, new_sealed = %s, new_open_box = %s, used = %s, seller_refurbished = %s, additional_pieces_included = %s, pieces_missing = %s, defects = %s, key_functions_test_results = %s, tech_note = %s WHERE sheet_id = %s"
                tech_val = (tech_form_data['item_sn_list'], tech_form_data['function_category'],
                            tech_form_data['cosmetic_category'],
                            tech_form_data['photo_folder_address'], tech_form_data['researched_item_price'],
                            tech_form_data['sold_as_lot'], tech_form_data['sold_as_individual'],
                            tech_form_data['number_of_lots'], tech_form_data['items_per_lot'],
                            tech_form_data['single_quantity'],
                            tech_form_data['weight'], tech_form_data['po_number'], tech_form_data['brand_name'],
                            tech_form_data['model_number'], tech_form_data['item_title'],
                            tech_form_data['is_new_box'], tech_form_data['is_open_box'], tech_form_data['is_used'],
                            tech_form_data['is_refurb'], tech_form_data['additional_pieces'],
                            tech_form_data['missing_pieces'], tech_form_data['defects'],
                            tech_form_data['test_results'], tech_form_data['tech_note'],
                            self.sheetID)

                # print(sql_upd_tech)
                # print(tech_val)

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
                        """find if record already exists for this sheet number"""

                        cursor.execute(sql_chk)

                        # gets the number of rows returned by database for the above sql command
                        row_count = cursor.rowcount
                        print("number of rows returned by database for this sheet number: {}".format(row_count))

                        if row_count == 0:
                            print("No record found for this sheet")

                        else:
                            """Update the record """

                            if self.loggedin_user_is_manager:
                                cursor.execute(sql_upd_manager, manager_val)
                            else:
                                cursor.execute(sql_upd_tech, tech_val)
                            # connection is not autocommit by default.So you must commit to save your changes.
                            connection.commit()
                            # Some things that are done to the form after the submission of data to database
                            print('Connection committed')
                            mesg = "This config sheet is successfully updated"
                            print(mesg)
                            wx.MessageBox(mesg, 'Success',
                                          wx.OK | wx.ICON_INFORMATION)

                # except pymysql.err.OperationalError as error:
                except pymysql.err.OperationalError as error:
                    print(error)

                finally:
                    connection.close()
                self.Parent.refresh()
                self.Destroy()

            else:

                mesg = "File status 'Processed' \nOnly manager can edit this file now."
                print(mesg)
                wx.MessageBox(mesg, 'STOP',
                              wx.OK | wx.ICON_STOP)

    def create_new_from_it(self, event):
        print('create_new_from_it is pressed')
        print(self.m_button_create_new_from_it.GetLabel())
        if self.m_button_create_new_from_it.GetLabel() == "Cancel":
            self.m_button_create_new_from_it.SetLabel("Create New")
            print("cancel was clicked on sheet ID {}".format(self.sheetID))
            self.m_button_add_pics.Enable()
            self.m_button_edit.Enable()
            if self.loggedin_user_is_manager:
                self.m_button_list_it.Show()
                self.m_button_reject.Show()

            self.m_button_add_pics.SetLabel("Show Pics")
            self.m_button_add_note.SetLabel("Show Note")
            self.m_button_add_sn.SetLabel("Show SN #")
            self.m_button_add_researched_price.SetLabel("Show Price")
            self.load_gui_form_from_database(self.sheetID)
            self.lock_fields()
            self.m_button_submit.Disable()
            self.m_button_print.Enable()
            self.m_button_create_pdf.Enable()
            self.m_button_print_ez_label.Enable()
            self.m_button_print_item_label.Enable()
            self.m_button_email_pdf.Enable()
            self.SetTitle("ezPro - Configsheet ( # " + self.sheetID + " )")

        elif self.m_button_create_new_from_it.GetLabel() == "Create New":
            self.m_button_create_new_from_it.SetLabel("Cancel")

            self.load_form_with_defaults()
            self.tech_note = ''
            self.sn_of_items_tested = ''
            self.researched_item_price = 0.00

            self.m_button_add_note.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))
            self.m_button_add_researched_price.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))
            self.m_button_add_sn.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))

            self.m_button_add_pics.Disable()
            self.m_button_edit.Disable()
            self.m_button_list_it.Hide()
            self.m_button_reject.Hide()
            self.m_button_add_pics.SetLabel("Take Pics")
            self.m_button_add_note.SetLabel("Add Note")
            self.m_button_add_sn.SetLabel("Add SN #")
            self.m_button_add_researched_price.SetLabel("Add Price")
            self.unlock_fields()
            self.m_button_submit.Enable()
            self.m_staticText_msg.SetLabel('')
            self.SetTitle("ezPro - Re-using Configsheet ( # " + self.sheetID + " )")

    def get_sn_list_entered(self, data):
        lst = data['item_sn_list'].split('\n')
        if lst[-1] != "":
            return lst
        else:
            return lst[:-1]


    def submit(self, event):
        process_it = self.verify_discontinue()
        if process_it == 'Yes':
            pass
        else:
            return
        tech_form_data = self.read_tech_form()  # a dict object
        manager_form_data = self.read_manager_form()  # a dict object
        # print(manager_form_data)
        print(tech_form_data)
        # serial_numbers = tech_form_data['item_sn_list'].split('\n')
        # print(serial_numbers)

        quantity = int(self.get_qty())
        print("Total items or lots in this sheet: ",quantity)
        sn_in_sn_list = self.get_sn_list_entered(tech_form_data)
        print("Serial numbers entered : ", sn_in_sn_list)
        if quantity != len(sn_in_sn_list):
            mesg = f"Qty of SN scanned are not equal to number of items in this sheet!\nNumber of items: {quantity}\nNumber of SN# scanned: {len(sn_in_sn_list)}."
            wx.MessageBox(mesg, 'Mismatch', wx.OK | wx.ICON_STOP)

            return
        else:
            pass

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
                """find if record already exists for this part number"""
                # for sn in serial_numbers:
                #     sql = "SELECT * FROM `ConfigSheet` WHERE item_sn_list LIKE '{}'".format(sn)
                #     cursor.execute(sql)
                #     # gets the number of rows returned by database for the above sql command
                #     row_count = cursor.rowcount
                #     print(row_count)
                row_count = 0
                print("number of rows returned by database for this SN: {}".format(row_count))
                if row_count == 0:
                    # self.m_staticText_login_msg.SetLabel("You can create a user with this username")
                    """Create a new record if no previous record found"""
                    new_val = True

                    tech_sql = "INSERT INTO `ConfigSheet` (item_sn_list, new, function_category, cosmetic_category, photo_folder, item_price_researched, tech_id, date_submitted, sell_as_lot, sell_as_individual, number_of_lots, items_per_lot, number_of_items, item_weight, po_number, brand_mfg_name, model_no, title, new_sealed, new_open_box, used, seller_refurbished, additional_pieces_included, pieces_missing, defects, key_functions_test_results, tech_note) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    tech_val = (tech_form_data['item_sn_list'], new_val, tech_form_data['function_category'],
                                tech_form_data['cosmetic_category'],
                                tech_form_data['photo_folder_address'], tech_form_data['researched_item_price'],
                                tech_form_data['tech_id'], tech_form_data['date_submitted'],
                                tech_form_data['sold_as_lot'], tech_form_data['sold_as_individual'],
                                tech_form_data['number_of_lots'], tech_form_data['items_per_lot'],
                                tech_form_data['single_quantity'],
                                tech_form_data['weight'], tech_form_data['po_number'], tech_form_data['brand_name'],
                                tech_form_data['model_number'], tech_form_data['item_title'],
                                tech_form_data['is_new_box'], tech_form_data['is_open_box'], tech_form_data['is_used'],
                                tech_form_data['is_refurb'], tech_form_data['additional_pieces'],
                                tech_form_data['missing_pieces'], tech_form_data['defects'],
                                tech_form_data['test_results'], tech_form_data['tech_note'],
                                )
                    manager_sql = "INSERT INTO `ConfigSheet` (item_sn_list, new, function_category, cosmetic_category, buy_now_price, auction_price, selling_as_buynow, selling_as_auction, ez_part_number, item_price_by_manager, shipout_price_by_manager, photo_folder, item_price_researched, tech_id, date_submitted, sell_as_lot, sell_as_individual, number_of_lots, items_per_lot, number_of_items, item_weight, po_number, brand_mfg_name, model_no, title, new_sealed, new_open_box, used, seller_refurbished, additional_pieces_included, pieces_missing, defects, key_functions_test_results, tech_note) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    manager_val = (tech_form_data['item_sn_list'], new_val, tech_form_data['function_category'],
                                   tech_form_data['cosmetic_category'], manager_form_data['buynow_dollar'],
                                   manager_form_data['auction_dollar'], manager_form_data['is_buynow'],
                                   manager_form_data['is_auction'], manager_form_data['ez_pn'],
                                   manager_form_data['item_dollar_by_manager'],
                                   manager_form_data['shipout_dollar_by_manager'],
                                   tech_form_data['photo_folder_address'], tech_form_data['researched_item_price'],
                                   tech_form_data['tech_id'],
                                   tech_form_data['date_submitted'],
                                   tech_form_data['sold_as_lot'], tech_form_data['sold_as_individual'],
                                   tech_form_data['number_of_lots'], tech_form_data['items_per_lot'],
                                   tech_form_data['single_quantity'],
                                   tech_form_data['weight'], tech_form_data['po_number'], tech_form_data['brand_name'],
                                   tech_form_data['model_number'], tech_form_data['item_title'],
                                   tech_form_data['is_new_box'], tech_form_data['is_open_box'],
                                   tech_form_data['is_used'],
                                   tech_form_data['is_refurb'], tech_form_data['additional_pieces'],
                                   tech_form_data['missing_pieces'], tech_form_data['defects'],
                                   tech_form_data['test_results'], tech_form_data['tech_note'],
                                   )
                    if self.loggedin_user_is_manager:
                        cursor.execute(manager_sql, manager_val)
                    else:
                        # cursor.execute(tech_sql, tech_val)
                        cursor.execute(manager_sql, manager_val)

                    # connection is not autocommit by default.So you must commit to save
                    # your changes.
                    connection.commit()
                    self.Parent.refresh()
                    # Some things that are done to the form after the submission of data to database
                    print('Connection committed')

                    # self.m_staticText_login_msg.SetLabel('Success! New record added to database.')
                    msg = "New record added to database."
                    abc = wx.MessageBox(msg, "Success!",
                                        wx.OK | wx.ICON_INFORMATION, )


                else:
                    msg1 = "This Serial number already assigned to another unit. Try again with a different one."
                    abc = wx.MessageBox(msg1, "STOP!",
                                        wx.OK | wx.ICON_STOP, )


        except pymysql.err.OperationalError as error:
            print(error)
            # self.m_staticText_login_msg.SetLabel("Connection Error! Could not submit record")

        finally:
            connection.close()
            self.Destroy()

    def query_database(self, qry, val):
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
                """find if record exists for this username"""
                cursor.execute(
                    qry,
                    (val,))

                info = cursor.fetchall()
                # print(info)

        except pymysql.err.OperationalError as error:
            print(error)
            # self.m_staticText_login_msg.SetLabel("Connection Error! ")

        finally:
            connection.close()
        return info

    def create_pdf_on_right_click(self, sheet_id):
        self.fill_pdf_template(self.configsheet_template_file_path,
                               self.get_data_from_db_for_pdf_template(sheet_id))

    def get_data_from_db_for_pdf_template(self, sheet_id):
        sheet_info_qry = "SELECT * FROM ConfigSheet WHERE sheet_id = %s"
        dataa = self.query_database(sheet_info_qry, sheet_id)[0]
        print("+++++++++ from database : \n", dataa)

        self.link_to_pics = dataa['photo_folder']
        self.sn_of_items_tested = dataa['item_sn_list']

        user_qry = "SELECT * FROM users WHERE user_id = %s"
        user_id = dataa['tech_id']
        try:
            user = self.query_database(user_qry, user_id)[0]
            username = user['user_username']
        except:
            username = ''

        idm = ''
        sdm = ''
        ap = ''
        bnp = ''
        ipl = ''
        nol = ''
        sq = ''
        qtty = ''
        ck_auction = False
        ck_buynow = False
        ck_islot = False
        ck_isnew = False
        ck_isopen = False
        ck_isused = False
        ck_isrefurb = False
        if str(dataa['number_of_items']) == '0':
            sq = ''
        else:
            sq = str(dataa['number_of_items'])
            qtty = str(dataa['number_of_items'])

        if str(dataa['number_of_lots']) == '0':
            nol = ''
        else:
            nol = str(dataa['number_of_lots'])
            qtty = str(dataa['number_of_lots'])

        if str(dataa['items_per_lot']) == '0':
            ipl = ''
        else:
            ipl = str(dataa['items_per_lot'])

        if dataa['shipout_price_by_manager'] == 0.0:
            sdm = ''
        elif dataa['shipout_price_by_manager']:
            sdm = str(dataa['shipout_price_by_manager'])
        else:
            sdm = ''

        if dataa['item_price_by_manager'] == 0.0:
            idm = ''
        elif dataa['item_price_by_manager']:
            idm = str(dataa['item_price_by_manager'])
        else:
            idm = ''

        if dataa['buy_now_price'] == 0.0:
            bnp = ''
        elif dataa['buy_now_price']:
            bnp = str(dataa['buy_now_price'])
        else:
            bnp = ''

        if dataa['auction_price'] == 0.0:
            ap = ''
        elif dataa['auction_price']:
            ap = str(dataa['auction_price'])
        else:
            ap = ''

        if dataa['selling_as_auction'] == 1:
            ck_auction = True
        elif dataa['selling_as_auction'] == 0:
            ck_auction = False

        if dataa['selling_as_buynow'] == 1:
            ck_buynow = True
        elif dataa['selling_as_buynow'] == 0:
            ck_buynow = False

        if dataa['sell_as_lot'] == 1:
            ck_islot = True
        elif dataa['selling_as_auction'] == 0:
            ck_islot = False

        if dataa['new_sealed'] == 1:
            ck_isnew = True
        elif dataa['new_sealed'] == 0:
            ck_isnew = False

        if dataa['new_open_box'] == 1:
            ck_isopen = True
        elif dataa['new_open_box'] == 0:
            ck_isopen = False

        if dataa['used'] == 1:
            ck_isused = True
        elif dataa['used'] == 0:
            ck_isused = False

        if dataa['seller_refurbished'] == 1:
            ck_isrefurb = True
        elif dataa['seller_refurbished'] == 0:
            ck_isrefurb = False

        data_for_pdf_fields = {
            'ez_part': dataa['ez_part_number'],
            'date_created': str(dataa['date_submitted']),
            'item_dollar_manager': idm,
            'shipout_dollar_manager': sdm,
            'auction_price': ap,
            'CheckBox_sold_as_auction': ck_auction,
            'CheckBox_sold_as_buy_now': ck_buynow,
            'CheckBox_sold_as_lot': ck_islot,
            'how_many_lots': nol,
            'individual_quantity': sq,
            'item_weight': str(dataa['item_weight']),
            'po_number': str(dataa['po_number']),
            'brand_name': str(dataa['brand_mfg_name']),
            'model_number': str(dataa['model_no']),
            'title': str(dataa['title']),
            'CheckBox_new': ck_isnew,
            'CheckBox_open': ck_isopen,
            'CheckBox_used': ck_isused,
            'CheckBox_refurbished': ck_isrefurb,
            'additional_pieces': str(dataa['additional_pieces_included']),
            'tech_note': str(dataa['tech_note']),
            'defects': str(dataa['defects']),
            'missing_pieces': str(dataa['pieces_missing']),
            'test_results': str(dataa['key_functions_test_results']),
            'buynow_price': bnp,
            'tech_name': username,
            'items_per_lot': ipl,
            'function_category': dataa['function_category'],
            'cosmetic_category': dataa['cosmetic_category'],
            'sheet_id': str(dataa['sheet_id']) + '-' + qtty,
        }
        print("+++++++++++++++++++ for pdf data = \n", data_for_pdf_fields)
        return data_for_pdf_fields

    def load_gui_form_from_database(self, sheet_id):
        self.set_window_size()
        self.sheetID = sheet_id
        print(sheet_id)
        sheet_info = "SELECT * FROM ConfigSheet WHERE sheet_id = %s"
        data = self.query_database(sheet_info, self.sheetID)[0]
        print("data = ", data)
        self.researched_item_price = data['item_price_researched']
        self.tech_note = data['tech_note']
        self.processed = data['processed']
        self.link_to_pics = data['photo_folder']
        self.sn_of_items_tested = data['item_sn_list']

        user_qry = "SELECT * FROM users WHERE user_id = %s"
        # print(data)
        user_id = data['tech_id']
        try:
            user = self.query_database(user_qry, user_id)[0]
            username = user['user_username']
        except:
            username = ''
        # print(data['sheet_id'])
        print(username)
        if self.loggedin_user_is_active and self.loggedin_user_is_manager:
            self.m_button_list_it.Show()
            self.m_button_reject.Show()

        else:
            self.m_button_print_ez_label.Show()
            self.m_button_print_item_label.Show()

        self.m_button_edit.Show()
        self.m_button_submit.SetLabel("Submit New")
        self.m_button_add_sn.SetLabel("Show SN #")
        self.m_button_add_note.SetLabel("Show Note")
        self.m_button_add_pics.SetLabel("Show Pics")
        self.m_button_add_researched_price.SetLabel("Show Price")
        self.m_textCtrl_tech_name.SetLabel(username)

        self.function_category_selector.SetValue(data['function_category'])
        self.cosmetic_category_selector.SetValue(data['cosmetic_category'])

        self.m_textCtrl_ez_pn.SetValue(data['ez_part_number'])
        if data['shipout_price_by_manager'] == None:
            self.m_textCtrl_shipout_dollar_by_manager.SetValue('')
        elif data['shipout_price_by_manager']:
            self.m_textCtrl_shipout_dollar_by_manager.SetValue(str(data['shipout_price_by_manager']))
        else:
            self.m_textCtrl_shipout_dollar_by_manager.SetValue('')
        if data['item_price_by_manager'] == None:
            self.m_textCtrl_item_dollar_by_manager.SetValue('')
        elif data['item_price_by_manager']:
            self.m_textCtrl_item_dollar_by_manager.SetValue(str(data['item_price_by_manager']))
        else:
            self.m_textCtrl_item_dollar_by_manager.SetValue('')

        self.m_checkBox_is_auction.SetValue(data['selling_as_auction'])
        self.m_checkBox_is_buynow.SetValue(data['selling_as_buynow'])

        if data['buy_now_price'] == None:
            self.m_textCtrl_buy_now_dollar.SetValue('')
        elif data['buy_now_price']:
            self.m_textCtrl_buy_now_dollar.SetValue(str(data['buy_now_price']))
        else:
            self.m_textCtrl_buy_now_dollar.SetValue('')

        if data['auction_price'] != 0:
            self.m_textCtrl_auction_dollar.SetValue('')
        elif data['auction_price']:
            self.m_textCtrl_auction_dollar.SetValue(str(data['auction_price']))
        else:
            self.m_textCtrl_auction_dollar.SetValue('')

        self.m_textCtrl_tech_date_received.SetValue(str(data['date_submitted']))
        self.m_checkBox_sold_lot.SetValue(data['sell_as_lot'])
        if data['number_of_lots'] != 0:
            self.m_textCtrl_lot_numbers.SetValue(str(data['number_of_lots']))
        else:
            self.m_textCtrl_lot_numbers.SetValue('')

        if data['items_per_lot'] != 0:
            self.m_textCtrl_ietms_per_lot.SetValue(str(data['items_per_lot']))
        else:
            self.m_textCtrl_ietms_per_lot.SetValue('')

        if data['number_of_items'] != 0:
            self.m_textCtrl_single_qty.SetValue(str(data['number_of_items']))
        else:
            self.m_textCtrl_single_qty.SetValue('')

        self.m_textCtrl_weight.SetValue(str(data['item_weight']))
        self.m_textCtrl_po_number.SetValue(data['po_number'])

        self.m_textCtrl_brand.SetValue(str(data['brand_mfg_name']))
        self.m_textCtrl_model_number.SetValue(str(data['model_no']))
        self.m_textCtrl_title.SetValue(str(data['title']))

        self.m_checkBox_new_box.SetValue(data['new_sealed'])
        self.m_checkBox_used.SetValue(data['used'])
        self.m_checkBox_open_box.SetValue(data['new_open_box'])
        self.m_checkBox_refurb.SetValue(data['seller_refurbished'])

        self.m_textCtrl_additional_pieces.SetValue(str(data['additional_pieces_included']))
        self.m_textCtrl_missing_pieces.SetValue(str(data['pieces_missing']))
        self.m_textCtrl_defects.SetValue(str(data['defects']))
        self.m_textCtrl_test_results.SetValue(str(data['key_functions_test_results']))
        # if data['processed']:
        #     status = "Sheet ID: " + self.sheetID
        #     self.m_staticText_msg.SetLabel(status)
        # elif not data['processed']:
        #     status = "Sheet ID: " + self.sheetID
        #     self.m_staticText_msg.SetLabel(status)

        if self.tech_note != '':
            self.m_button_add_note.SetBackgroundColour(self.blue_color)

        if self.researched_item_price != '':
            self.m_button_add_researched_price.SetBackgroundColour(self.blue_color)
        if self.sn_of_items_tested != '':
            self.m_button_add_sn.SetBackgroundColour(self.blue_color)

        self.lock_fields()

    def lock_fields(self):
        self.m_textCtrl_tech_name.SetEditable(False)
        self.function_category_selector.Disable()
        self.cosmetic_category_selector.Disable()
        self.m_textCtrl_ez_pn.SetEditable(False)
        self.m_textCtrl_shipout_dollar_by_manager.SetEditable(False)
        self.m_textCtrl_item_dollar_by_manager.SetEditable(False)
        self.m_checkBox_is_auction.Disable()
        self.m_checkBox_is_buynow.Disable()
        self.m_textCtrl_buy_now_dollar.SetEditable(False)
        self.m_textCtrl_auction_dollar.SetEditable(False)
        self.m_textCtrl_tech_date_received.SetEditable(False)
        self.m_checkBox_sold_lot.Disable()
        self.m_textCtrl_lot_numbers.SetEditable(False)
        self.m_textCtrl_ietms_per_lot.SetEditable(False)
        self.m_textCtrl_single_qty.SetEditable(False)
        self.m_textCtrl_weight.SetEditable(False)
        self.m_textCtrl_po_number.SetEditable(False)
        self.m_textCtrl_brand.SetEditable(False)
        self.m_textCtrl_model_number.SetEditable(False)
        self.m_textCtrl_title.SetEditable(False)
        self.m_checkBox_new_box.Disable()
        self.m_checkBox_used.Disable()
        self.m_checkBox_open_box.Disable()
        self.m_checkBox_refurb.Disable()
        self.m_textCtrl_additional_pieces.SetEditable(False)
        self.m_textCtrl_missing_pieces.SetEditable(False)
        self.m_textCtrl_defects.SetEditable(False)
        self.m_textCtrl_test_results.SetEditable(False)

    def unlock_fields(self):
        if self.loggedin_user_is_manager:
            print("user is manager")
            self.m_checkBox_is_buynow.Enable()
            self.m_checkBox_is_auction.Enable()
            self.m_textCtrl_ez_pn.SetEditable(True)
            self.m_textCtrl_shipout_dollar_by_manager.SetEditable(True)
            self.m_textCtrl_item_dollar_by_manager.SetEditable(True)
            self.m_textCtrl_buy_now_dollar.SetEditable(True)
            self.m_textCtrl_auction_dollar.SetEditable(True)

        else:
            print("user is not manager or user is a tech")
            self.m_checkBox_is_buynow.Disable()
            self.m_checkBox_is_auction.Disable()
            self.m_textCtrl_ez_pn.SetEditable(False)
            self.m_textCtrl_shipout_dollar_by_manager.SetEditable(False)
            self.m_textCtrl_item_dollar_by_manager.SetEditable(False)
            self.m_textCtrl_buy_now_dollar.SetEditable(False)
            self.m_textCtrl_auction_dollar.SetEditable(False)

        # self.m_textCtrl_tech_name.SetEditable(True)
        self.function_category_selector.Enable(True)
        self.cosmetic_category_selector.Enable(True)
        self.m_textCtrl_tech_date_received.SetEditable(True)
        self.m_checkBox_sold_lot.Enable()
        self.m_textCtrl_lot_numbers.SetEditable(True)
        self.m_textCtrl_ietms_per_lot.SetEditable(True)
        self.m_textCtrl_single_qty.SetEditable(True)
        self.m_textCtrl_weight.SetEditable(True)
        self.m_textCtrl_po_number.SetEditable(True)
        self.m_textCtrl_brand.SetEditable(True)
        self.m_textCtrl_model_number.SetEditable(True)
        self.m_textCtrl_title.SetEditable(True)
        self.m_checkBox_new_box.Enable()
        self.m_checkBox_used.Enable()
        self.m_checkBox_open_box.Enable()
        self.m_checkBox_refurb.Enable()
        self.m_textCtrl_additional_pieces.SetEditable(True)
        self.m_textCtrl_missing_pieces.SetEditable(True)
        self.m_textCtrl_defects.SetEditable(True)
        self.m_textCtrl_test_results.SetEditable(True)

    def runcommand(self, cmd):
        '''this function runs terminal commands in the background, which are given to it as input when it is called'''
        getcore = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        out, err = getcore.communicate()  # type: (str, str)
        if err:
            print(err)
        return out

    def create_pdf(self, event):
        self.fill_pdf_template(self.configsheet_template_file_path, self.get_data_from_pdf())
        self.add_barcode(self.sheetID + "-" + self.get_qty(), self.configsheet_file_produced_path)
        if os.path.exists(self.configsheet_file_produced_path):
            outpath = ("_{}.pdf".format(next(self.GetParent().gen))).join(
                self.configsheet_file_produced_path.split('.pdf'))
            os.rename(self.configsheet_file_produced_path, outpath)
            # os.rename(self.configsheet_file_produced_path, "{}_".format(next(self.GetParent().gen()))+self.configsheet_file_produced_path)
        else:
            print("The file does not exist")

    def get_data_from_pdf(self):
        if self.m_checkBox_sold_lot.IsChecked():
            qtty = self.m_textCtrl_lot_numbers.GetValue().lstrip()
        else:
            qtty = self.m_textCtrl_single_qty.GetValue().lstrip()
        data = {
            'function_category': self.function_category_selector.GetValue(),
            'cosmetic_category': self.cosmetic_category_selector.GetValue(),
            'ez_part': self.m_textCtrl_ez_pn.GetValue().lstrip().upper(),
            'item_dollar_manager': self.m_textCtrl_item_dollar_by_manager.GetValue().lstrip(),
            'shipout_dollar_manager': self.m_textCtrl_shipout_dollar_by_manager.GetValue().lstrip(),
            'CheckBox_sold_as_auction': self.m_checkBox_is_auction.GetValue(),
            'CheckBox_sold_as_buy_now': self.m_checkBox_is_buynow.GetValue(),
            'auction_price': self.m_textCtrl_auction_dollar.GetValue().lstrip(),
            'buynow_price': self.m_textCtrl_buy_now_dollar.GetValue().lstrip(),
            'tech_id': self.loggedin_user_id,
            'tech_name': self.m_textCtrl_tech_name.GetValue().lstrip(),
            'date_submitted': self.m_textCtrl_tech_date_received.GetValue(),
            'CheckBox_sold_as_lot': self.m_checkBox_sold_lot.GetValue(),
            'sold_as_individual': '',
            'how_many_lots': self.m_textCtrl_lot_numbers.GetValue().lstrip(),
            'items_per_lot': self.m_textCtrl_ietms_per_lot.GetValue().lstrip(),
            'individual_quantity': self.m_textCtrl_single_qty.GetValue().lstrip(),
            'item_weight': self.m_textCtrl_weight.GetValue().lstrip(),
            'po_number': self.m_textCtrl_po_number.GetValue().lstrip(),
            'brand_name': self.m_textCtrl_brand.GetValue().lstrip().upper(),
            'model_number': self.m_textCtrl_model_number.GetValue().lstrip(),
            'title': self.m_textCtrl_title.GetValue().lstrip(),
            'CheckBox_new': self.m_checkBox_new_box.GetValue(),
            'CheckBox_open': self.m_checkBox_open_box.GetValue(),
            'CheckBox_used': self.m_checkBox_used.GetValue(),
            'CheckBox_refurbished': self.m_checkBox_refurb.GetValue(),
            'additional_pieces': self.m_textCtrl_additional_pieces.GetValue().lstrip(),
            'missing_pieces': self.m_textCtrl_missing_pieces.GetValue().lstrip(),
            'defects': self.m_textCtrl_defects.GetValue().lstrip(),
            'test_results': self.m_textCtrl_test_results.GetValue().lstrip(),
            'tech_note': self.tech_note,
            'researched_item_price': self.researched_item_price,
            'sn_of_items_tested': self.sn_of_items_tested,
            'photo_folder_address': self.link_to_pics,
            'date_created': self.m_textCtrl_tech_date_received.GetValue(),
            'model': self.m_textCtrl_model_number.GetValue().lstrip(),
            'sheet_unit': "TID: " + str(self.sheetID),
            'sheet_id': str(self.sheetID) + "-" + qtty
        }
        return data

    def fill_pdf_template(self, template, dt={}):

        ppath = "output\\".join(template.split('templates\\'))
        output = "".join(ppath.split('_template'))

        print(output)
        # self.create_simple_form(manager_form_data, tech_form_data)
        keys_in_pdf_template = ['sheet_id', 'ez_part', 'date_created', 'item_dollar_manager', 'shipout_dollar_manager',
                                'auction_price', 'CheckBox_sold_as_auction', 'CheckBox_sold_as_buy_now',
                                'CheckBox_sold_as_lot', 'how_many_lots', 'individual_quantity', 'item_weight',
                                'po_number', 'brand_name', 'model_number', 'title', 'CheckBox_new', 'CheckBox_open',
                                'CheckBox_used', 'CheckBox_refurbished', 'additional_pieces', 'tech_note', 'defects',
                                'missing_pieces', 'test_results', 'buynow_price', 'tech_name', 'items_per_lot',
                                'function_category', 'cosmetic_category']
        data = dt
        print("Data received to fill pdf template : ", data)
        # for k,v in data.items():
        #     print(k, v)
        print('\nAdding data to pdf...')
        template = pdfrw.PdfReader(template)
        pdf_keys = []
        # template.Root.AcroForm.update(pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))
        for page in template.pages:
            annotations = page['/Annots']
            if annotations is None:
                continue

            for annotation in annotations:
                # print('\n')
                # print(annotation)
                # print('annotation[/v] before = ', annotation['/V'])
                # print('annotation[/AP] before = ', annotation['/AP'])
                # print('annotation[/AS] before = ', annotation['/AS'])
                # print('annotation before = ', annotation)
                if annotation['/Subtype'] == '/Widget':
                    if annotation['/T']:
                        # key = annotation['/T'][1:-1]
                        key = annotation['/T'].to_unicode()
                        if re.search(r'.-[0-9]+', key):
                            key = key[:-2]
                        # print('key = ', key)
                        pdf_keys.append(key)
                        if key in data.keys():
                            print('key found in Data Key = ', data[key])
                            if type(data[key]) == bool:
                                if data[key]:
                                    annotation.update(pdfrw.PdfDict(AS=pdfrw.PdfName('Yes')))
                                    annotation.update(pdfrw.PdfDict(V=pdfrw.PdfName('Yes')))
                            else:
                                annotation.update(
                                    pdfrw.PdfDict(V='{}'.format(data[key])))
                                annotation.update(pdfrw.PdfDict(AP=''))
                        else:
                            print("Key not found:")
                        # print('annotation[/v] after = ', annotation['/V'])
                        # print('annotation[/AP] after = ', annotation['/AP'])
                        # print('annotation[/AS] after = ', annotation['/AS'])

        template.Root.AcroForm.update(pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))
        pdfrw.PdfWriter().write(output, template)
        print('Pdf saved')
        print(pdf_keys)

    def get_qty(self):
        if self.m_checkBox_sold_lot.IsChecked():
            qtty = self.m_textCtrl_lot_numbers.GetValue().lstrip()
        else:
            qtty = self.m_textCtrl_single_qty.GetValue().lstrip()
        return qtty

    def print_ez_label(self, event):

        if self.m_textCtrl_ez_pn.GetValue().lstrip() == '':
            print("EZ Part number field is empty")
            msg1 = "EZ Part number field can not be empty"
            abc = wx.MessageBox(msg1, "STOP!",
                                wx.OK | wx.ICON_STOP, )
            return
        if os.path.exists(self.ezlabel_file_produced_path):
            os.remove(self.ezlabel_file_produced_path)
        else:
            print("The file does not exist")
        self.fill_pdf_template(self.ezlabel_template_file_path, self.get_data_from_pdf())
        self.add_barcode(self.m_textCtrl_ez_pn.GetValue().lstrip(), self.ezlabel_file_produced_path,
                         rect=(0, 10, 430, 40))
        # self.add_barcode_to_pdf(self.m_textCtrl_ez_pn.GetValue().lstrip(), "ez_label_sticker.pdf", x_start = 140, y_start = 115, width = 120, height = 40)
        if platform.system() == 'Darwin':
            cmd_open = """open \output\ez_label_sticker.pdf"""  # open pdf file in default pdf reader
            cmd_del = """rm - rf output.pdf"""
            self.runcommand(cmd_open)
            # self.runcommand(cmd_del)
        elif platform.system() == 'Windows':
            # cmd_open = """start Acrobat.exe /t "ez_label_sticker.pdf"""""  # open pdf file in Acrobat pdf reader ( must be installed on windows already) and prints it and closes pdf reader
            cmd_open = 'start Acrobat.exe "{}"'.format(
                self.ezlabel_file_produced_path)  # open pdf file in Acrobat pdf reader ( must be installed on windows already)
            self.runcommand(cmd_open)
            print("printed")
        else:
            print(platform.system())

    def print_item_labels(self, event):

        if self.m_checkBox_sold_lot.IsChecked():
            items_list = [self.sheetID + '-' + self.m_textCtrl_lot_numbers.GetValue() + '-' + str(i + 1) for i in
                          range(int(self.m_textCtrl_lot_numbers.GetValue()))]
        else:
            items_list = [self.sheetID + '-' + self.m_textCtrl_single_qty.GetValue() + '-' + str(i + 1) for i in
                          range(int(self.m_textCtrl_single_qty.GetValue()))]
        print(items_list)
        if len(items_list) > 1:
            dlg = wx.MessageDialog(None, "Do you want to print labels for all {} items?".format(len(items_list)),
                                   'Caution', wx.YES_NO | wx.ICON_QUESTION)
            result = dlg.ShowModal()
            if result == wx.ID_YES:
                for j in items_list:
                    ezbar.createBarCodes(j)
            else:
                ezbar.createBarCodes(items_list[0])
        else:
            ezbar.createBarCodes(items_list[0])

    def print(self, event):

        if os.path.exists(self.configsheet_file_produced_path):
            os.remove(self.configsheet_file_produced_path)
        else:
            print("The file does not exist")
        self.fill_pdf_template(self.configsheet_template_file_path, self.get_data_from_pdf())
        self.add_barcode(self.sheetID + "-" + self.get_qty(), self.configsheet_file_produced_path)
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

        # self.Destroy()
        return

    def update_database(self, sql_check, sql_update):
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
                """find if record already exists for this sheet number"""
                # cursor.execute(
                #     "SELECT sheet_id, COUNT(*) FROM `ConfigSheet` WHERE sheet_id = %s GROUP BY sheet_id",
                #     (sheet,))
                cursor.execute(sql_check)

                # gets the number of rows returned by database for the above sql command
                row_count = cursor.rowcount
                print("number of rows returned by database for this sheet number: {}".format(row_count))

                if row_count == 0:
                    print("No record found for this sheet")

                else:
                    """Update the record """
                    cursor.execute(sql_update)
                    # connection is not autocommit by default.So you must commit to save your changes.
                    connection.commit()
                    # Some things that are done to the form after the submission of data to database
                    print('Connection committed')

        except pymysql.err.OperationalError as error:
            print(error)

        finally:
            connection.close()

    def get_ez(self):
        dlg = wx.TextEntryDialog(self, 'Please enter ez part number', 'Part # Required')
        dlg.SetValue("")
        if dlg.ShowModal() == wx.ID_OK:
            ez = dlg.GetValue().lstrip()
            print('You entered: %s\n' % dlg.GetValue())
        else:
            ez = ''
        dlg.Destroy()
        return ez

    def list_it(self, event):
        if self.m_textCtrl_ez_pn.GetValue().lstrip() == '':
            ez = self.get_ez()
            if ez == '':
                return
            else:
                pass
        else:
            ez = self.m_textCtrl_ez_pn.GetValue().lstrip()

        sql_chk = "SELECT sheet_id, COUNT(*) FROM `ConfigSheet` WHERE sheet_id = {} GROUP BY sheet_id".format(
            self.sheetID)
        sql_upd = "UPDATE `ConfigSheet` SET date_listed = '{}', ez_part_number = '{}', listed = True, new = False, processed = True WHERE sheet_id = {}".format(
            self.date_today,
            ez, self.sheetID)
        # print(sql_chk, "\n", sql_upd)
        self.update_database(sql_chk, sql_upd)

        self.Parent.refresh()
        self.Destroy()

    def reject_it(self, event):
        sql_chk = "SELECT sheet_id, COUNT(*) FROM `ConfigSheet` WHERE sheet_id = {} GROUP BY sheet_id".format(
            self.sheetID)
        sql_upd = "UPDATE `ConfigSheet` SET date_rejected = '{}', rejected = True, new = False, listed = False, processed = True WHERE sheet_id = {}".format(
            self.date_today,
            self.sheetID)
        # print(sql_chk, "\n", sql_upd)
        self.update_database(sql_chk, sql_upd)
        self.Parent.refresh()
        self.Destroy()

    def record_exists(self, qry, val):
        rslt = len(self.query_database(qry, val))
        if rslt > 0:
            return True
        else:
            return False

    def add_serial_numbers(self, event):
        print(self.sn_of_items_tested)
        lbl = self.m_button_add_sn.GetLabel()
        if lbl == "Add SN #":
            # Create text input
            dlg = MyTextEntryDialog(self, 'Serial Numbers', 'Scan in the SN of items here')
            dlg.SetValue("")
            if dlg.ShowModal() == wx.ID_OK:
                print('You entered: %s\n' % dlg.GetValue())
            self.sn_of_items_tested = dlg.GetValue()
            print(self.sn_of_items_tested)
            quantity = int(self.get_qty())
            print("Total items or lots in this sheet: ", quantity)
            serials = dlg.GetValue().split('\n')
            if serials[-1] != "":
                sn_in_sn_list = serials
            else:
                sn_in_sn_list = serials[:-1]
            print("Serial numbers entered : ", sn_in_sn_list)
            if quantity != len(sn_in_sn_list):
                mesg = f"Qty of SN scanned are not equal to number of items in this sheet!\nNumber of items: {quantity}\nNumber of SN# scanned: {len(sn_in_sn_list)}."
                wx.MessageBox(mesg, 'Mismatch', wx.OK | wx.ICON_STOP)
                return

            dlg.Destroy()
        elif lbl == "Edit SN #":

            # Create text input
            dlg = MyTextEntryDialog(self, 'Serial Numbers', 'Scan in the SN of items here')
            dlg.SetValue(self.sn_of_items_tested)
            if dlg.ShowModal() == wx.ID_OK:
                print('You entered: %s\n' % dlg.GetValue())
            self.sn_of_items_tested = dlg.GetValue()
            print(self.sn_of_items_tested)
            quantity = int(self.get_qty())
            print("Total items or lots in this sheet: ", quantity)
            serials = dlg.GetValue().split('\n')
            if serials[-1] != "":
                sn_in_sn_list = serials
            else:
                sn_in_sn_list = serials[:-1]
            print("Serial numbers entered : ", sn_in_sn_list)
            if quantity != len(sn_in_sn_list):
                mesg = f"Qty of SN scanned are not equal to number of items in this sheet!\nNumber of items: {quantity}\nNumber of SN# scanned: {len(sn_in_sn_list)}."
                wx.MessageBox(mesg, 'Mismatch', wx.OK | wx.ICON_STOP)
                return

            dlg.Destroy()
        elif lbl == "Show SN #":

            # Create text input
            dlg = MyTextEntryDialog(self, 'Serial Numbers', 'Serial No for items in this Config Sheet')
            dlg.SetValue(self.sn_of_items_tested)

            if dlg.ShowModal() == wx.ID_OK:
                dlg.Destroy()

    def add_researched_price(self, event):
        print(self.researched_item_price)
        lbl = self.m_button_add_researched_price.GetLabel()
        if lbl == "Add Price":
            # Create text input
            dlg = wx.TextEntryDialog(self, 'Enter the average selling price of this item here', 'Item Price')
            dlg.SetValue("")
            if dlg.ShowModal() == wx.ID_OK:
                print('You entered: %s\n' % dlg.GetValue())
            self.researched_item_price = float(dlg.GetValue())
            print(self.researched_item_price)

            dlg.Destroy()
        elif lbl == "Edit Price":
            # Create text input
            dlg = wx.TextEntryDialog(self, 'Enter the average selling price of this item here', 'Item Price')
            dlg.SetValue(str(self.researched_item_price))
            if dlg.ShowModal() == wx.ID_OK:
                print('You entered: %s\n' % dlg.GetValue())
            self.researched_item_price = float(dlg.GetValue())
            print(self.researched_item_price)

            dlg.Destroy()
        elif lbl == "Show Price":
            # Create text input
            dlg = wx.TextEntryDialog(self, 'Average selling price of this item', 'Item Price')
            dlg.SetValue(str(self.researched_item_price))

            if dlg.ShowModal() == wx.ID_OK:
                dlg.Destroy()

    def shoot_pic(self, pic_no):
        """# initializing the camera"""
        pygame.camera.init()
        """# make the list of all available cameras"""
        camlist = pygame.camera.list_cameras()
        print(camlist)
        """# if camera is detected or not"""
        if camlist:
            """initializing the cam variable with default camera"""
            cam = pygame.camera.Camera(camlist[0], (1280, 720))
            """opening the camera"""
            cam.start()
            """capturing the single image"""
            image = cam.get_image()
            """saving the image"""
            pic_name = "{}.jpg".format(pic_no)
            pygame.image.save(image, pic_name)

        else:
            print("No camera on current device")
            pic_name = ""
        return pic_name

    def add_photo_to_smb_folder(self, folder):
        mysmb = smb('RHEL8', '192.168.1.14', 'Anonymous')
        mysmb.connect_with_smb_share()
        t = len(mysmb.get_img_list(folder)) + 1
        if t < 13:
            img = self.shoot_pic(t)
            mysmb.transfer_image(folder, img, "{}.jpg".format(t))

            # self.m_bitmap_1.SetBitmap(wx.Image(img, wx.BITMAP_TYPE_ANY).ConvertToBitmap())
            # self.bitmap_list[t].SetBitmap(wx.Image(img, wx.BITMAP_TYPE_ANY).ConvertToBitmap())
            print("Picture # {} with name {} is added to the folder {}".format(t, img, folder))
            wx.MessageBox("Picture # {} with name {} is added to the folder {}".format(t, img, folder), 'Info',
                          wx.OK | wx.ICON_INFORMATION)
            cmd = "rm -rf {}.jpg".format(t)
            self.runcommand(cmd)
        else:
            wx.MessageBox('Max limit reached.\n Only 12 pics can be added per Config Sheet', 'Info',
                          wx.OK | wx.ICON_INFORMATION)
        mysmb.close_connection()
        cmd2 = "open smb://GUEST:''@192.168.1.14/Anonymous/{}".format(self.sheetID)
        self.runcommand(cmd2)

    def add_pictures(self, event):
        print(self.link_to_pics)
        lbl = self.m_button_add_pics.GetLabel()

        if lbl == "Take Pics":
            new_dir = self.make_smb_dir()

            # cmd = "open smb://GUEST:''@192.168.1.14/Anonymous/{}".format(self.sheetID)
            # self.runcommand(cmd)
            self.add_photo_to_smb_folder(new_dir)

            #
            # frame = pFolder.Pictures(self)
            # frame.folder_id = new_dir
            # frame.on_load()

        elif lbl == "Show Pics":
            mysmb = smb('RHEL8', '192.168.1.14', 'Anonymous')
            mysmb.connect_with_smb_share()
            if mysmb.dir_exists(self.sheetID):
                mysmb.close_connection()
                cmd = "open smb://GUEST:''@192.168.1.14/Anonymous/{}".format(self.sheetID)
                self.runcommand(cmd)

                # frame = pFolder.Pictures(self)
                # frame.folder_id = self.sheetID
                # frame.show_pictures()

            else:
                wx.MessageBox('No pictures found!', 'Info',
                              wx.OK | wx.ICON_INFORMATION)

    def add_note(self, event):
        print(self.tech_note)
        lbl = self.m_button_add_note.GetLabel()
        if lbl == "Add Note":

            # Create text input
            dialog = MyTextEntryDialog(self, 'Tech Notes', 'Enter tech notes here')

            # dialog.Center()
            # dialog.SetValue('Value')

            if dialog.ShowModal() == wx.ID_OK:
                print('You entered: %s\n' % dialog.GetValue())
                self.tech_note = dialog.GetValue()
                print(self.tech_note)

            dialog.Destroy()

        elif lbl == "Edit Note":

            # Create text input
            dialog = MyTextEntryDialog(self, 'Tech Notes', 'Edit the tech note')
            # dialog.Center()
            self.tech_note = self.tech_note + "Sheet ID : " + self.sheetID + "\n"
            dialog.SetValue(self.tech_note)
            if dialog.ShowModal() == wx.ID_OK:
                print('You entered: %s\n' % dialog.GetValue())
                self.tech_note = dialog.GetValue()
                print(self.tech_note)

            dialog.Destroy()

        elif lbl == "Show Note":

            # Create text input
            dlg = MyTextEntryDialog(self, 'Tech Notes', 'Here is the saved note')
            dlg.SetValue(self.tech_note)

            if dlg.ShowModal() == wx.ID_OK:
                dlg.Destroy()

    def get_screen_size(self):
        view_width, view_height = pyautogui.size()

        screen_size = [view_width, view_height]
        print("Screen dimensions", screen_size)
        return (view_width, view_height)

    def set_window_size(self):
        w, h = self.get_screen_size()
        self.Size = (1220, h - 80)
        self.Centre()

    def adjust_configsheet(self):
        self.SetSize(wx.Size(1260, 720))
        self.SetSizeHints(wx.DefaultSize, wx.Size(1260, 1080))

    def email_pdf_discarded(self, event):
        """This function sends email and attach the pdf file(error is that pdf file does not get proper name and extension in the sent email"""
        # DISCARDED FUNCTION
        mail_content = '''Hello,
        This is a test mail.
        In this mail we are sending some attachments.
        The mail is sent using Python SMTP library.
        Thank You
        '''
        # The mail addresses and password
        sender_address = 'bciebayconfigsheet@gmail.com'
        sender_pass = ''
        receiver_address = 'bciebayconfigsheet@gmail.com'
        # Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'This is a test mail sent from ConfigSheet Dashboard. It has an attachment.'
        # The subject line
        # The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'plain'))
        attach_file_name = "Ebay Config Sheet Rev1.4.pdf"
        attach_file = open(attach_file_name, 'rb')  # Open the file as binary mode
        payload = MIMEBase('application', 'octate-stream')
        payload.set_payload((attach_file).read())
        encoders.encode_base64(payload)  # encode the attachment
        # add payload header with filename
        payload.add_header('Content-Decomposition', 'attachment', filename="Ebay Config Sheet Rev1.4.pdf")
        message.attach(payload)
        # Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
        session.starttls()  # enable security
        session.login(sender_address, sender_pass)  # login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        # Upload (save) the email to the "Sent" mailbox.

        session.quit()
        print('Mail Sent')

    def email_pdf(self, event):
        """This function used installed outloook express to send emails. So record of sent emails is also made automatically in outlook express"""
        if platform.system() == 'Windows':
            if os.path.exists(self.configsheet_file_produced_path):
                os.remove(self.configsheet_file_produced_path)
            else:
                print("The file does not exist")
            self.fill_pdf_template(self.configsheet_template_file_path, self.get_data_from_pdf())
            self.add_barcode(self.sheetID + "-" + self.get_qty(), self.configsheet_file_produced_path)

            sheet_data = self.read_tech_form()
            cwd = os.getcwd()
            print(cwd)
            # attachment_path = cwd + "\\Ebay Config Sheet Rev1.5.pdf"
            attachment_path = self.configsheet_file_produced_path
            print(attachment_path)
            to_email_address = self.to_email
            print("To email address : ", to_email_address)
            try:
                import win32com.client  # for this to work, install pypiwin32 module using pip first
                outlook = win32com.client.Dispatch('outlook.application')
            except Exception as e:
                print("Please make sure you have outlook express installed and configured on this machine.")
                return

            if not sheet_data['sold_as_lot']:
                qty = str(sheet_data['single_quantity']) + "    "
            else:
                qty = str(sheet_data['number_of_lots']) + " lot of " + str(sheet_data['items_per_lot']) + "    "

            email_title = "QTY=" + qty + str(sheet_data['item_title'])
            email_body = sheet_data['tech_note']

            def send_email(outlook, to_email_address, attachment_path):
                mail = outlook.CreateItem(0)
                mail.To = to_email_address
                mail.Subject = email_title
                mail.Body = email_body
                if attachment_path:
                    mail.Attachments.Add(Source=attachment_path)

                mail.Send()

            send_email(outlook, to_email_address, attachment_path)

            print("email sent")
            msg = "Config Sheet successfully emailed."
            abc = wx.MessageBox(msg, "Success!",
                                wx.OK | wx.ICON_INFORMATION, )

            self.Destroy()
        elif platform.system() == 'Darwin':
            if os.path.exists(self.configsheet_file_produced_path):
                os.remove(self.configsheet_file_produced_path)
            else:
                print("The file does not exist")
            self.fill_pdf_template(self.configsheet_template_file_path, self.get_data_from_pdf())
            # self.add_barcode(self.sheetID + "-" + self.get_qty(), "Ebay Config Sheet Rev1.5.pdf")
            self.add_barcode(self.sheetID + "-" + self.get_qty(), self.configsheet_file_produced_path)

            msg = "You need to manually email the pdf file."
            abc = wx.MessageBox(msg, "Alert!",
                                wx.OK | wx.ICON_INFORMATION, )

    def load_discont_list(self):
        """ loads a list of discontinued models from database """

        def query_database(qry, val):
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
                    """find if record exists for this username"""
                    cursor.execute(
                        qry,
                        (val,))

                    info = cursor.fetchall()
                    # print(info)

            except pymysql.err.OperationalError as error:
                print(error)

            finally:
                connection.close()
            return info

        qry = "SELECT * from `discontinue_items` WHERE is_active=%s"
        val = (True)
        data = query_database(qry, val)
        df = pd.DataFrame(data)
        return list(df['item_model']), df

        #
        #
        # dlg = MyDiscontinueViewer(self, 'Discontinued Items', 'If you see any of these items, Deman them.')
        # dlg.SetValue(d_items)
        # if dlg.ShowModal() == wx.ID_OK:
        #     print('You entered: %s\n' % dlg.GetValue())
        # # self.sn_of_items_tested = dlg.GetValue()
        # # print(self.sn_of_items_tested)
        #
        # dlg.Destroy()

    def verify_discontinue(self):
        # item = self.m_textCtrl_model_number.GetValue().lstrip().upper()
        item = self.m_textCtrl_title.GetValue().lstrip().upper()
        try:
            lst = item.split(' ')
        except:
            lst = item
        print(lst)
        discon, df = self.load_discont_list()
        out1 = []
        for i in lst:
            if i in discon:
                condition = ''.join(df[df['item_model'] == i]['discontinue_condition'].values)
                msg = "Discontinued item:  {} - {}\nDo you still want to create config sheet for it?".format(i,
                                                                                                             condition)
                dlg = wx.MessageDialog(None, msg, "STOP!", wx.YES_NO | wx.ICON_QUESTION)
                result = dlg.ShowModal()
                # self.m_textCtrl_model_number.SetFocusFromKbd()
                if result == wx.ID_YES:
                    pass
                else:
                    out1.append("No")
            else:
                pass

        if len(out1) >= 1:
            return 'No'
        else:
            return 'Yes'

#
# if __name__ == '__main__':
#     app = wx.App()
#     frame = MyConfigSheet(None)
#     frame.set_window_size()
#     frame.Show()
#     app.MainLoop()
