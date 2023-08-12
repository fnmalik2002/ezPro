# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-40-g8042f487)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################
import datetime

import wx
import wx.xrc
import pymysql
import hashlib
from company_logo import *

###########################################################################
## Class NewUser
###########################################################################

class NewDiscontinue(wx.Frame):
    ip = ''  # IP address of the database server
    user = 'tarpon'  # limited access user name of the database
    password = 'eBay'  # limited access user's pw
    db = 'bass2'  # database name

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title="ezPro - Edit Discontinue Items", pos=wx.DefaultPosition,
                          size=wx.Size(700, 350), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.logo = wx.Image(l_med.GetImage()).ConvertToBitmap()
        self.logo_med = wx.Image(l_med.GetImage()).ConvertToBitmap()
        self.SetIcon(wx.Icon(self.logo_med))
        self.loaded_hash = None
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

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

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        bSizer13 = wx.BoxSizer(wx.HORIZONTAL)
        bSizer_submit_delete =  wx.BoxSizer(wx.VERTICAL)
        self.m_button_edit = wx.Button(self.m_panel_button_panel, wx.ID_ANY, u"Edit", wx.DefaultPosition,
                                       wx.Size(130, -1), 0)
        bSizer_submit_delete.Add(self.m_button_edit, 0, wx.ALL, 2)

        self.m_button_deactivate_user = wx.Button(self.m_panel_button_panel, wx.ID_ANY, u"Deactivate", wx.DefaultPosition,
                                                  wx.Size(130, -1), 0)
        bSizer_submit_delete.Add(self.m_button_deactivate_user, 0, wx.ALL, 2)

        self.m_button_activate_user = wx.Button(self.m_panel_button_panel, wx.ID_ANY, u"Activate",
                                                  wx.DefaultPosition,
                                                  wx.Size(130, -1), 0)
        bSizer_submit_delete.Add(self.m_button_activate_user, 0, wx.ALL, 2)

        self.m_button_delete_user = wx.Button(self.m_panel_button_panel, wx.ID_ANY, u"Delete",
                                                wx.DefaultPosition,
                                                wx.Size(130, -1), 0)
        bSizer_submit_delete.Add(self.m_button_delete_user, 0, wx.ALL, 2)

        bSizer4.Add(bSizer_submit_delete, 1, wx.ALIGN_CENTER_HORIZONTAL, 5)

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

        bSizer16.Add((0, 0), 2, wx.EXPAND, 5)

        bSizer11 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText2 = wx.StaticText(self.m_panel7, wx.ID_ANY, u"Model :", wx.DefaultPosition,
                                           wx.Size(150, -1), 0)
        self.m_staticText2.Wrap(-1)

        bSizer11.Add(self.m_staticText2, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_model_name = wx.TextCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                 wx.Size(280, -1), 0)
        bSizer11.Add(self.m_textCtrl_model_name, 0, wx.ALL, 5)

        bSizer16.Add(bSizer11, 0, 0, 5)

        bSizer111 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText21 = wx.StaticText(self.m_panel7, wx.ID_ANY, u"Discontinue Condition :", wx.DefaultPosition,
                                            wx.Size(150, -1), 0)
        self.m_staticText21.Wrap(-1)

        bSizer111.Add(self.m_staticText21, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_discont_condition = wx.TextCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                        wx.Size(280, -1), 0)
        bSizer111.Add(self.m_textCtrl_discont_condition, 0, wx.ALL, 5)

        bSizer16.Add(bSizer111, 0, 0, 5)

        bSizer1111 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText211 = wx.StaticText(self.m_panel7, wx.ID_ANY, u"Discontinue Date :", wx.DefaultPosition,
                                             wx.Size(150, -1), 0)
        self.m_staticText211.Wrap(-1)

        bSizer1111.Add(self.m_staticText211, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_discontinue_date = wx.TextCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                               wx.Size(280, -1),
                                               0)
        bSizer1111.Add(self.m_textCtrl_discontinue_date, 0, wx.ALL, 5)

        bSizer16.Add(bSizer1111, 0, wx.EXPAND, 5)
        #
        # bSizer11111 = wx.BoxSizer(wx.HORIZONTAL)
        #
        # self.m_staticText2111 = wx.StaticText(self.m_panel7, wx.ID_ANY, u"password :", wx.DefaultPosition,
        #                                       wx.Size(80, -1), 0)
        # self.m_staticText2111.Wrap(-1)
        #
        # bSizer11111.Add(self.m_staticText2111, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        # self.m_textCtrl_password = wx.TextCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
        #                                        wx.Size(280, -1),
        #                                        0)
        # bSizer11111.Add(self.m_textCtrl_password, 0, wx.ALL, 5)
        #
        # bSizer16.Add(bSizer11111, 0, wx.EXPAND, 5)

        self.m_checkBox_is_active = wx.CheckBox(self.m_panel7, wx.ID_ANY, u"Make item active", wx.DefaultPosition,
                                                wx.DefaultSize, wx.ALIGN_RIGHT)
        bSizer16.Add(self.m_checkBox_is_active, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        # self.m_checkBox_is_manager = wx.CheckBox(self.m_panel7, wx.ID_ANY, u"Make user Manager", wx.DefaultPosition,
        #                                          wx.DefaultSize, wx.ALIGN_RIGHT)
        # bSizer16.Add(self.m_checkBox_is_manager, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        bSizer16.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_staticText_login_msg = wx.StaticText(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                    wx.DefaultSize, 0)
        self.m_staticText_login_msg.Wrap(-1)

        bSizer16.Add(self.m_staticText_login_msg, 0, wx.ALIGN_LEFT | wx.ALL, 5)

        bSizer16.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_button_submit = wx.Button(self.m_panel7, wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.Size(130, -1), 0)
        bSizer16.Add(self.m_button_submit, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)



        bSizer16.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer10.Add(bSizer16, 1, wx.EXPAND, 5)


        bSizer17 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText6 = wx.StaticText(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText6.Wrap(-1)

        bSizer17.Add(self.m_staticText6, 0, wx.ALL, 5)

        bSizer10.Add(bSizer17, 1, wx.EXPAND, 5)

        self.m_panel7.SetSizer(bSizer10)
        self.m_panel7.Layout()
        bSizer10.Fit(self.m_panel7)
        self.m_notebook2.AddPage(self.m_panel7, u"Item Information", True)

        bSizer9.Add(self.m_notebook2, 0, wx.EXPAND | wx.ALL, 0)

        self.m_panel_grid_panel.SetSizer(bSizer9)
        self.m_panel_grid_panel.Layout()
        bSizer9.Fit(self.m_panel_grid_panel)
        bSizer_main.Add(self.m_panel_grid_panel, 1, wx.ALL | wx.EXPAND, 0)

        self.SetSizer(bSizer_main)
        self.Layout()

        self.Centre(wx.BOTH)

        # add icons to buttons
        self.m_button_delete_user.SetBitmap(wx.Bitmap(wx.Image(trash.GetImage()).ConvertToBitmap()))
        self.m_button_edit.SetBitmap(wx.Bitmap(wx.Image(editit.GetImage()).ConvertToBitmap()))
        self.m_button_submit.SetBitmap(wx.Bitmap(wx.Image(submit.GetImage()).ConvertToBitmap()))
        self.m_button_activate_user.SetBitmap(wx.Bitmap(wx.Image(activate_it.GetImage()).ConvertToBitmap()))
        self.m_button_deactivate_user.SetBitmap(wx.Bitmap(wx.Image(deactivate_it.GetImage()).ConvertToBitmap()))

        # Connect Events
        self.m_button_submit.Bind(wx.EVT_BUTTON, self.submit)
        self.m_button_edit.Bind(wx.EVT_BUTTON, self.edit_item)
        self.m_button_deactivate_user.Bind(wx.EVT_BUTTON, self.deactivate_item)
        self.m_button_activate_user.Bind(wx.EVT_BUTTON, self.activate_item)
        self.m_button_delete_user.Bind(wx.EVT_BUTTON, self.delete_item)

    def __del__(self):
        pass

    def lock_inputs(self):
        self.m_textCtrl_model_name.SetEditable(False)
        self.m_textCtrl_discont_condition.SetEditable(False)

        self.m_checkBox_is_active.Disable()

        self.m_button_submit.Show(False)
        self.m_checkBox_is_active.SetLabel("     Item is Active")

        self.SetTitle("View / Edit Item")

    def unlock_inputs(self):
        self.m_textCtrl_model_name.SetEditable(True)
        self.m_textCtrl_discont_condition.SetEditable(True)

        self.m_checkBox_is_active.Enable()

        self.m_button_submit.SetLabel("Update")
        self.m_button_submit.Show(True)
        self.m_checkBox_is_active.SetLabel("Make item active")


    def edit_item(self, event):

        if self.m_button_edit.GetLabel()== "Edit":
            self.unlock_inputs()
            self.m_button_edit.SetLabel("Cancel")
        elif self.m_button_edit.GetLabel() == "Cancel":
            self.Destroy()


    def delete_item(self, event):
        form_data = self.read_form()  # a dict object

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
                """find if record already exists for this username"""
                cursor.execute(
                    "SELECT item_model, COUNT(*) FROM discontinue_items WHERE item_model = %s GROUP BY item_model",
                    (form_data['model_name'],))

                # gets the number of rows returned by database for the above sql command
                row_count = cursor.rowcount
                print("number of rows returned by database for this model name: {}".format(row_count))

                if row_count == 0:

                    print('item not found in the database')


                    msg = "Item not found in the database"
                    abc = wx.MessageBox(msg, "STOP!",
                                        wx.OK | wx.ICON_INFORMATION, )
                else:
                    msg1 = "Do you really want to delete this item?"
                    abc = wx.MessageBox(msg1, "STOP!",
                                        wx.YES | wx.NO | wx.ICON_STOP, )
                    if abc == wx.YES:
                        print("you selected yes which means you want to delete the item")
                        # update record that already exists for the same serial Number
                        sql1 = "DELETE FROM discontinue_items WHERE item_model = %s"
                        val = (form_data['model_name'])
                        cursor.execute(sql1, val)
                        connection.commit()
                        self.Parent.refresh()
                    elif abc == wx.NO:
                        print("No changes made in the database.")

        except pymysql.err.OperationalError as error:
            print(error)
            self.m_staticText_login_msg.SetLabel("Connection Error! Could not submit record")

        finally:
            connection.close()
            self.Destroy()



    def deactivate_item(self, event):
        form_data = self.read_form()  # a dict object

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
                """find if record already exists for this item"""
                cursor.execute(
                    "SELECT item_model, COUNT(*) FROM discontinue_items WHERE item_model = %s GROUP BY item_model",
                    (form_data['model_name'],))

                # gets the number of rows returned by database for the above sql command
                row_count = cursor.rowcount
                print("number of rows returned by database for this model: {}".format(row_count))

                if row_count == 0:

                    print('Item not found in the database')


                    msg = "Item not found in the database"
                    abc = wx.MessageBox(msg, "STOP!",
                                        wx.OK | wx.ICON_INFORMATION, )
                else:
                    msg1 = "Do you want to deactivate this item?"
                    abc = wx.MessageBox(msg1, "STOP!",
                                        wx.YES | wx.NO | wx.ICON_STOP, )
                    if abc == wx.YES:
                        print("you selected yes which means you want to deactivate the item")
                        # update record that already exists for the same serial Number
                        sql1 = "UPDATE discontinue_items SET is_active = %s WHERE item_model = %s"
                        val = (False, form_data['model_name'])
                        cursor.execute(sql1, val)
                        connection.commit()
                        self.Parent.refresh()
                    elif abc == wx.NO:
                        print("No changes made in the database.")

        except pymysql.err.OperationalError as error:
            print(error)
            self.m_staticText_login_msg.SetLabel("Connection Error! Could not submit record")

        finally:
            connection.close()
            self.Destroy()



    def activate_item(self, event):
        form_data = self.read_form()  # a dict object

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
                """find if record already exists for this username"""
                cursor.execute(
                "SELECT item_model, COUNT(*) FROM discontinue_items WHERE item_model = %s GROUP BY item_model",
                (form_data[ 'model_name' ],))

                # gets the number of rows returned by database for the above sql command
                row_count = cursor.rowcount
                print("number of rows returned by database for this item: {}".format(row_count))

                if row_count == 0:

                    print('Item not found in the database')


                    msg = "Item not found in the database"
                    abc = wx.MessageBox(msg, "STOP!",
                                        wx.OK | wx.ICON_INFORMATION, )
                else:
                    msg1 = "Do you want to activate the item?"
                    abc = wx.MessageBox(msg1, "STOP!",
                                        wx.YES | wx.NO | wx.ICON_STOP, )
                    if abc == wx.YES:
                        print("you selected yes which means you want to activate the item")
                        # update record that already exists for the same serial Number
                        sql1 = "UPDATE discontinue_items SET is_active = %s WHERE item_model = %s"
                        val = (True, form_data[ 'model_name' ])
                        cursor.execute(sql1, val)
                        connection.commit()
                        self.Parent.refresh()
                    elif abc == wx.NO:
                        print("No changes made in the database.")

        except pymysql.err.OperationalError as error:
            print(error)
            self.m_staticText_login_msg.SetLabel("Connection Error! Could not submit record")

        finally:
            connection.close()
            self.Destroy()


    def read_form(self):
        """This function reads the vlaues from all text control fields in the new user form and return it as dictionary"""

        data = {
            'model_name': self.m_textCtrl_model_name.GetValue().lstrip().upper(),
            'discont_condition': self.m_textCtrl_discont_condition.GetValue().lstrip().upper(),
            'discontinue_date' : self.m_textCtrl_discontinue_date.GetValue().lstrip(),
            'item_is_active': self.m_checkBox_is_active.GetValue(),
        }
        print(data)
        return data


    def submit(self, event):

        form_data = self.read_form() # a dict object

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
                """find if record already exists for this username"""
                cursor.execute(
                    "SELECT item_model, COUNT(*) FROM discontinue_items WHERE item_model = %s GROUP BY item_model",
                    (form_data[ 'model_name' ],))

                # gets the number of rows returned by database for the above sql command
                row_count = cursor.rowcount
                print("number of rows returned by database for this item: {}".format(row_count))

                if row_count == 0:
                    self.m_staticText_login_msg.SetLabel("Add a new item to the list")
                    """Create a new record if no previous record found"""

                    sql = "INSERT INTO `discontinue_items` (item_model, discontinue_condition, discontinue_date, is_active) VALUES (%s, %s, %s, %s)"

                    cursor.execute(sql,(form_data['model_name'], form_data['discont_condition'], form_data['discontinue_date'], form_data['item_is_active']))

                    #connection is not autocommit by default.So you must commit to save
                    # your changes.
                    connection.commit()

                    # Some things that are done to the form after the submission of data to database
                    print('Connection committed')
                    self.Parent.refresh()
                    self.m_staticText_login_msg.SetLabel('Success! New record added to database.')
                    msg = "Success! New record added to database."
                    abc = wx.MessageBox(msg, "STOP!",
                                        wx.OK | wx.ICON_STOP, )
                else:
                    msg1 = "Do you want to update this item?"
                    abc = wx.MessageBox(msg1, "STOP!",
                                        wx.YES | wx.NO | wx.ICON_STOP, )
                    if abc == wx.YES:
                        print("you selected yes which means you want to update the record")
                        # update record that already exists for the same serial Number
                        sql1 = "UPDATE discontinue_items SET item_model = %s, discontinue_condition = %s, discontinue_date = %s, is_active = %s WHERE item_model = %s"
                        val = (form_data['model_name'], form_data['discont_condition'], form_data['discontinue_date'], form_data['item_is_active'],form_data['model_name'])
                        cursor.execute(sql1, val)
                        connection.commit()
                        # Some stuff that is done after updating database
                        self.Parent.refresh()
                        self.m_button_submit.SetLabel('Submit')
                    elif abc == wx.NO:
                        print("No changes made in the database.")

        except pymysql.err.OperationalError as error:
            print(error)
            self.m_staticText_login_msg.SetLabel("Connection Error! Could not submit record")

        finally:
            connection.close()
            self.Destroy()


    def query_database(self, model):
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
                """find if record exists for this model"""
                cursor.execute(
                    "SELECT * FROM discontinue_items WHERE item_model = %s GROUP BY item_model",
                    (model,))

                info = cursor.fetchall()
                # print(info)


        except pymysql.err.OperationalError as error:
            print(error)
            self.m_staticText_login_msg.SetLabel("Connection Error! ")

        finally:
            connection.close()
        return info

    def load_item(self, model):
        data = self.query_database(model)[0]
        self.m_textCtrl_model_name.SetValue(data['item_model'])
        self.m_textCtrl_discont_condition.SetValue(data[ 'discontinue_condition' ])
        self.m_textCtrl_discontinue_date.SetValue(str(data['discontinue_date']))
        self.m_checkBox_is_active.SetValue(data['is_active'])

