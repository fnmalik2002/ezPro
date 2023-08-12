# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-40-g8042f487)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid
import new_user_creation_form as new_user
import pymysql
from company_logo import *

###########################################################################
## Class UserManagement
###########################################################################

class UserManagement(wx.Frame):
    ip = ''  # IP address of the database server
    user = ''  # limited access user name of the database
    password = ''  # limited access user's pw
    db = ''  # database name
    bins = []
    today_units = []

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title="ezPro - User Management", pos=wx.DefaultPosition,
                          size=wx.Size(800, 450), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

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

        bSizer2.Add((0, 100), 3, wx.EXPAND, 5)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        bSizer13 = wx.BoxSizer(wx.VERTICAL)

        self.m_button_create_new_user = wx.Button(self.m_panel_button_panel, wx.ID_ANY, u"Add...",
                                                  wx.DefaultPosition, wx.Size(130, -1), 0)
        bSizer13.Add(self.m_button_create_new_user, 0, wx.ALL, 2)

        self.m_button_refresh = wx.Button(self.m_panel_button_panel, wx.ID_ANY, u"Refresh",
                                          wx.DefaultPosition, wx.Size(130, -1), 0)
        bSizer13.Add(self.m_button_refresh, 0, wx.ALL, 2)

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
        self.m_grid1.CreateGrid(50, 6)
        self.m_grid1.EnableEditing(True)
        self.m_grid1.EnableGridLines(True)
        self.m_grid1.EnableDragGridSize(False)
        self.m_grid1.SetMargins(0, 0)

        # Columns
        self.m_grid1.SetColSize(0, 100)
        self.m_grid1.SetColSize(1, 100)
        self.m_grid1.SetColSize(2, 100)
        self.m_grid1.SetColSize(3, 100)
        self.m_grid1.SetColSize(4, 100)
        self.m_grid1.SetColSize(5, 100)
        self.m_grid1.EnableDragColMove(True)
        self.m_grid1.EnableDragColSize(True)
        self.m_grid1.SetColLabelValue(0, u"User ID")
        self.m_grid1.SetColLabelValue(1, u"Username")
        self.m_grid1.SetColLabelValue(2, u"Title")
        self.m_grid1.SetColLabelValue(3, u"Status")
        self.m_grid1.SetColLabelValue(4, u"First Name")
        self.m_grid1.SetColLabelValue(5, u"Last Name")
        self.m_grid1.SetColLabelValue(6, wx.EmptyString)
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
        self.m_notebook2.AddPage(self.m_panel7, u"Users", True)

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
        self.m_button_create_new_user.SetBitmap(wx.Bitmap(wx.Image(manage_users.GetImage()).ConvertToBitmap()))

        # Connect Events
        self.m_button_create_new_user.Bind(wx.EVT_BUTTON, self.create_new_user)
        self.m_grid1.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.on_dclick)
        self.m_grid1.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.new_cell_left_click)
        self.m_button_refresh.Bind(wx.EVT_BUTTON, self.refresh_by_button)

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
        user_id = str(self.m_grid1.GetCellValue(event.GetRow(), 0))
        # print(username)
        frame = new_user.NewUser(self)
        frame.ip = self.ip
        frame.load_user(user_id)
        frame.lock_inputs()
        frame.Show()


    # Virtual event handlers, override them in your derived class
    def create_new_user(self, event):
        frame = new_user.NewUser(self)
        frame.ip = self.ip
        frame.m_button_edit.Disable()
        frame.m_button_delete_user.Disable()
        frame.m_button_activate_user.Disable()
        frame.m_button_deactivate_user.Disable()
        frame.Show()

    def load_data(self, qr, vl):
        qry = qr
        val = vl
        self.m_grid1.ClearGrid()
        # self.clear_row_color()

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

                    n = 0
                    r = 0

                while n < len(data) and r < row_count:
                    lst = data[n]
                    self.today_units.append(lst[u'user_username'])
                    # print(self.today_units)

                    if lst[u'user_is_active']:
                        status = 'ACTIVE'
                    else:
                        status = 'INACTIVE'

                    if lst[u'user_is_manager']:
                        u_title = "MANAGER"
                    else:
                        u_title = "EBAY TECH"

                    self.m_grid1.SetCellValue(r, 0, str(lst[u'user_id']))
                    self.m_grid1.SetCellValue(r, 1, str(lst[u'user_username']))
                    self.m_grid1.SetCellValue(r, 2, u_title)
                    self.m_grid1.SetCellValue(r, 3, status)
                    self.m_grid1.SetCellValue(r, 4, str(lst[u'first_name']))
                    self.m_grid1.SetCellValue(r, 5, str(lst[u'last_name']))
    
                    r = r + 1
                    n = n + 1

        except pymysql.err.OperationalError as error:
            print(error)
            # wx.MessageBox("No connection to the database.", "Error!", wx.ICON_ERROR)
        finally:
            connection.close()
            # print(self.today_units)
            return len(data)

    def on_load_grid(self):

        qry = "SELECT user_id, first_name, last_name, user_username, user_password_hash, user_is_manager, user_is_active FROM users ORDER BY user_id DESC LIMIT 50"
        val = ''
        self.load_data(qry, val)
