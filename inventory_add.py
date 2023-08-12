# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-231-gdf7791bf)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

from datetime import datetime as dt
from company_logo import *
import pymysql.cursors
import wx
import wx.xrc


###########################################################################
## Class Inventory_location
###########################################################################

class Add_Inventory_items(wx.Frame):
    date_today = str(dt.now())
    ip = ''  # IP address of the database server
    user = ''  # limited access username of the database
    password = ''  # limited access user's pw
    db = ''  # database name
    bins = []
    loggedin_user_username = ''

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"ezPro - Inventory Management", pos=wx.DefaultPosition,
                          size=wx.Size(500, 600), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.logo_med = wx.Image(l_med.GetImage()).ConvertToBitmap()
        self.SetIcon(wx.Icon(self.logo_med))
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer111 = wx.BoxSizer(wx.VERTICAL)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Add items",
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)

        self.m_staticText1.SetFont(
            wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande"))

        bSizer2.Add(self.m_staticText1, 1, wx.ALIGN_BOTTOM | wx.ALL, 5)

        self.m_staticText2 = wx.StaticText(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText2.Wrap(-1)

        bSizer2.Add(self.m_staticText2, 2, wx.ALL, 5)

        self.m_bitmap_logo = wx.StaticBitmap(self.m_panel1, wx.ID_ANY, wx.Bitmap(self.logo_med),
                                             wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_bitmap_logo, 0, wx.ALL, 5)

        bSizer111.Add(bSizer2, 0, wx.EXPAND, 5)

        self.m_staticline1 = wx.StaticLine(self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        bSizer111.Add(self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)


        bSizer5_0 = wx.BoxSizer(wx.VERTICAL)
        # bSizer5_0.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_staticText5 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"PN#:", wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText5.Wrap(-1)

        self.m_staticText5.SetFont(
            wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande"))

        bSizer5_0.Add(self.m_staticText5, 0, wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl_item_ez_no = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                 wx.Size(150, 40), 0)
        self.m_textCtrl_item_ez_no.SetFont(
            wx.Font(14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande"))
        bSizer5_0.Add(self.m_textCtrl_item_ez_no, 0, wx.ALL | wx.EXPAND, 5)

        # bSizer5_0.Add((0, 0), 1, wx.EXPAND, 5)
        bSizer3.Add(bSizer5_0, 0, wx.ALL, 0)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        # bSizer5.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_staticText3 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Bin# :", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)

        self.m_staticText3.SetFont(
            wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande"))

        bSizer5.Add(self.m_staticText3, 0, wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl_bin = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(150, 40),
                                          0)
        self.m_textCtrl_bin.SetFont(
            wx.Font(14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande"))
        bSizer5.Add(self.m_textCtrl_bin, 0, wx.ALL | wx.EXPAND, 5)

        # bSizer5.Add((0, 5), 1, wx.EXPAND, 5)

        bSizer3.Add(bSizer5, 0, wx.ALL, 0)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        # bSizer6.Add((0, 5), 1, wx.EXPAND, 5)

        bSizer_h = wx.BoxSizer(wx.HORIZONTAL)
        bSizer_h.Add(bSizer3, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText4 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"SN of items:", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)

        self.m_staticText4.SetFont(
            wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande"))

        bSizer6.Add(self.m_staticText4, 0, wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl_item_id = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                              wx.Size(360, 340), style=wx.TE_MULTILINE)
        bSizer6.Add(self.m_textCtrl_item_id, 0, wx.ALL | wx.EXPAND, 5)

        # bSizer6.Add((0, 5), 1, wx.EXPAND, 5)
        self.m_staticText_info = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Using default Sheet number (i.e. 111111)", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText_info.Wrap(-1)

        self.m_staticText_info.SetFont(
            wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Lucida Grande"))

        bSizer6.Add(self.m_staticText_info, 0, wx.ALL | wx.EXPAND, 5)

        # self.m_checkBox_cb1 = wx.CheckBox(self.m_panel1, label='Use default Sheet number (i.e. 121212)')
        #
        # bSizer6.Add(self.m_checkBox_cb1, 0, wx.ALL | wx.EXPAND, 5)
        # self.m_checkBox_cb1.SetValue(True)

        bSizer_h.Add(bSizer6, 0, wx.ALL | wx.EXPAND, 0)

        bSizer111.Add(bSizer_h, 0, wx.ALL | wx.EXPAND, 5)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText6 = wx.StaticText(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText6.Wrap(-1)

        bSizer8.Add(self.m_staticText6, 0, wx.ALL, 5)

        bSizer4.Add(bSizer8, 1, wx.EXPAND, 10)

        bSizer11 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText7 = wx.StaticText(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText7.Wrap(-1)

        bSizer11.Add(self.m_staticText7, 0, wx.ALL, 5)

        bSizer4.Add(bSizer11, 1, wx.EXPAND, 10)

        bSizer12 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button_add = wx.Button(self.m_panel1, wx.ID_ANY, u"Add items", wx.DefaultPosition, wx.Size(130, -1), 0)

        # self.m_button_add.SetDefault()
        bSizer12.Add(self.m_button_add, 0, wx.ALL, 5)
        #
        self.m_button_reset = wx.Button(self.m_panel1, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.Size(130, -1),
                                        0)
        bSizer12.Add(self.m_button_reset, 0, wx.ALL, 5)
        #
        # self.m_button_find = wx.Button(self.m_panel1, wx.ID_ANY, u"Find", wx.DefaultPosition, wx.DefaultSize, 0)
        # bSizer12.Add(self.m_button_find, 0, wx.ALL, 5)

        bSizer4.Add(bSizer12, 0, wx.EXPAND, 10)

        bSizer111.Add(bSizer4, 0, wx.EXPAND, 10)

        self.m_panel1.SetSizer(bSizer111)
        self.m_panel1.Layout()
        bSizer111.Fit(self.m_panel1)
        bSizer1.Add(self.m_panel1, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()
        self.m_statusBar = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)

        self.Centre(wx.BOTH)

        self.m_button_add.SetBitmap(wx.Bitmap(wx.Image(add_item.GetImage()).ConvertToBitmap()))
        self.m_button_reset.SetBitmap(wx.Bitmap(wx.Image(reset.GetImage()).ConvertToBitmap()))
        # Connect Events
        self.m_button_add.Bind(wx.EVT_BUTTON, self.add_item)
        self.m_button_reset.Bind(wx.EVT_BUTTON, self.clear_form)
        # self.m_textCtrl_item_id.Bind(wx.EVT_TEXT_ENTER, self.load_ez)
        print("Inventory add module:", self.ip)

    def __del__(self):
        pass

    def query_database(self, qry):
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
                cursor.execute(qry)
                rows = cursor.rowcount
                info = cursor.fetchall()
                # print(info)
        except pymysql.err.OperationalError as error:
            print(error)

        finally:
            connection.close()
        return [rows, info]

    def load_ez(self, event):

        s_id = self.m_textCtrl_item_id.GetValue().split('-')[0]
        qry = "SELECT * FROM ConfigSheet WHERE sheet_id={}".format(s_id)
        result = self.query_database(qry)
        print(result)
        if result[0] != 0:
            self.m_textCtrl_item_ez_no.SetValue(result[1][0]['ez_part_number'])
        else:
            print("No record of this config sheet in the database")
            self.SetStatusText("No record of this config sheet in the database")

    # Virtual event handlers, override them in your derived class
    def clear_form(self, event):
        self.m_textCtrl_bin.SetValue('')
        self.m_textCtrl_item_id.SetValue('')
        self.m_textCtrl_item_ez_no.SetValue('')
        self.m_textCtrl_item_ez_no.SetFocus()

    def read_form(self):
        print(self.bins)
        ez_no = self.m_textCtrl_item_ez_no.GetValue().lstrip().upper()
        bin_number = self.m_textCtrl_bin.GetValue().lstrip().upper()
        item_id = self.m_textCtrl_item_id.GetValue().lstrip().split()
        if bin_number == '' or bin_number not in self.bins:
            print("Please enter a valid bin number")
            self.SetStatusText("Please enter a valid bin number")
            return
        elif item_id == []:
            print("Item ID field can not be empty")
            self.SetStatusText("Item ID field can not be empty")
            return
        elif ez_no == '':
            print("EZ No field can not be empty")
            self.SetStatusText("Ez No field can not be empty")
            return
        else:
            date_today = self.date_today
            sht_id = 111111
            print(sht_id)
            dct = {
                'date_today': date_today,
                'bin_no': bin_number,
                'item_id': item_id,
                'sheet_id': sht_id,
                'ez_no': ez_no,
                'username': self.loggedin_user_username.upper(),
            }  # a dict object
            return dct

    def add_item(self, event):

        data = self.read_form()
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
                    for i in data['item_id']:
                        # find if record already exists for this part number
                        sql = "SELECT * FROM item_to_bin WHERE item_id='{}'".format(i)
                        cursor.execute(sql)

                        # gets the number of rows returned by database for the above sql command
                        row_count = cursor.rowcount

                        # row_count = 0
                        print("number of rows returned by database for this item: {}".format(row_count))

                        if row_count == 0:
                            """Create a new record if no previous record found"""
                            if i != '':

                                sql = "INSERT INTO `item_to_bin` (date_added, bin_number, item_id, sheet_id, ez_no, added_by) VALUES (%s, %s, %s, %s, %s, %s)"
                                val = (data['date_today'],
                                            data['bin_no'],
                                            i,
                                            data['sheet_id'],
                                            data['ez_no'],
                                            data['username']
                                            )

                                cursor.execute(sql, val)

                                # connection is not autocommit by default.So you must commit to save
                                # your changes.
                                connection.commit()
                                print('Connection committed')
                                txt = "{} with part number  {}  is successfully added to bin number  {}".format(i,
                                                                                                      data['ez_no'],
                                                                                                      data['bin_no'])
                                self.SetStatusText(txt)
                                self.m_textCtrl_item_id.SetValue(txt)
                            else:
                                txt = "SN field is empty"
                                self.SetStatusText(txt)
                        else:
                            d = cursor.fetchall()[0]
                            # print(d)
                            msg1 = "This item {} with part number {} is already placed in bin numer {}".format(i,
                                                                                                    data['ez_no'],
                                                                                                    d['bin_number'])
                            wx.MessageBox(msg1, "STOP!",
                                          wx.OK | wx.ICON_STOP, )
                            self.SetStatusText(msg1)
                            # self.clear_form(event=wx.EVT_BUTTON)

            except pymysql.err.OperationalError as error:
                print(error)

            finally:
                connection.close()
                self.clear_form(event=wx.EVT_BUTTON)
        else:
            print("All fields are required.")
            self.SetStatusText("All fields are required.")


# if __name__ == '__main__':
#     app = wx.App(False)
#     frame = Add_Inventory_items(None)
#     frame.m_textCtrl_item_ez_no.SetFocus()
#     frame.Show()
#     app.MainLoop()
