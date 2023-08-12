# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-40-g8042f487)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import hashlib
import pymysql
from company_logo import *

###########################################################################
## Class MyLogin
###########################################################################

class MyLogin(wx.Dialog):
    # ip = ''  # IP address of the database server
    # user = 'tarpon'  # limited access user name of the database
    # password = 'eBay'  # limited access user's pw
    # db = 'bass2'  # database name
    data = []
    ip = ''  # IP address of the database server
    user = ''  # limited access user name of the database
    password = ''  # limited access user's pw
    db = ''  # database name
    bins = []

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title='Login', pos=wx.DefaultPosition, size=wx.Size(700, 350),
                           style=wx.DEFAULT_DIALOG_STYLE | wx.TAB_TRAVERSAL)
        self.logo_med = wx.Image(l_med.GetImage()).ConvertToBitmap()

        self.logo_lrg = wx.Image(l_lar.GetImage()).ConvertToBitmap()
        self.SetIcon(wx.Icon(self.logo_med))
        self.logged_in = False
        self.user_name = ''

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer_main = wx.BoxSizer(wx.HORIZONTAL)

        self.m_panel_button_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel_button_panel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)
        bSizer3.Add((0, 10), 0, wx.EXPAND, 5)
        self.m_bitmap1 = wx.StaticBitmap(self.m_panel_button_panel, wx.ID_ANY,
                                         wx.Bitmap(self.logo_lrg), wx.DefaultPosition, wx.DefaultSize,
                                         0)
        bSizer3.Add(self.m_bitmap1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer3.Add((0, 0), 0, wx.EXPAND, 5)

        bSizer2.Add(bSizer3, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        bSizer13 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer4.Add(bSizer13, 1, wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer4.Add((0, 100), 1, wx.EXPAND, 5)

        bSizer4.Add((0, 200), 6, wx.EXPAND, 5)

        bSizer2.Add(bSizer4, 0, wx.EXPAND, 5)

        self.m_panel_button_panel.SetSizer(bSizer2)
        self.m_panel_button_panel.Layout()
        bSizer2.Fit(self.m_panel_button_panel)
        bSizer_main.Add(self.m_panel_button_panel, 0, wx.ALL | wx.EXPAND, 0)

        self.m_panel_grid_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel_grid_panel.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.m_notebook2 = wx.Notebook(self.m_panel_grid_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 350), 0)
        self.m_panel7 = wx.Panel(self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer10 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer15 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText5 = wx.StaticText(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText5.Wrap(-1)

        bSizer15.Add(self.m_staticText5, 0, wx.ALL, 5)

        bSizer10.Add(bSizer15, 1, wx.EXPAND, 5)

        bSizer16 = wx.BoxSizer(wx.VERTICAL)

        bSizer16.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer11 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer11.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_staticText2 = wx.StaticText(self.m_panel7, wx.ID_ANY, u"User : ", wx.DefaultPosition, wx.Size(70, -1), 0)
        self.m_staticText2.Wrap(-1)

        bSizer11.Add(self.m_staticText2, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_username = wx.TextCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        bSizer11.Add(self.m_textCtrl_username, 0, wx.ALL, 5)


        bSizer11.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer16.Add(bSizer11, 0, 0, 5)

        bSizer111 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer111.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_staticText21 = wx.StaticText(self.m_panel7, wx.ID_ANY, u"Password : ", wx.DefaultPosition,
                                            wx.Size(70, -1), 0)
        self.m_staticText21.Wrap(-1)

        bSizer111.Add(self.m_staticText21, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer111.Add((0, 0), 0, wx.EXPAND, 5)

        self.m_textCtrl_password = wx.TextCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                               wx.DefaultSize,
                                               wx.TE_PASSWORD | wx.TE_PROCESS_ENTER)
        bSizer111.Add(self.m_textCtrl_password, 0, wx.ALL, 5)

        bm = wx.Bitmap(wx.Image(login_enter.GetImage()).ConvertToBitmap())
        self.m_button7 = wx.BitmapButton(self.m_panel7, wx.ID_ANY, bm, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer111.Add(self.m_button7, 0, wx.ALL, 5)
        # set bmp as bitmap for button
        # < a
        # target = "_blank"
        # href = "https://icons8.com/icon/BD3laP7MFEAB/bust-in-silhouette" > Bust
        # In
        # Silhouette < / a > icon
        # by < a
        # target = "_blank"
        # href = "https://icons8.com" > Icons8 < / a >

        # self.m_button7.SetBitmap(bm)

        bSizer111.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer16.Add(bSizer111, 0, 0, 5)
        self.m_staticText_login_msg = wx.StaticText(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                    wx.DefaultSize, 0)
        self.m_staticText_login_msg.Wrap(-1)

        bSizer16.Add(self.m_staticText_login_msg, 0, wx.ALL, 5)

        bSizer16.Add((0, 30), 1, wx.EXPAND, 5)
        #----------------

        bSizer_developer =  wx.BoxSizer(wx.VERTICAL)
        bSizer_developer1 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText_developer = wx.StaticText(self.m_panel7, wx.ID_ANY, 'Developer : ', wx.DefaultPosition,
                                                    wx.DefaultSize, 0)
        self.m_staticText_developer.Wrap(-1)

        bSizer_developer1.Add(self.m_staticText_developer, 0, wx.ALL, 5)
        self.m_staticText_developer_name = wx.StaticText(self.m_panel7, wx.ID_ANY, 'Faizan Malik  |  fnmalik2002@yahoo.co.uk', wx.DefaultPosition,
                                                    wx.DefaultSize, 0)
        self.m_staticText_developer_name.Wrap(-1)

        bSizer_developer1.Add(self.m_staticText_developer_name, 0, wx.ALL, 5)
        bSizer_developer.Add(bSizer_developer1, 1, wx.EXPAND, 5)



        bSizer10.Add(bSizer16, 1, wx.EXPAND, 5)
        bSizer16.Add(bSizer_developer, 1, wx.EXPAND, 5)

        bSizer17 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText6 = wx.StaticText(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText6.Wrap(-1)

        bSizer17.Add(self.m_staticText6, 0, wx.ALL, 5)

        bSizer10.Add(bSizer17, 1, wx.EXPAND, 5)

        self.m_panel7.SetSizer(bSizer10)
        self.m_panel7.Layout()
        bSizer10.Fit(self.m_panel7)
        self.m_notebook2.AddPage(self.m_panel7, u"Please login", True)

        bSizer9.Add(self.m_notebook2, 0, wx.EXPAND | wx.ALL, 0)

        self.m_panel_grid_panel.SetSizer(bSizer9)
        self.m_panel_grid_panel.Layout()
        bSizer9.Fit(self.m_panel_grid_panel)
        bSizer_main.Add(self.m_panel_grid_panel, 1, wx.ALL | wx.EXPAND, 0)

        self.SetSizer(bSizer_main)
        self.Layout()
        # self.m_textCtrl_username.SetFocus()


        self.Centre(wx.BOTH)
        self.m_button7.Bind(wx.EVT_BUTTON, self.on_login)
        self.m_textCtrl_password.Bind(wx.EVT_TEXT_ENTER, self.on_login)
        # self.Show()

    def __del__(self):
        pass

    def clear_fields(self, event):
        self.m_staticText_login_msg.SetLabel('')
        self.m_textCtrl_username.SetValue('')
        self.m_textCtrl_password.SetValue('')

    def read_form(self):
        """This function reads the vlaues from all text control fields in the new user form and return it as dictionary"""
        user_password = self.m_textCtrl_password.GetValue().lstrip()
        user_password_hashed = hashlib.md5(user_password.encode('utf8')).hexdigest()

        data = {

                'user_username': self.m_textCtrl_username.GetValue().lstrip().upper(),
                'user_password_hash': user_password_hashed,

            }
        # print(data)
        return data



    # Virtual event handlers, override them in your derived class
    def on_login(self, event):
        self.data = []
        form_data = self.read_form()
        stupid_password = ''

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

                cursor.execute(
                    "SELECT * FROM users WHERE user_username = %s GROUP BY user_username",
                        (form_data['user_username'],))

                # gets the number of rows returned by database for the above sql command
                row_count = cursor.rowcount
                print("number of rows returned by database for this username: {}".format(row_count))




                # print(stupid_password)
                if row_count == 0:
                    self.m_staticText_login_msg.SetLabel("User not found")

                else:
                    self.data.append(cursor.fetchall())
                    # print(self.data)
                    stupid_password = (self.data[0][0]['user_password_hash'])
                    self.m_staticText_login_msg.SetLabel("User verified")


        except pymysql.err.OperationalError as error:
            print(error)
            self.m_staticText_login_msg.SetLabel("Connection Error! Could not submit record")

        finally:
            connection.close()

        """
        Check credentials and login
        """

        user_password_entered = self.read_form()['user_password_hash']

        if user_password_entered == stupid_password:
            # print("You are now logged in!")
            self.user_name = self.m_textCtrl_username.GetValue()
            self.logged_in = True
            self.Close()

        else:
            print("Username or password is incorrect!")
            self.m_staticText_login_msg.SetLabel("Username or password is incorrect!")

        # print("user name = ", self.user_name)
        # print("user logged in ? = ", self.logged_in)




#
# if __name__ == '__main__':
#     app = wx.App(False)
#     frame = MyLogin(None)
#     frame.m_textCtrl_username.SetFocus()
#     frame.Show()
#     app.MainLoop()