# -*- coding: utf-8 -*-
import subprocess
###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-231-gdf7791bf)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

from datetime import datetime as dt
from company_logo import *
import wx
import wx.xrc
import pymysql.cursors


###########################################################################
## Class Inventory_location
###########################################################################

class Inventory_Pulls(wx.Frame):
    date_today = str(dt.now())
    ip = ''  # IP address of the database server
    user = ''  # limited access username of the database
    password = ''  # limited access user's pw
    db = ''  # database name
    bins = []
    loggedin_user_username = ''

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"ezPro - Inventory Management", pos=wx.DefaultPosition,
                          size=wx.Size(740, 600), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.logo_med = wx.Image(l_med.GetImage()).ConvertToBitmap()
        self.SetIcon(wx.Icon(self.logo_med))
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        font1 = wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande")
        font2 = wx.Font(20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Lucida Grande")

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer111 = wx.BoxSizer(wx.VERTICAL)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)
        bSizer2_1 = wx.BoxSizer(wx.VERTICAL)
        bSizer2_2 = wx.BoxSizer(wx.VERTICAL)
        bSizer2.Add(bSizer2_1)
        # add spacer
        bSizer2.Add((20, 0), 0, wx.EXPAND, 5)
        bSizer2.Add(bSizer2_2)
        bSizer2.Add((20, 0), 0, wx.EXPAND, 5)
        # ------------

        self.m_staticText1 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"PN#:",
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)

        self.m_staticText1.SetFont(font1)

        bSizer2_1.Add(self.m_staticText1, 1, wx.ALL, 5)

        self.m_textCtrl_pn = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.Size(200, 40), 0 | wx.TE_PROCESS_ENTER)
        self.m_textCtrl_pn.SetFont(font2)
        bSizer2_1.Add(self.m_textCtrl_pn, 0, wx.ALL, 5)




        self.m_staticText111 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"BIN#:",
                                             wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText111.Wrap(-1)

        self.m_staticText111.SetFont(font1)

        bSizer2_2.Add(self.m_staticText111, 1, wx.ALL, 5)

        self.m_textCtrl_bin = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                          wx.Size(200, 40), 0 | wx.TE_PROCESS_ENTER)
        self.m_textCtrl_bin.SetFont(font2)
        bSizer2_2.Add(self.m_textCtrl_bin, 0, wx.ALL, 5)
        #-------------
        m_radioBoxChoices = [u"Find", u"Append"]
        self.m_radioBox = wx.RadioBox(self.m_panel1, wx.ID_ANY, u"Mode", wx.DefaultPosition, wx.Size( -1,55 ), m_radioBoxChoices,
                                      1, wx.RA_SPECIFY_ROWS)
        self.m_radioBox.SetSelection(0)
        bSizer2.Add(self.m_radioBox, 0, wx.ALIGN_BOTTOM, 5)



        # ----------

        self.m_staticText2 = wx.StaticText(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText2.Wrap(-1)

        bSizer2.Add(self.m_staticText2, 2, wx.EXPAND, 5)

        self.m_bitmap_logo = wx.StaticBitmap(self.m_panel1, wx.ID_ANY, wx.Bitmap(self.logo_med),
                                             wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_bitmap_logo, 0, wx.ALL, 5)

        bSizer111.Add(bSizer2, 0, wx.EXPAND, 5)
        self.m_button_print = wx.Button(self.m_panel1, wx.ID_ANY, u"Print", wx.DefaultPosition, wx.Size(80, -1), 0)
        bSizer111.Add(self.m_button_print, 0, wx.ALL, 5)

        self.m_staticline1 = wx.StaticLine(self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        bSizer111.Add(self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        bSizer5_0 = wx.BoxSizer(wx.VERTICAL)

        bSizer5_0.Add((0, 5), 1, wx.EXPAND, 5)

        self.m_staticText5 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"items list:", wx.DefaultPosition,
                                           wx.DefaultSize,
                                           0)
        self.m_staticText5.Wrap(-1)

        self.m_staticText5.SetFont(
            wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande"))

        bSizer5_0.Add(self.m_staticText5, 0, wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl_items_list = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, style=wx.TE_MULTILINE
                                                 )
        self.m_textCtrl_items_list.SetInitialSize((200, 200))
        bSizer5_0.Add(self.m_textCtrl_items_list, 0, wx.ALL | wx.EXPAND, 5)

        # bSizer5_0.Add((0, 5), 1, wx.EXPAND, 5)
        bSizer3.Add(bSizer5_0, 1, wx.ALL | wx.EXPAND, 0)

        # bSizer5 = wx.BoxSizer(wx.VERTICAL)

        # bSizer5.Add((0, 5), 1, wx.EXPAND, 5)

        # self.m_staticText3 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Bin number :", wx.DefaultPosition, wx.DefaultSize, 0)
        # self.m_staticText3.Wrap(-1)
        #
        # self.m_staticText3.SetFont(
        #     wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande"))
        #
        # bSizer5.Add(self.m_staticText3, 0, wx.ALL | wx.EXPAND, 5)
        #
        # self.m_textCtrl_bin = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
        #                                   0)
        # bSizer5.Add(self.m_textCtrl_bin, 0, wx.ALL | wx.EXPAND, 5)
        #
        # bSizer5.Add((0, 5), 1, wx.EXPAND, 5)
        #
        # bSizer3.Add(bSizer5, 1, wx.ALL | wx.EXPAND, 0)

        bSizer111.Add(bSizer3, 2, wx.ALL | wx.EXPAND, 5)

        #
        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        bSizer7.Add((0, 5), 1, wx.EXPAND, 5)

        # self.m_staticText4 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Quantity :", wx.DefaultPosition,
        #                                    wx.DefaultSize, 0)
        # self.m_staticText4.Wrap(-1)
        #
        # self.m_staticText4.SetFont(
        #     wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande"))
        #
        # bSizer7.Add(self.m_staticText4, 0, wx.ALL | wx.EXPAND, 5)
        #
        # self.m_textCtrl_qty_sold = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
        #                                        wx.DefaultSize,
        #                                        0 | wx.TE_PROCESS_ENTER)
        # bSizer7.Add(self.m_textCtrl_qty_sold, 0, wx.ALL | wx.EXPAND, 5)

        bSizer7.Add((0, 5), 1, wx.EXPAND, 5)

        bSizer3.Add(bSizer7, 1, wx.ALL | wx.EXPAND, 0)

        # ----
        bSizer7_0 = wx.BoxSizer(wx.VERTICAL)

        bSizer7_0.Add((0, 5), 1, wx.EXPAND, 5)

        self.m_staticText44 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"SO Number :", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText44.Wrap(-1)

        self.m_staticText44.SetFont(
            wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande"))

        bSizer7_0.Add(self.m_staticText44, 0, wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl_so = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.DefaultSize,
                                         0 | wx.TE_PROCESS_ENTER)
        bSizer7_0.Add(self.m_textCtrl_so, 0, wx.ALL | wx.EXPAND, 5)

        bSizer7_0.Add((0, 5), 1, wx.EXPAND, 5)
        bSizer3.Add(bSizer7_0, 1, wx.ALL | wx.EXPAND, 0)
        # ----

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

        self.m_button_sold = wx.Button(self.m_panel1, wx.ID_ANY, u"Mark Sold", wx.DefaultPosition, wx.Size(130, -1), 0)
        bSizer12.Add(self.m_button_sold, 0, wx.ALL, 5)

        # self.m_button_deman = wx.Button(self.m_panel1, wx.ID_ANY, u"Mark Deman", wx.DefaultPosition, wx.Size(130, -1), 0)

        # self.m_button_add.SetDefault()
        # bSizer12.Add(self.m_button_deman, 0, wx.ALL, 5)
        #
        self.m_button_reset = wx.Button(self.m_panel1, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.Size(130, -1),
                                        0)
        bSizer12.Add(self.m_button_reset, 0, wx.ALL, 5)

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

        self.m_button_sold.SetBitmap(wx.Bitmap(wx.Image(sold.GetImage()).ConvertToBitmap()))
        # self.m_button_deman.SetBitmap(wx.Bitmap(wx.Image(deman.GetImage()).ConvertToBitmap()))
        self.m_button_reset.SetBitmap(wx.Bitmap(wx.Image(reset.GetImage()).ConvertToBitmap()))

        # Connect Events
        self.m_button_sold.Bind(wx.EVT_BUTTON, self.mark_sold)
        self.m_button_reset.Bind(wx.EVT_BUTTON, self.clear_full_form)
        self.m_button_print.Bind(wx.EVT_BUTTON, self.my_print)
        self.m_textCtrl_pn.Bind(wx.EVT_TEXT_ENTER, self.find)
        self.m_textCtrl_bin.Bind(wx.EVT_TEXT_ENTER, self.find)
        self.Bind(wx.EVT_CHAR_HOOK, self.OnKeyUP)

        print("Inventory remove module:", self.ip)

    def __del__(self):
        pass

    def OnKeyUP(self, event):
        print("KEY UP!")
        keyCode = event.GetKeyCode()
        if keyCode == wx.WXK_ESCAPE:
            self.clear_form(event)
        event.Skip()

    def read_find_form(self):
        pn = self.m_textCtrl_pn.GetValue().lstrip()
        bin = self.m_textCtrl_bin.GetValue().lstrip()
        date_today = self.date_today
        dct = {
            'date_today': date_today,
            'pn': pn,
            'username': self.loggedin_user_username.upper(),
            'bin': bin,
        }  # a dict object
        return dct

    def my_print(self, event):
        print("print is pressed")
        print(self.m_radioBox.GetSelection())
        event.Skip()
        wr = self.m_textCtrl_items_list.GetValue().encode("utf-8")
        if wr != "":
            lpr = subprocess.Popen('usr/bin/lpr',stdin=subprocess.PIPE)
            lpr.stdin.write(wr)
            lpr.communicate()

    def find(self, event):
        self.m_button_sold.Disable()
        data = self.read_find_form()
        print(data['pn'], data['bin'])
        print('find pressed')
        if data['pn'] != "" and data['bin'] == "":

            data2 = self.populate_results(
                "SELECT * FROM item_to_bin WHERE ez_no='{}' AND is_sold=False AND is_not_sold_in_three_months=False".format(
                    data['pn']))
            self.m_statusBar.SetStatusText(f'Available Quantity = {data2[0]}')
            old_bin = ""
            for i in data2[1]:
                if i['bin_number'] != old_bin:
                    self.m_textCtrl_bin.AppendText(i['bin_number'] + " ")
                    old_bin = i['bin_number']
            for i in data2[1]:
                if self.m_radioBox.GetSelection() == 0:
                    self.m_textCtrl_items_list.AppendText("SN#:  " + i['item_id']+"\n" )
                else:
                    pass

        elif data['bin'] != "" and data['pn'] == "":


            data3 = self.populate_results(
                "SELECT * FROM item_to_bin WHERE bin_number='{}' AND is_sold=False AND is_not_sold_in_three_months=False".format(
                    data['bin']))
            self.m_statusBar.SetStatusText(f'Available Quantity = {data3[0]}')
            old_pn = ""
            for i in data3[1]:
                if i['ez_no'] != old_pn:
                    self.m_textCtrl_pn.AppendText(i['ez_no'] + " ")
                    old_pn = i['ez_no']

            for i in data3[1]:
                if self.m_radioBox.GetSelection() == 0:
                    self.m_textCtrl_items_list.AppendText(i['item_id'] + "\n")
                else:
                    pass

        else:
            print("please fill only one field")
        if self.m_radioBox.GetSelection() == 0:
            pass
        else:
            self.m_textCtrl_items_list.AppendText("P/N:    "+ self.m_textCtrl_pn.GetValue().upper()+"        Bin No:    "+ self.m_textCtrl_bin.GetValue().upper()+"\n")

    def populate_results(self, qry):
        result = self.query_database(qry)
        available_qty = str(result[0])
        data = result[1]
        print("data = \n", available_qty, len(data), data)

        if result[0] == 0:
            if self.m_radioBox.GetSelection() == 1:
                pass
            else:
                self.m_textCtrl_items_list.SetValue('No record found')
        return [available_qty, data]

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
    def clear_full_form(self, event):
        self.m_textCtrl_items_list.SetValue('')
        self.m_textCtrl_so.SetValue('')
        self.m_textCtrl_pn.SetValue('')
        self.m_textCtrl_bin.SetValue('')
        self.m_textCtrl_pn.SetFocus()
        self.m_button_sold.Enable()
        self.m_statusBar.SetStatusText("")
        self.m_radioBox.SetSelection(0)

    def clear_form(self, event):

        if self.m_radioBox.GetSelection() == 1:
            pass
        else:
            self.m_textCtrl_items_list.SetValue('')

        self.m_textCtrl_so.SetValue('')
        self.m_textCtrl_pn.SetValue('')
        self.m_textCtrl_bin.SetValue('')
        self.m_statusBar.SetStatusText("")
        self.m_textCtrl_pn.SetFocus()
        self.m_button_sold.Enable()

    def read_form(self):
        so_number = self.m_textCtrl_so.GetValue().lstrip()
        date_today = self.date_today
        dct = {
            'date_today': date_today,
            'item_list': self.m_textCtrl_items_list.GetValue().lstrip(),
            'username': self.loggedin_user_username.upper(),
            'so_number': so_number,
        }  # a dict object
        return dct

    def verfiy_status(self, item):
        # need to update it
        try:
            qry = "SELECT * FROM item_to_bin WHERE item_id='{}'".format(
                item)
            result = self.query_database(qry)
            is_sold = result[1][0]['is_sold']
            is_deman = result[1][0]['is_not_sold_in_three_months']
            print(is_sold, is_deman, result)
            if is_sold == True or is_deman == True:
                return "no"
            else:
                return "yes"
        except Exception as e:
            print(self.m_statusBar.SetStatusText("Some error occurred while trying to find the items"))
            self.m_textCtrl_items_list.SetBackgroundColour("pink")

    def mark_sold(self, event):
        data = self.read_form()
        print("Data to be updated : ", data)
        if data['so_number'] == '':
            dlg = wx.MessageDialog(self, 'Please enter SO number', 'Stop', wx.ICON_STOP)
            if dlg.ShowModal() == wx.ID_OK:
                dlg.Destroy()
                self.m_textCtrl_so.SetFocus()
                return
        items = data['item_list'].split('\n')
        done = []
        not_done = []
        for i in items:
            if i != '':
                print(i)
                if self.verfiy_status(i) == 'no':
                    print(f"item {i} is already marked as sold or deman")
                    not_done.append(i)
                elif self.verfiy_status(i) == 'yes':
                    print(f"item {i} is ready to be marked as sold")
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

                            sql = "UPDATE item_to_bin SET is_sold=True, date_removed=%s, removed_by=%s, sales_order=%s WHERE item_id=%s"
                            vals = (self.date_today, data['username'], data['so_number'], i)
                            cursor.execute(sql, vals)

                            # connection is not autocommit by default.So you must commit to save
                            # your changes.
                            connection.commit()
                            print('Connection committed')
                            txt = "Item # {} is successfully marked as sold".format(i)
                            done.append(i)
                            self.SetStatusText(txt)

                    except pymysql.err.OperationalError as error:
                        print(error)

                    finally:
                        connection.close()

        self.m_textCtrl_items_list.AppendText(
            f'\n Items successfully marked as sold = {done}\n')
        self.m_textCtrl_items_list.AppendText(
            f'\n Items that could not be marked successfully = {not_done}\n')

# if __name__ == '__main__':
#     app = wx.App(False)
#     frame = Inventory_Pulls(None)
#     frame.m_textCtrl_items_list.SetFocus()
#     frame.Show()
#     app.MainLoop()
