# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-40-g8042f487)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################
import datetime
import os
import wx
import wx.xrc
import wx.grid
import add_to_discontinue_form as new_discontinue
import pymysql
from company_logo import *
import pandas as pd

###########################################################################
## Class UserManagement
###########################################################################

class DiscontinuedViewer(wx.Frame):
    ip = ''  # IP address of the database server
    user = ''  # limited access user name of the database
    password = ''  # limited access user's pw
    db = ''  # database name
    bins = []
    today_units = []

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title="ezPro - Discontinued Items Management", pos=wx.DefaultPosition,
                          size=wx.Size(1240, 700), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.logo_med = wx.Image(l_med.GetImage()).ConvertToBitmap()
        self.SetIcon(wx.Icon(self.logo_med))
        bSizer_main = wx.BoxSizer(wx.HORIZONTAL)

        self.m_panel_button_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel_button_panel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_bitmap1 = wx.StaticBitmap(self.m_panel_button_panel, wx.ID_ANY,
                                         wx.Bitmap(self.logo_med), wx.DefaultPosition, wx.DefaultSize,
                                         0)
        bSizer3.Add(self.m_bitmap1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer3.Add((0, 0), 0, wx.EXPAND, 5)

        bSizer2.Add(bSizer3, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer2.Add((0, 10), 3, wx.EXPAND, 5)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        bSizer13 = wx.BoxSizer(wx.VERTICAL)

        self.m_button_add_new_discontinue = wx.Button(self.m_panel_button_panel, wx.ID_ANY, u"Add...",
                                                      wx.DefaultPosition, wx.Size(130, -1), 0)
        bSizer13.Add(self.m_button_add_new_discontinue, 0, wx.ALL, 2)

        self.m_button_refresh = wx.Button(self.m_panel_button_panel, wx.ID_ANY, u"Refresh",
                                          wx.DefaultPosition, wx.Size(130, -1), 0)
        bSizer13.Add(self.m_button_refresh, 0, wx.ALL, 2)
        self.m_button_download_list = wx.Button(self.m_panel_button_panel, wx.ID_ANY, u"Download List",
                                          wx.DefaultPosition, wx.Size(130, -1), 0)
        bSizer13.Add(self.m_button_download_list, 0, wx.ALL, 2)

        bSizer4.Add(bSizer13, 1, wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer4.Add((0, 200), 3, wx.EXPAND, 5)

        bSizer2.Add(bSizer4, 0, wx.EXPAND, 5)

        self.m_panel_button_panel.SetSizer(bSizer2)
        self.m_panel_button_panel.Layout()
        bSizer2.Fit(self.m_panel_button_panel)
        bSizer_main.Add(self.m_panel_button_panel, 0, wx.ALL | wx.EXPAND, 0)

        self.m_panel_grid_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel_grid_panel.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.m_notebook2 = wx.Notebook(self.m_panel_grid_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.m_panel7 = wx.Panel(self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        self.m_grid1 = wx.grid.Grid(self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid1.CreateGrid(1000, 5)
        self.m_grid1.EnableEditing(True)
        self.m_grid1.EnableGridLines(True)
        self.m_grid1.EnableDragGridSize(False)
        self.m_grid1.SetMargins(0, 0)

        # Columns
        self.m_grid1.SetColSize(0, 60)
        self.m_grid1.SetColSize(1, 250)
        self.m_grid1.SetColSize(2, 400)
        self.m_grid1.SetColSize(3, 200)
        self.m_grid1.SetColSize(4, 100)

        self.m_grid1.EnableDragColMove(True)
        self.m_grid1.EnableDragColSize(True)
        self.m_grid1.SetColLabelValue(0, u"Item ID")
        self.m_grid1.SetColLabelValue(1, u"Model")
        self.m_grid1.SetColLabelValue(2, u"Special Instructions")
        self.m_grid1.SetColLabelValue(3, u"Discontinue Date")
        self.m_grid1.SetColLabelValue(4, u"Active")

        # self.m_grid1.SetColLabelValue(6, wx.EmptyString)
        self.m_grid1.SetColLabelSize(wx.grid.GRID_AUTOSIZE)

        self.m_grid1.SetColLabelAlignment(wx.ALIGN_LEFT, wx.ALIGN_LEFT)

        # Rows
        self.m_grid1.AutoSizeRows()
        self.m_grid1.EnableDragRowSize(True)
        self.m_grid1.SetRowLabelSize(wx.grid.GRID_AUTOSIZE)
        # self.m_grid1.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.m_grid1.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer10.Add(self.m_grid1, 0, wx.ALL | wx.EXPAND, 5)

        self.m_panel7.SetSizer(bSizer10)
        self.m_panel7.Layout()
        bSizer10.Fit(self.m_panel7)
        self.m_notebook2.AddPage(self.m_panel7, u"Discontinued Items", True)

        bSizer9.Add(self.m_notebook2, 0, wx.EXPAND | wx.ALL, 0)

        self.m_panel_grid_panel.SetSizer(bSizer9)
        self.m_panel_grid_panel.Layout()
        bSizer9.Fit(self.m_panel_grid_panel)
        bSizer_main.Add(self.m_panel_grid_panel, 1, wx.ALL | wx.EXPAND, 0)

        self.SetSizer(bSizer_main)
        self.Layout()

        self.Centre(wx.BOTH)
        # add icons to buttons
        self.m_button_refresh.SetBitmap(wx.Bitmap(wx.Image(reuse_sheet.GetImage()).ConvertToBitmap()))
        self.m_button_add_new_discontinue.SetBitmap(wx.Bitmap(wx.Image(manage_users.GetImage()).ConvertToBitmap()))
        self.m_button_download_list.SetBitmap(wx.Bitmap(wx.Image(add_item.GetImage()).ConvertToBitmap()))

        # Connect Events
        self.m_button_add_new_discontinue.Bind(wx.EVT_BUTTON, self.add_to_discontinue)
        self.m_grid1.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.on_dclick)
        self.m_grid1.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.new_cell_left_click)
        self.m_button_download_list.Bind(wx.EVT_BUTTON, self.download_list)
        self.m_button_refresh.Bind(wx.EVT_BUTTON, self.refresh_by_button)
        self.Show()
        self.m_statusBar = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)

    def new_cell_left_click(self, event):
        print("cell left clicked ")
        tab = event.EventObject.GetChildren()[event.Selection].GetName()
        print("you selected tab " + tab)
        self.m_grid1.SelectRow(event.GetRow(), False)

    def __del__(self):
        pass

    def refresh_by_button(self, event):
        print("refresh called")
        self.on_load_grid()

    def refresh(self):
        print("refresh called")
        self.on_load_grid()

    def on_dclick(self, event):
        model = str(self.m_grid1.GetCellValue(event.GetRow(), 1))
        # print(username)
        frame = new_discontinue.NewDiscontinue(self)
        frame.ip = self.ip
        frame.load_item(model)
        frame.lock_inputs()
        frame.Show()

    def add_to_discontinue(self, event):
        frame = new_discontinue.NewDiscontinue(self)
        frame.ip = self.ip
        frame.m_button_edit.Disable()
        frame.m_button_delete_user.Disable()
        frame.m_button_activate_user.Disable()
        frame.m_button_deactivate_user.Disable()
        frame.m_textCtrl_discontinue_date.SetValue(str(datetime.datetime.now().date()))
        frame.Show()

    def download_list(self, event):
        qry = "SELECT * from discontinue_items ORDER BY is_active DESC"
        val = ('')
        data1 = self.load_data(qry, val)
        print('data1', data1)
        df = pd.DataFrame(data = data1)
        print(df)
        f = os.path.abspath(".\\output\Discontinued items list as of {}.xlsx".format(datetime.datetime.now().date()))
        df.to_excel(f)

    def on_load_grid(self):
        qry = "SELECT * from discontinue_items ORDER BY is_active DESC"
        val = ('')
        self.load_data(qry, val)

    def load_data(self, qr, vl):
        qry = qr
        val = vl
        self.m_grid1.ClearGrid()
        # self.clear_row_color()

        # Connect to the database
        cursor = pymysql.cursors.DictCursor
        connection = pymysql.connect(host = self.ip,
                                     user = self.user,
                                     password = self.password,
                                     db = self.db,
                                     charset = 'utf8mb4',
                                     cursorclass = cursor)

        try:
            with connection.cursor() as cur:
                if val != '':
                    cur.execute(
                        qry, val,
                    )
                    row_count = cur.rowcount
                    data = cur.fetchall()

                    self.total_Number_of_rows_of_data_returned = len(data)  # stores total rows returned to variable

                    n = 0
                    r = 0
                else:
                    cur.execute(
                        qry
                    )
                    row_count = cur.rowcount
                    data = cur.fetchall()
                    # print(data)
                    self.total_Number_of_rows_of_data_returned = len(data)  # stores total rows returned to variable
                    print("total rows returned to variable", self.total_Number_of_rows_of_data_returned)
                    self.SetStatusText("Total records found : {}".format(self.total_Number_of_rows_of_data_returned))
                    n = 0
                    r = 0

                while n < len(data) and r < row_count:
                    lst = data[ n ]
                    # self.today_units.append(lst[ u'user_username' ])
                    # print(self.today_units)

                    if lst[ u'is_active' ]:
                        status = 'ACTIVE'
                    else:
                        status = 'INACTIVE'
                    #
                    # if lst[ u'user_is_manager' ]:
                    #     u_title = "MANAGER"
                    # else:
                    #     u_title = "EBAY TECH"

                    self.m_grid1.SetCellValue(r, 0, str(lst[ u'item_id' ]))
                    self.m_grid1.SetCellValue(r, 1, str(lst[ u'item_model' ]))
                    self.m_grid1.SetCellValue(r, 2, str(lst[ u'discontinue_condition' ]))
                    self.m_grid1.SetCellValue(r, 3, str(lst[ u'discontinue_date' ]))
                    self.m_grid1.SetCellValue(r, 4, status)

                    r = r + 1
                    n = n + 1

        except pymysql.err.OperationalError as error:
            print(error)
            # wx.MessageBox("No connection to the database.", "Error!", wx.ICON_ERROR)
        finally:
            connection.close()
            # print(self.today_units)
            return data
