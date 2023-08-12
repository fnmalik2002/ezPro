# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-231-gdf7791bf)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################
import platform
from datetime import datetime as dt

import pyautogui
import pymysql.cursors
import wx.grid
import configsheet_gui_edited as gui
import inventory_add as inv_a
import inventory_remove_for_sold as inv_r
from company_logo import *
import pandas as pd
import inventory_pull as inventory_pull


###########################################################################
## Class Inventory_location
###########################################################################

class Search_Inventory_items(wx.Frame):
    date_today = str(dt.now())
    ip = ''  # IP address of the database server
    user = ''  # limited access username of the database
    password = ''  # limited access user's pw
    db = ''  # database name
    bins = []
    loggedin_user_id = 0
    loggedin_user_username = ''
    loggedin_user_is_manager = False
    loggedin_user_is_active = False
    loggedin_user_is_tier2 = False
    loggedin_user_is_tier3 = False
    loggedin_user_first_name = ''
    loggedin_user_last_name = ''
    data_selected_sheet = {}

    def __init__(self, parent):
        # wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"ezPro - Inventory Management", pos=wx.DefaultPosition,
        #                   size=wx.Size(1240, 600), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        wx.Frame.__init__(self, parent, id = wx.ID_ANY, title = u"ezPro - Inventory Management",
                          pos = wx.DefaultPosition,
                          size = wx.Size(1260,700), style = wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.logo_med = wx.Image(l_med.GetImage()).ConvertToBitmap()
        self.SetIcon(wx.Icon(self.logo_med))
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(255, 255, 255))

        frame_sizer_V = wx.BoxSizer(wx.VERTICAL)

        self.m_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        panel_sizer_v = wx.BoxSizer(wx.VERTICAL)

        topline_sizer_on_panel = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1 = wx.StaticText(self.m_panel, wx.ID_ANY,
                                           u"Find items in eBay inventory by bin number, ez part number or config sheet id",
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)

        self.m_staticText1.SetFont(
            wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Lucida Grande"))

        topline_sizer_on_panel.Add(self.m_staticText1, 1, wx.ALIGN_BOTTOM | wx.ALL, 5)

        self.m_staticText2 = wx.StaticText(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText2.Wrap(-1)

        topline_sizer_on_panel.Add(self.m_staticText2, 2, wx.ALL, 5)

        self.m_bitmap_logo = wx.StaticBitmap(self.m_panel, wx.ID_ANY, wx.Bitmap(self.logo_med),
                                             wx.DefaultPosition, wx.DefaultSize, 0)
        topline_sizer_on_panel.Add(self.m_bitmap_logo, 0, wx.ALL, 5)

        panel_sizer_v.Add(topline_sizer_on_panel, 0, wx.EXPAND, 5)

        self.m_staticline1 = wx.StaticLine(self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        panel_sizer_v.Add(self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5)

        sizer_button_row = wx.BoxSizer(wx.HORIZONTAL)

        sizer_searchbar = wx.BoxSizer(wx.HORIZONTAL)

        self.m_textCtrl_search_bar = wx.TextCtrl(self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                 wx.Size(400, 10),
                                                 0 | wx.TE_PROCESS_ENTER)
        sizer_searchbar.Add(self.m_textCtrl_search_bar, 0, wx.ALL | wx.EXPAND, 5)

        sizer_searchbar.Add((0, 5), 0, wx.EXPAND, 5)

        sizer_button_row.Add(sizer_searchbar, 0, wx.ALL | wx.EXPAND, 0)

        sizer_search_results = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText4 = wx.StaticText(self.m_panel, wx.ID_ANY, u"", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)

        self.m_staticText4.SetFont(
            wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Lucida Grande"))

        sizer_search_results.Add(self.m_staticText4, 0, wx.ALL | wx.EXPAND, 5)

        self.m_button_search_unsold = wx.Button(self.m_panel, wx.ID_ANY, u"Show Unsold", wx.DefaultPosition, wx.Size(130, -1), 0)

        sizer_button_row.Add(self.m_button_search_unsold, 0, wx.ALL, 5)
        #

        self.m_button_search_onlysold = wx.Button(self.m_panel, wx.ID_ANY, u"Show Sold", wx.DefaultPosition,
                                                wx.Size(130, -1), 0)

        sizer_button_row.Add(self.m_button_search_onlysold, 0, wx.ALL, 5)

        self.m_button_search_all = wx.Button(self.m_panel, wx.ID_ANY, u"Show All", wx.DefaultPosition, wx.Size(130, -1), 0)

        # self.m_button_add.SetDefault()
        sizer_button_row.Add(self.m_button_search_all, 0, wx.ALL, 5)


        self.m_button_reset = wx.Button(self.m_panel, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.Size(130, -1),
                                        0)
        sizer_button_row.Add(self.m_button_reset, 0, wx.ALL, 5)

        # add space
        sizer_button_row.Add((80, 0), 0, wx.ALL, 5)
        sizer_new = wx.BoxSizer(wx.HORIZONTAL)
        self.m_button_inv_report = wx.Button(self.m_panel, wx.ID_ANY, u"Inventory Report", wx.DefaultPosition, wx.Size(130, -1),
                                          0)
        sizer_new.Add(self.m_button_inv_report, 0, wx.ALL, 5)

        self.m_button_add_inv = wx.Button(self.m_panel, wx.ID_ANY, u"Add items", wx.DefaultPosition, wx.Size(130, -1),
                                        0)
        sizer_new.Add(self.m_button_add_inv, 0, wx.ALL, 5)

        self.m_button_rem_inv = wx.Button(self.m_panel, wx.ID_ANY, u"Pull Orders", wx.DefaultPosition, wx.Size(130, -1),
                                          0)
        sizer_new.Add(self.m_button_rem_inv, 0, wx.ALL, 5)

        panel_sizer_v.Add(sizer_button_row, 0, wx.ALL | wx.EXPAND, 5)
        panel_sizer_v.Add(sizer_new, 0, wx.ALL | wx.EXPAND, 5)

        panel_sizer_v.Add(sizer_search_results, 0, wx.ALL | wx.EXPAND, 0)

        sizer_for_grid = wx.BoxSizer(wx.VERTICAL)

        self.m_grid = wx.grid.Grid(self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid.CreateGrid(3001, 11)
        self.m_grid.EnableEditing(True)
        self.m_grid.EnableGridLines(True)
        self.m_grid.EnableDragGridSize(True)
        self.m_grid.SetMargins(0, 0)

        # Columns
        self.m_grid.SetColSize(0, 80)
        self.m_grid.SetColSize(1, 110)
        self.m_grid.SetColSize(2, 110)
        self.m_grid.SetColSize(3, 100)
        self.m_grid.SetColSize(4, 160)
        self.m_grid.SetColSize(5, 80)
        self.m_grid.SetColSize(6, 160)
        self.m_grid.SetColSize(7, 100)
        self.m_grid.SetColSize(8, 80)
        self.m_grid.SetColSize(9, 80)
        self.m_grid.SetColSize(10, 80)


        self.m_grid.EnableDragColMove(False)
        self.m_grid.EnableDragColSize(True)
        self.m_grid.SetColLabelValue(0, u"Bin Number")
        self.m_grid.SetColLabelValue(1, u"EZ Part Number")
        self.m_grid.SetColLabelValue(2, u"ConfigSheet ID")
        self.m_grid.SetColLabelValue(3, u"Item ID")
        self.m_grid.SetColLabelValue(4, u"Date Added")
        self.m_grid.SetColLabelValue(5, u"Added by")
        self.m_grid.SetColLabelValue(6, u"Date Removed")
        self.m_grid.SetColLabelValue(7, u"SO Number")
        self.m_grid.SetColLabelValue(8, u"Removed by")
        self.m_grid.SetColLabelValue(9, u"Status")
        self.m_grid.SetColLabelValue(10, u"Days Listed")

        self.m_grid.SetColLabelSize(wx.grid.GRID_AUTOSIZE)
        self.m_grid.SetColLabelAlignment(wx.ALIGN_LEFT, wx.ALIGN_LEFT)

        # Rows

        self.m_grid.EnableDragRowSize(True)
        self.m_grid.SetRowLabelSize(wx.grid.GRID_AUTOSIZE)
        self.m_grid.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults

        self.m_grid.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        sizer_for_grid.Add(self.m_grid, 1, wx.ALL | wx.EXPAND, 5)

        panel_sizer_v.Add(sizer_for_grid, 0, wx.ALL | wx.EXPAND, 0)

        self.m_panel.SetSizer(panel_sizer_v)
        self.m_panel.Layout()
        panel_sizer_v.Fit(self.m_panel)
        frame_sizer_V.Add(self.m_panel, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(frame_sizer_V)
        self.Layout()
        self.m_statusBar = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)

        self.Centre(wx.BOTH)
        # add icons to buttons
        self.m_button_reset.SetBitmap(wx.Bitmap(wx.Image(reset.GetImage()).ConvertToBitmap()))
        self.m_button_search_all.SetBitmap(wx.Bitmap(wx.Image(search_all.GetImage()).ConvertToBitmap()))
        self.m_button_search_unsold.SetBitmap(wx.Bitmap(wx.Image(inventory.GetImage()).ConvertToBitmap()))
        self.m_button_add_inv.SetBitmap(wx.Bitmap(wx.Image(add_item.GetImage()).ConvertToBitmap()))
        self.m_button_rem_inv.SetBitmap(wx.Bitmap(wx.Image(remove_item.GetImage()).ConvertToBitmap()))
        self.m_button_inv_report.SetBitmap(wx.Bitmap(wx.Image(printer.GetImage()).ConvertToBitmap()))

        # Connect Events
        self.m_textCtrl_search_bar.Bind(wx.EVT_TEXT_ENTER, self.search_unsold)
        self.m_button_search_unsold.Bind(wx.EVT_BUTTON, self.search_unsold)
        self.m_button_search_onlysold.Bind(wx.EVT_BUTTON, self.search_sold)
        self.m_button_search_all.Bind(wx.EVT_BUTTON, self.search_all)
        self.m_button_reset.Bind(wx.EVT_BUTTON, self.clear_form)
        self.m_grid.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.row_double_clicked)
        self.m_button_inv_report.Bind(wx.EVT_BUTTON, self.generate_inv_report)
        self.m_button_add_inv.Bind(wx.EVT_BUTTON, self.add_inv)
        self.m_button_rem_inv.Bind(wx.EVT_BUTTON, self.rem_inv)
        self.m_grid.Bind(wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.grid_cell_right_clicked)
        self.m_grid.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.on_cell_left_click)
        self.m_grid.Bind(wx.grid.EVT_GRID_RANGE_SELECT, self.onDragSelection)
        self.selected_item_id = ''

    def __del__(self):
        pass

    def generate_inv_report(self, event):
        event.Skip()
        print("Generate inventory report is clicked")

    def onDragSelection(self, event):
        """
        Gets the cells that are selected by holding the left
        mouse button down and dragging
        """
        items = [ ]
        if self.m_grid.GetSelectionBlockTopLeft():
            top_left = self.m_grid.GetSelectionBlockTopLeft()[ 0 ]
            bottom_right = self.m_grid.GetSelectionBlockBottomRight()[ 0 ]
            cells = [ ]
            rows = range(top_left[ 0 ], bottom_right[ 0 ] + 1)
            cols = range(top_left[ 1 ], bottom_right[ 1 ] + 1)
            # print(rows, cols)
            cells.extend([ (row, col)
                           for row in rows
                           for col in cols ])

            print("You selected the following cells: ", cells)
            items = [ ]
            for cell in cells:
                row, col = cell
                items.append(self.m_grid.GetCellValue(row, 3))
                print(self.m_grid.GetCellValue(row, 3))
            ids = pd.Series(data = items)
            print("Item id of selected items : ", ids.unique())
            return ids.unique()
        else:
            return []

    def printSelectedCells(self, top_left, bottom_right):
        """
        Based on code from http://ginstrom.com/scribbles/2008/09/07/getting-the-selected-cells-from-a-wxpython-grid/
        """
        cells = [ ]

        rows_start = top_left[ 0 ]
        rows_end = bottom_right[ 0 ]

        cols_start = top_left[ 1 ]
        cols_end = bottom_right[ 1 ]

        rows = range(rows_start, rows_end + 1)
        cols = range(cols_start, cols_end + 1)

        cells.extend([ (row, col)
                       for row in rows
                       for col in cols ])

        print("You selected the following cells: ", cells)
        items = []
        for cell in cells:
            row, col = cell
            items.append(self.m_grid.GetCellValue(row, 3))
            print(self.m_grid.GetCellValue(row, 3))
        ids = pd.Series(data=items)
        print("Item id of selected items : ", ids.unique())
        # print("Item id of selected items : ", items)

    def on_cell_left_click(self, event):
        """
        Shows whole row as selected when any cell in a row is left clicked in new tab
        :param event:
        :return:
        """
        print("cell left clicked ")
        self.m_grid.SelectRow(event.GetRow(), False)

    def get_icon(self, txt):
        mrk_sold = wx.Bitmap(wx.Image(sold.GetImage()).ConvertToBitmap())
        mrk_deman = wx.Bitmap(wx.Image(deman.GetImage()).ConvertToBitmap())
        mrk_out = wx.Bitmap(wx.Image(delete_icon.GetImage()).ConvertToBitmap())
        mrk_returned = wx.Bitmap(wx.Image(return_sold.GetImage()).ConvertToBitmap())
        mov_bin = wx.Bitmap(wx.Image(move_bin.GetImage()).ConvertToBitmap())
        icns = {
            "Move Bin": mov_bin,
            "Mark Sold": mrk_sold,
            "Mark Deman": mrk_deman,
            "Mark Deleted": mrk_out,
            "Mark Returned": mrk_returned,
        }
        return icns[txt]

    def OnShowPopup(self, event):
        """
        logic for what will happen when context menu item is clicked in current tab only
        :param event:
        :return:
        """
        pos1 = event.GetPosition()
        if platform.system() == 'Darwin':
            x, y = pos1
            print("x = ", x, "y = ", y)
            # pos = self.m_panel.ScreenToClient(x + 170, y + 170)
            pos = self.m_panel.ScreenToClient(x + 40, y + 270)
        elif platform.system() == 'Windows':
            pos = self.m_panel.ScreenToClient(pos1)
        else:
            print(platform.system())

        self.m_panel.PopupMenu(self.popupmenu, pos)

    def get_so_number(self):
        """
        Presents a dialogbox to get ez part number from user
        :return:
        """
        dlg = wx.TextEntryDialog(self, 'Please enter sales order number', 'SO# Required')
        dlg.SetValue("")
        if dlg.ShowModal() == wx.ID_OK:
            so_n = dlg.GetValue().lstrip()
            print('You entered: %s\n' % dlg.GetValue())
        else:
            so_n = ''
        dlg.Destroy()
        return so_n

    def get_new_bin(self):
        """
        Presents a dialogbox to get ez part number from user
        :return:
        """
        dlg = wx.TextEntryDialog(self, 'Please enter new bin number', 'Bin# Required')
        dlg.SetValue("")
        if dlg.ShowModal() == wx.ID_OK:
            new_bin_no = dlg.GetValue().lstrip().upper()
            print('You entered: %s\n' % new_bin_no)
        else:
            new_bin_no = ''
        dlg.Destroy()
        return new_bin_no

    def OnPopupItemSelected(self, event):
        """
        Logic for actions of each item clicked in context menu in both new and listed tabs
        :param event:
        :return:
        """
        item = self.popupmenu.FindItemById(event.GetId())
        text_clicked = item.GetItemLabel()

        if text_clicked == "    Move Bin":
            print(" you selected Move Bin")
            if self.data_selected_sheet['status'] != 'Sold' and self.data_selected_sheet['status'] != 'Deman':
                resp = self.get_new_bin()
                if resp != '':
                    print(resp)
                    self.move_bin(resp)
                    self.SetStatusText("Bin # for selected item is changed successfully")
                else:
                    # dlg = wx.MessageDialog(self, 'Please enter new bin number', 'Stop', wx.ICON_STOP)
                    # if dlg.ShowModal() == wx.ID_OK:
                    #     dlg.Destroy()
                    # self.SetStatusText("New bin number is required")
                    pass
            else:
                dlg = wx.MessageDialog(self, 'This item is already marked as {}. No need to change its bin# now'.format(self.data_selected_sheet['status']), 'Stop', wx.ICON_STOP)
                if dlg.ShowModal() == wx.ID_OK:
                    dlg.Destroy()
                self.SetStatusText("This item is already marked as {}. No need to change its bin# now".format(self.data_selected_sheet['status']))

        elif text_clicked == "    Mark Sold":
            print(" you selected sold")
            if self.data_selected_sheet['status'] != 'Sold' and self.data_selected_sheet['status'] != 'Deman':
                resp = self.get_so_number()
                if resp != '':
                    print(resp)
                    self.mark_sold(resp)
                    self.SetStatusText("Selected item is marked as sold successfully")
                else:
                    dlg = wx.MessageDialog(self, 'Please enter sales order number', 'Stop', wx.ICON_STOP)
                    if dlg.ShowModal() == wx.ID_OK:
                        dlg.Destroy()
                    self.SetStatusText("Sales order number is required")
            else:
                dlg = wx.MessageDialog(self, 'This item is already marked as {}'.format(self.data_selected_sheet['status']), 'Stop', wx.ICON_STOP)
                if dlg.ShowModal() == wx.ID_OK:
                    dlg.Destroy()
                self.SetStatusText("This item is already marked as {}".format(self.data_selected_sheet['status']))


        elif text_clicked == "    Mark Deman":
            print("you selected Deman")

            if self.data_selected_sheet['status'] != 'Deman' and self.data_selected_sheet['status'] != 'Sold':
                self.mark_deman()
                self.SetStatusText("Selected item is marked as Deman successfully")
            else:
                dlg = wx.MessageDialog(self, 'This item is already marked as {}'.format(self.data_selected_sheet['status']), 'Stop', wx.ICON_STOP)
                if dlg.ShowModal() == wx.ID_OK:
                    dlg.Destroy()
                self.SetStatusText("This item is already marked as {}".format(self.data_selected_sheet['status']))

        elif text_clicked == "    Mark Deleted":
            print("you selected delete")
            dlg = wx.MessageDialog(self, 'Do you really want to delete this record?', 'Stop' ,wx.YES_NO | wx.ICON_QUESTION)

            if dlg.ShowModal() == wx.ID_YES:
                dlg.Destroy()
                self.mark_deleted()
            else:
                self.SetStatusText("No changes made in the database")
                return

        elif text_clicked == "    Mark Returned":
            print(" you selected Mark Returned")
            if self.data_selected_sheet['status'] == 'Sold' and self.data_selected_sheet['status'] != 'Deman':
                self.mark_returned()
                self.SetStatusText("Selected item is successfully marked as returned")
            else:
                dlg = wx.MessageDialog(self, 'Can not return an unsold item', 'Stop', wx.ICON_STOP)
                if dlg.ShowModal() == wx.ID_OK:
                    dlg.Destroy()
                self.SetStatusText("Can not return an unsold item")



    def move_bin(self, resp):
        # Connect to the database
        cursor = pymysql.cursors.DictCursor
        connection = pymysql.connect(host = self.ip,
                                     user = self.user,
                                     password = self.password,
                                     db = self.db,
                                     charset = 'utf8mb4',
                                     cursorclass = cursor)

        try:
            with connection.cursor() as cursor:

                sql = "UPDATE item_to_bin SET bin_number=%s WHERE item_id=%s"
                vals = (resp, self.selected_item_id)
                cursor.execute(sql, vals)

                # connection is not autocommit by default.So you must commit to save
                # your changes.
                connection.commit()
                print('Connection committed')
                txt = "Bin number is successfully changed to {} for item id {}".format(resp, self.selected_item_id)
                self.SetStatusText(txt)

        except pymysql.err.OperationalError as error:
            print(error)

        finally:
            connection.close()
            self.m_textCtrl_search_bar.SetValue(self.selected_item_id)
            self.search_all(event = wx.EVT_BUTTON)

    def mark_sold(self, resp):
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

                sql = "UPDATE item_to_bin SET is_sold=True, date_removed=%s, removed_by=%s, sales_order=%s WHERE item_id=%s"
                vals = (
                    self.date_today, self.loggedin_user_username.upper(), resp, self.selected_item_id)
                cursor.execute(sql, vals)

                # connection is not autocommit by default.So you must commit to save
                # your changes.
                connection.commit()
                print('Connection committed')
                txt = "item {} is successfully marked as sold".format(self.selected_item_id)
                self.SetStatusText(txt)

        except pymysql.err.OperationalError as error:
            print(error)

        finally:
            connection.close()
            self.m_textCtrl_search_bar.SetValue(self.selected_item_id)
            # self.search_all(event=wx.EVT_BUTTON)
            self.search_unsold(event = wx.EVT_BUTTON)

    def mark_deman(self):
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
                sql = "UPDATE item_to_bin SET removed_by=%s,  is_not_sold_in_three_months=%s, date_removed=%s WHERE item_id=%s"
                val = (self.loggedin_user_username.upper(), True, self.date_today, self.selected_item_id)

                cursor.execute(sql, val)

                # connection is not autocommit by default.So you must commit to save
                # your changes.
                connection.commit()
                print('Connection committed')
                txt = "item {} is successfully marked as Deman".format(self.selected_item_id)
                self.SetStatusText(txt)

        except pymysql.err.OperationalError as error:
            print(error)

        finally:
            connection.close()
            self.m_textCtrl_search_bar.SetValue(self.selected_item_id)
            self.search_all(event=wx.EVT_BUTTON)

    def mark_deleted(self):
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
                # delete this record
                sql = "DELETE FROM item_to_bin WHERE item_id=%s"
                val = (self.selected_item_id)

                cursor.execute(sql, val)

                # connection is not autocommit by default.So you must commit to save
                # your changes.
                connection.commit()
                print('Connection committed')
                txt = "item {} is successfully deleted from inventory".format(self.selected_item_id)
                self.SetStatusText(txt)

        except pymysql.err.OperationalError as error:
            print(error)

        finally:
            connection.close()
            self.search_unsold(event=wx.EVT_BUTTON)

    def mark_returned(self):
        """Marks an item as not sold but keeps the date sold and so# sold to and employee id who removed it when it was sold"""
        # Connect to the database
        cursor = pymysql.cursors.DictCursor
        connection = pymysql.connect(host = self.ip,
                                     user = self.user,
                                     password = self.password,
                                     db = self.db,
                                     charset = 'utf8mb4',
                                     cursorclass = cursor)

        try:
            with connection.cursor() as cursor:

                sql = "UPDATE item_to_bin SET is_sold=False WHERE item_id=%s"
                vals = self.selected_item_id
                cursor.execute(sql, vals)

                # connection is not autocommit by default.So you must commit to save
                # your changes.
                connection.commit()
                print('Connection committed')
                txt = "item {} is successfully marked as returned".format(self.selected_item_id)
                self.SetStatusText(txt)

        except pymysql.err.OperationalError as error:
            print(error)

        finally:
            connection.close()
            self.m_textCtrl_search_bar.SetValue(self.selected_item_id)
            self.search_all(event = wx.EVT_BUTTON)

    def grid_cell_right_clicked(self, event):
        print('cell right clicked')
        print("Logged-in user & ID = ", self.loggedin_user_username, self.loggedin_user_id)
        self.selected_item_id = self.m_grid.GetCellValue(event.GetRow(), 3)

        dte = self.date_today
        ez = str(self.m_grid.GetCellValue(event.GetRow(), 1).lstrip())
        usr_name = self.loggedin_user_username.upper()
        sheet_id = self.m_grid.GetCellValue(event.GetRow(), 2).lstrip()
        stts = self.m_grid.GetCellValue(event.GetRow(), 9).lstrip()
        bin_n = self.m_grid.GetCellValue(event.GetRow(), 0).lstrip()
        self.data_selected_sheet = {
            'date_today': dte,
            'ez_no': ez,
            'sht_id': sheet_id,
            'username': usr_name,
            'itm_id': self.selected_item_id,
            'bin_no': bin_n,
            'status': stts,
        }



        self.popupmenu = wx.Menu()
        if self.selected_item_id != '':
            lst = [ "Move Bin", "Mark Sold", "Mark Deman", "Mark Deleted","Mark Returned" ]
            for text in lst:
                item = self.popupmenu.Append(-1, "    " + text)
                item.SetBitmap(self.get_icon(text))
                self.Bind(wx.EVT_MENU, self.OnPopupItemSelected, item)
            # print(item)
            self.m_panel.Bind(wx.EVT_CONTEXT_MENU, self.OnShowPopup)
            if platform.system() == 'Darwin':
                self.OnShowPopup(event = event)
        else:
            return

    def add_inv(self, event):
        frame = inv_a.Add_Inventory_items(self)
        frame.ip = self.ip
        frame.db = self.db
        frame.user = self.user
        frame.password = self.password
        frame.bins = self.bins
        frame.m_textCtrl_item_ez_no.SetFocus()
        frame.loggedin_user_username = self.loggedin_user_username
        frame.Show()


    def rem_inv(self, event):
        frame = inventory_pull.Inventory_Pulls(self)
        frame.ip = self.ip
        frame.db = self.db
        frame.user = self.user
        frame.password = self.password
        frame.bins = self.bins
        frame.m_textCtrl_pn.SetFocus()
        frame.loggedin_user_username = self.loggedin_user_username
        frame.Show()


    def row_double_clicked(self, event):
        print("Row_double_clicked")
        value = str(self.m_grid.GetCellValue(event.GetRow(), event.GetCol()))
        col_name = str(self.m_grid.GetColLabelValue(event.GetCol()))
        print(col_name, value)

        if col_name == 'Bin Number':
            sql = "SELECT * FROM item_to_bin WHERE bin_number=%s ORDER BY record_id ASC LIMIT 3000"
            val = value
            self.load_grid(sql, val)
        elif col_name == 'EZ Part Number':
            sql = "SELECT * FROM item_to_bin WHERE ez_no=%s ORDER BY record_id ASC LIMIT 3000"
            val = value
            self.load_grid(sql, val)
        elif col_name == 'ConfigSheet ID':
            print("new_cell_double_clicked")
            sheet_id = value

            print(sheet_id)
            if not self.loggedin_user_is_tier3:
                try:
                    loaded_frame = gui.MyConfigSheet(self)
                    loaded_frame.ip = self.ip
                    print(loaded_frame.ip)
                    loaded_frame.user = self.user
                    loaded_frame.password = self.password
                    loaded_frame.db = self.db
                    loaded_frame.bins = self.bins
                    loaded_frame.loggedin_user_id = self.loggedin_user_id
                    loaded_frame.loggedin_user_username = self.loggedin_user_username
                    loaded_frame.loggedin_user_is_manager = self.loggedin_user_is_manager
                    loaded_frame.loggedin_user_is_active = self.loggedin_user_is_active
                    loaded_frame.loggedin_user_first_name = self.loggedin_user_first_name
                    loaded_frame.loggedin_user_last_name = self.loggedin_user_last_name
                    loaded_frame.m_button_submit.Disable()
                    loaded_frame.load_gui_form_from_database(sheet_id)
                    loaded_frame.set_window_size()
                    loaded_frame.Show()
                except Exception as e:
                    print(e)
                else:
                    print("Logged in user is not allowed to open config sheets")
                    pass
        elif col_name == 'Date Added':
            sql = "SELECT * FROM item_to_bin WHERE date_added LIKE %s ORDER BY record_id ASC LIMIT 3000"
            val = value
            self.load_grid(sql, val)
        elif col_name == 'Status':
            if value == 'Sold':
                sql = "SELECT * FROM item_to_bin WHERE is_sold=%s ORDER BY record_id ASC LIMIT 3000"
                val = True
            elif value == 'Deman':
                sql = "SELECT * FROM item_to_bin WHERE is_not_sold_in_three_months=%s ORDER BY record_id ASC LIMIT 3000"
                val = True
            else:
                sql = "SELECT * FROM item_to_bin WHERE is_not_sold_in_three_months=%s AND is_sold=%s ORDER BY record_id ASC LIMIT 3000"
                val = (False, False)
            self.clear_row_color()
            self.load_grid(sql, val)

    # Virtual event handlers, override them in your derived class
    def clear_form(self, event):
        self.m_textCtrl_search_bar.SetValue('')
        self.m_grid.ClearGrid()
        self.clear_row_color()

    def read_form(self):
        # out = []
        search_input = self.m_textCtrl_search_bar.GetValue().lstrip()
        if search_input:
            kind = ""
            # y = [c for c in search_input]
            # print(y)
            print(search_input[:5].upper(), type(search_input[0]))
            if search_input[:5].upper() in self.bins:
                kind = 'bin_no'
                print("its in bin")
            elif search_input.count('-') == 2:
                kind = 'item_id'
                print("its item_id")
            elif any(c.isalpha() for c in search_input):
                print("its ez number")
                kind = 'ez_no'
            else:
                print("its sheet number")
                kind = 'sheet_id'
            return search_input
        else:
            return ""

    def search_all(self, event):
        data = self.read_form()

        self.clear_row_color()
        print(data)
        if data:
            sql = "SELECT * FROM item_to_bin WHERE sheet_id=%s OR item_id=%s OR bin_number LIKE %s OR ez_no LIKE %s OR date_added LIKE %s ORDER BY bin_number ASC LIMIT 3000"
            val = (data, data, data, data, data)
            # Connect to the database
        else:
            sql = "SELECT * FROM item_to_bin ORDER BY record_id DESC LIMIT 3000"
            val = ""
        # Connect to the database
        self.load_grid(sql, val)

    def search_unsold(self, event):
        data = self.read_form()
        self.clear_row_color()
        print(data)
        if data:
            sql = "SELECT * FROM item_to_bin WHERE is_sold=%s AND is_not_sold_in_three_months=%s AND (sheet_id=%s OR item_id=%s OR bin_number LIKE %s OR ez_no LIKE %s OR date_added LIKE %s) ORDER BY bin_number ASC LIMIT 3000"
            val = (False, False, data, data, data, data, data)
        else:
            sql = "SELECT * FROM item_to_bin WHERE is_sold=%s AND is_not_sold_in_three_months=%s ORDER BY record_id DESC LIMIT 3000"
            val = (False, False)
        # Connect to the database
        self.load_grid(sql, val)

    def search_sold(self, event):
        data = self.read_form()
        self.clear_row_color()
        print(data)
        if data:
            sql = "SELECT * FROM item_to_bin WHERE is_sold=%s AND is_not_sold_in_three_months=%s AND (sheet_id=%s OR item_id=%s OR bin_number LIKE %s OR ez_no LIKE %s OR date_added LIKE %s) ORDER BY bin_number ASC LIMIT 3000"
            val = (True, False, data, data, data, data, data)
        else:
            sql = "SELECT * FROM item_to_bin WHERE is_sold=%s AND is_not_sold_in_three_months=%s ORDER BY record_id DESC LIMIT 3000"
            val = (True, False)
        # Connect to the database
        self.load_grid(sql, val)

    def row_color(self, row_number, color):
        r = row_number
        # change row colors
        # attr = wx.grid.GridCellAttr()
        attr = self.m_grid.GetOrCreateCellAttr(r, 1)
        attr.SetBackgroundColour(color)
        self.m_grid.SetRowAttr(r, attr)

    def clear_row_color(self):
        i = 0
        while i < self.m_grid.GetNumberRows():
            self.row_color(i, "white")
            i = i + 1

    def load_grid(self, sql, val):
        self.m_grid.ClearGrid()

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
                if val == "":
                    cursor.execute(sql)
                else:
                    cursor.execute(sql, val)
                # gets the number of rows returned by database for the above sql command
                row_count = cursor.rowcount
                data = cursor.fetchall()

                if row_count == 0:
                    # row_count = 0
                    print("number of rows returned by database for this item: {}".format(row_count))
                    self.SetStatusText("No record found")

                else:
                    self.SetStatusText("{} records found".format(row_count))
                    print(data)
                    n = 0
                    r = 0
                    while n < len(data) and r < row_count:
                        lst = data[n]
                        # print(type(lst['date_removed']), type(lst['is_sold']))
                        self.m_grid.SetCellValue(r, 0, str(lst['bin_number']))
                        self.m_grid.SetCellValue(r, 1, str(lst['ez_no']))
                        self.m_grid.SetCellValue(r, 2, str(lst['sheet_id']))
                        self.m_grid.SetCellValue(r, 3, str(lst['item_id']))
                        self.m_grid.SetCellValue(r, 4, str(lst['date_added']))
                        self.m_grid.SetCellValue(r, 5, str(lst['added_by']))
                        if not lst['date_removed'] == None:
                            self.m_grid.SetCellValue(r, 6, str(lst['date_removed']))
                        else:
                            self.m_grid.SetCellValue(r, 6, "")

                        if not lst['sales_order'] == None:
                            self.m_grid.SetCellValue(r, 7, str(lst[ 'sales_order' ]))
                        else:
                            self.m_grid.SetCellValue(r, 7, "")
                        if not lst['removed_by'] == None:
                            self.m_grid.SetCellValue(r, 8, str(lst[ 'removed_by' ]))
                        else:
                            self.m_grid.SetCellValue(r, 8, "")
                        if lst['is_sold'] == 1:
                            sold_in_days = (lst[ 'date_removed' ] - lst[ 'date_added' ]).days
                            sold_in_hours = (lst[ 'date_removed' ] - lst[ 'date_added' ]).seconds // 3600
                            self.m_grid.SetCellValue(r, 9, "Sold")
                            attr = self.m_grid.GetOrCreateCellAttr(r, 1)
                            attr.SetBackgroundColour(wx.Colour(113, 230, 113))
                            self.m_grid.SetRowAttr(r, attr)
                            # self.row_color(r, "GREEN")
                            if sold_in_days > 0:
                                self.m_grid.SetCellValue(r, 10, str(sold_in_days)+" days")
                            else:
                                self.m_grid.SetCellValue(r, 10, str(sold_in_hours)+" hours")

                        elif lst['is_not_sold_in_three_months'] == 1:
                            deman_in_days = (lst['date_removed'] - lst['date_added']).days
                            deman_in_hours = (lst['date_removed'] - lst['date_added']).seconds // 3600
                            self.m_grid.SetCellValue(r, 9, "Deman")
                            if deman_in_days > 0:
                                self.m_grid.SetCellValue(r, 10, str(deman_in_days)+" days")
                            else:
                                self.m_grid.SetCellValue(r, 10, str(deman_in_hours)+" hours")
                        else:
                            not_deman_in_days = (dt.now() - lst['date_added']).days
                            not_deman_in_hours = (dt.now() - lst['date_added']).seconds // 3600
                            self.m_grid.SetCellValue(r, 9, "")
                            if not_deman_in_days > 0:
                                self.m_grid.SetCellValue(r, 10, str(not_deman_in_days)+" days")
                            else:
                                self.m_grid.SetCellValue(r, 10, str(not_deman_in_hours)+" hours")

                        r = r + 1
                        n = n + 1

        except pymysql.err.OperationalError as error:
            print(error)

        finally:
            connection.close()

    def get_screen_size(self):
        view_width, view_height = pyautogui.size()

        screen_size = [view_width, view_height]
        print("Screen dimensions", screen_size)
        return (view_width, view_height)

    def set_window_size(self):
        w, h = self.get_screen_size()
        self.Size = (1240, h - 80)
        self.SetSizeHints(wx.DefaultSize, wx.Size(1240, h-80))
        self.Centre()

#
# if __name__ == '__main__':
#     app = wx.App(False)
#     frame = Search_Inventory_items(None)
#     frame.m_textCtrl_search_bar.SetFocus()
#     frame.Show()
#     app.MainLoop()
