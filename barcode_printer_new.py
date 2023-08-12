# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-40-g8042f487)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################
import os
import platform
import subprocess

import wx
import wx.html
import wx.xrc
from reportlab.graphics.barcode import code128
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from company_logo import *


###########################################################################
## Class LabelSheetPrinter
###########################################################################

class LabelSheetPrinter(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=-1, title="ezPro - Print Barcode Sheets", pos=wx.DefaultPosition,
                          size=wx.Size(1200, 760), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.start = 1
        self.end = 81
        self.total_sheets = 1
        self.po_no = None
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        # convert the embedded image bytes into images for use in gui
        self.logo_med = wx.Image(l_med.GetImage()).ConvertToBitmap()
        self.logo_lrg = wx.Image(l_lar.GetImage()).ConvertToBitmap()

        # sets icon for title bar for current frame
        self.SetIcon(wx.Icon(self.logo_lrg))

        mainSizer = wx.BoxSizer(wx.HORIZONTAL)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.left_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        leftPanel_sizer = wx.BoxSizer(wx.VERTICAL)
        leftPanel_sizer.Add((0, 40), 0, wx.EXPAND, 1)
        self.m_bitmap1 = wx.StaticBitmap(self.left_panel, wx.ID_ANY, wx.Bitmap(self.logo_lrg), wx.DefaultPosition, wx.DefaultSize,
                                         0)
        leftPanel_sizer.Add(self.m_bitmap1, 0, wx.ALIGN_CENTER_HORIZONTAL, 1)

        leftPanel_sizer.Add((0, 50), 0, wx.EXPAND, 5)

        bSizer_txt_input_1 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1 = wx.StaticText(self.left_panel, wx.ID_ANY, u"Key :", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)

        bSizer_txt_input_1.Add(self.m_staticText1, 1, wx.ALL, 5)

        self.m_textCtrl_po_number = wx.TextCtrl(self.left_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        bSizer_txt_input_1.Add(self.m_textCtrl_po_number, 1, wx.ALL, 5)

        leftPanel_sizer.Add(bSizer_txt_input_1, 0, wx.ALIGN_CENTER_HORIZONTAL, 1)

        bSizer_txt_input_2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText11 = wx.StaticText(self.left_panel, wx.ID_ANY, u"No of pages : ", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)

        bSizer_txt_input_2.Add(self.m_staticText11, 1, wx.ALL, 5)

        self.m_textCtrl_no_of_sheets = wx.TextCtrl(self.left_panel, wx.ID_ANY, '1', wx.DefaultPosition,
                                                   wx.DefaultSize, 0)
        bSizer_txt_input_2.Add(self.m_textCtrl_no_of_sheets, 1, wx.ALL, 5)

        leftPanel_sizer.Add(bSizer_txt_input_2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText4 = wx.StaticText(self.left_panel, wx.ID_ANY, u"__ For partial sheets use following __", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)

        leftPanel_sizer.Add(self.m_staticText4, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 20)

        bSizer_txt_input_21 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText111 = wx.StaticText(self.left_panel, wx.ID_ANY, u"From (first number): ", wx.DefaultPosition, wx.DefaultSize,
                                             0)
        self.m_staticText111.Wrap(-1)

        bSizer_txt_input_21.Add(self.m_staticText111, 1, wx.ALL, 5)

        self.m_textCtrl_from = wx.TextCtrl(self.left_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        bSizer_txt_input_21.Add(self.m_textCtrl_from, 1, wx.ALL, 5)

        leftPanel_sizer.Add(bSizer_txt_input_21, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer_txt_input_22 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText112 = wx.StaticText(self.left_panel, wx.ID_ANY, u"To (last number): ", wx.DefaultPosition, wx.DefaultSize,
                                             0)
        self.m_staticText112.Wrap(-1)

        bSizer_txt_input_22.Add(self.m_staticText112, 1, wx.ALL, 5)

        self.m_textCtrl_to = wx.TextCtrl(self.left_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                         0)
        bSizer_txt_input_22.Add(self.m_textCtrl_to, 1, wx.ALL, 5)

        leftPanel_sizer.Add(bSizer_txt_input_22, 0, wx.ALIGN_CENTER, 5)

        leftPanel_sizer.Add((0, 50), 0, wx.EXPAND, 5)
        button_groupSizer1 = wx.BoxSizer(wx.HORIZONTAL)
        self.m_button_generate = wx.Button(self.left_panel, wx.ID_ANY, u"Generate", wx.DefaultPosition, wx.DefaultSize,
                                           0)
        button_groupSizer1.Add(self.m_button_generate, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_button_print = wx.Button(self.left_panel, wx.ID_ANY, u"Print", wx.DefaultPosition, wx.DefaultSize, 0)
        button_groupSizer1.Add(self.m_button_print, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        button_groupSizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.m_button_reset = wx.Button(self.left_panel, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize, 0)
        button_groupSizer2.Add(self.m_button_reset, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        self.m_button_settings = wx.Button(self.left_panel, wx.ID_ANY, u"Settings", wx.DefaultPosition, wx.DefaultSize, 0)
        button_groupSizer2.Add(self.m_button_settings, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        leftPanel_sizer.Add(button_groupSizer1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)
        leftPanel_sizer.Add(button_groupSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)
        leftPanel_sizer.Add((0, 160), 0, wx.EXPAND, 5)

        developer_Sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1121 = wx.StaticText(self.left_panel, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize,
                                             0)
        self.m_staticText1121.Wrap(-1)

        developer_Sizer.Add(self.m_staticText1121, 0, wx.ALL, 5)
        self.m_staticText11211 = wx.StaticText(self.left_panel, wx.ID_ANY, u"", wx.DefaultPosition,
                                              wx.DefaultSize,
                                              0)
        self.m_staticText11211.Wrap(-1)

        developer_Sizer.Add(self.m_staticText11211, 0, wx.ALL, 5)
        developer_Sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.m_staticText112112 = wx.StaticText(self.left_panel, wx.ID_ANY, u"", wx.DefaultPosition,
                                               wx.DefaultSize,
                                               0)
        self.m_staticText112112.Wrap(-1)

        developer_Sizer2.Add(self.m_staticText112112, 0, wx.ALL, 5)

        self.m_staticText1121122 = wx.StaticText(self.left_panel, wx.ID_ANY, u"", wx.DefaultPosition,
                                                wx.DefaultSize,
                                                0)
        self.m_staticText1121122.Wrap(-1)

        developer_Sizer2.Add(self.m_staticText1121122, 0, wx.ALL, 5)

        leftPanel_sizer.Add(developer_Sizer, 0, wx.ALIGN_LEFT, 5)
        leftPanel_sizer.Add(developer_Sizer2, 0, wx.ALIGN_LEFT, 5)
        # leftPanel_sizer.Add((0, 10), 0, wx.EXPAND, 5)
        self.left_panel.SetSizer(leftPanel_sizer)
        self.left_panel.Layout()
        leftPanel_sizer.Fit(self.left_panel)
        bSizer2.Add(self.left_panel, 1, wx.EXPAND | wx.ALL, 0)

        mainSizer.Add(bSizer2, 1, wx.EXPAND, 0)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.right_panel_scrolled = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                      wx.HSCROLL | wx.VSCROLL)
        self.right_panel_scrolled.SetScrollRate(5, 5)
        bSizer14 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText8 = wx.StaticText(self.right_panel_scrolled, wx.ID_ANY, u"Preview", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)

        bSizer14.Add(self.m_staticText8, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.m_htmlWin1 = wx.html.HtmlWindow(self.right_panel_scrolled, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                             wx.html.HW_SCROLLBAR_AUTO)
        bSizer14.Add(self.m_htmlWin1, 1, wx.ALL | wx.EXPAND, 5)

        self.right_panel_scrolled.SetSizer(bSizer14)
        self.right_panel_scrolled.Layout()
        bSizer14.Fit(self.right_panel_scrolled)
        bSizer3.Add(self.right_panel_scrolled, 1, wx.EXPAND | wx.ALL, 0)

        mainSizer.Add(bSizer3, 6, wx.EXPAND, 5)

        self.SetSizer(mainSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button_generate.Bind(wx.EVT_BUTTON, self.generate_pdf)
        self.m_button_print.Bind(wx.EVT_BUTTON, self.print_pdf)
        self.m_button_reset.Bind(wx.EVT_BUTTON, self.reset)
        # self.m_button_settings.Bind(wx.EVT_BUTTON, self.pdf_to_png)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def generate_pdf(self, event):
        """
            Create barcode examples and embed in a PDF
            """
        rows = 20
        colms = 4
        c = canvas.Canvas("barcodes.pdf", pagesize=letter)

        try:
            self.po_no = int(self.m_textCtrl_po_number.GetValue().lstrip())
        except ValueError as e:
            wx.MessageBox("Please enter a number in Key field", "Error!", wx.OK | wx.ICON_ERROR, )
            self.m_textCtrl_po_number.SelectAll()
            return

        if self.m_textCtrl_no_of_sheets.GetValue().lstrip() != "":
            try:
                self.total_sheets = int(self.m_textCtrl_no_of_sheets.GetValue().lstrip())
            except ValueError as e:
                wx.MessageBox("Please enter a number in total sheets field", "Error!", wx.OK | wx.ICON_ERROR, )
                self.m_textCtrl_no_of_sheets.SelectAll()
                return
            self.start = 1
            self.end = 80*self.total_sheets+1
        else:
            self.total_sheets = 1
            try:
                self.start = int(self.m_textCtrl_from.GetValue().lstrip())
            except ValueError as e:
                wx.MessageBox("Please enter a number in 'from' field", "Error!", wx.OK | wx.ICON_ERROR, )
                self.m_textCtrl_from.SelectAll()
                return
            try:
                self.end = int(self.m_textCtrl_to.GetValue().lstrip()) + 1
            except ValueError as e:
                wx.MessageBox("Please enter a number in 'to' field", "Error!", wx.OK | wx.ICON_ERROR, )
                self.m_textCtrl_to.SelectAll()
                return



        codes = [str(self.po_no) + '-' + str(i) for i in range(self.start, self.end)]

        # codes = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

        x = 42.51968503937008

        # y = 742.6771653543308
        y = 750

        n = 1
        col = 1
        for code in codes:
            code128.Code128(code).drawOn(c, x, y)
            # c.drawString(x + 24, y - 10, str(code))
            c.drawString(x + 16, y - 10, str(code)) # Draws string under the codes
            # y = y - 36.425196850393704 #12.85 * mm
            y = y - 36
            n += 1
            if n > rows:
                x += 147.40157480314963 #52 * mm
                y = 750
                n = 1
                col += 1

            if col > colms:
                c.showPage()
                x = 42.51968503937008
                y = 750
                col = 1
        c.save()
        wx.Yield()
        self.pdf_to_png()

    def print_pdf(self, event):
        if os.path.exists("barcodes.pdf"):
            if platform.system() == 'Darwin':
                cmd_open = """open barcodes.pdf"""  # open pdf file in default pdf reader
                self.runcommand(cmd_open)

            elif platform.system() == 'Windows':
                cmd_open = """start Acrobat.exe /t "barcodes.pdf"""""  # open pdf file in Acrobat pdf reader ( must be installed on windows already) and prints it and closes pdf reader
                # cmd_open = """start Acrobat.exe "Ebay Config Sheet Rev1.5.pdf"""""  # open pdf file in Acrobat pdf reader ( must be installed on windows already)
                self.runcommand(cmd_open)
            else:
                print(platform.system())
            return
        else:
            wx.MessageBox("Please generate a barcode sheet first", "Error!", wx.OK | wx.ICON_ERROR, )

    def runcommand(self, cmd):
        '''this function runs terminal commands in the background, which are given to it as input when it is called'''
        getcore = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        out, err = getcore.communicate()  # type: (str, str)
        if err:
            print(err)
        return out


    def reset(self, event):
        self.m_textCtrl_to.SetValue("")
        self.m_textCtrl_from.SetValue("")
        self.m_textCtrl_no_of_sheets.SetValue("")
        self.m_textCtrl_po_number.SetValue("")

    def pdf_to_png(self):
        import fitz

        dpi = 100  # choose desired dpi here
        zoom = dpi / 72  # zoom factor, standard: 72 dpi
        magnify = fitz.Matrix(zoom, zoom)  # magnifies in x, resp. y direction
        doc = fitz.open('barcodes.pdf')  # open document
        img_files = []
        for page in doc:
            pix = page.get_pixmap(matrix=magnify)  # render page to an image
            fname = f"page-{page.number}.png"
            pix.save(fname)
            img_files.append("<img src='{}'>".format(fname))

        print(img_files)
        webpage = ""
        for i in img_files:
            webpage = webpage + i + " <hr> "
        print(webpage)
        self.m_htmlWin1.SetPage(
            webpage


        )


#
# if __name__ == '__main__':
#     app = wx.App()
#     frame = LabelSheetPrinter(None)
#     frame.Show()
#     app.MainLoop()
