# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-40-g8042f487)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import pygame.camera
from smbShare import SMBShare as smb
from company_logo import *

###########################################################################
## Class NewUser
###########################################################################

class Pictures(wx.Frame):
    folder_id = ''

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(900, 700), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        # wx.InitAllImageHandlers()
        self.logo_med = wx.Image(l_med.GetImage()).ConvertToBitmap()
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

        bSizer3.Add((0, 50), 0, wx.EXPAND, 5)

        bSizer2.Add(bSizer3, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        bSizer13 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button_take_photo = wx.Button(self.m_panel_button_panel, wx.ID_ANY, u"Take Photo", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        bSizer13.Add(self.m_button_take_photo, 0, wx.ALL, 5)

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

        self.m_notebook2 = wx.Notebook(self.m_panel_grid_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.m_panel7 = wx.Panel(self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), wx.TAB_TRAVERSAL)
        gSizer1 = wx.GridSizer(3, 4, 10, 10)

        self.m_bitmap_1 = wx.StaticBitmap(self.m_panel7, wx.ID_ANY, wx.Bitmap(u"bass.jpg", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.Size(-1, -1), wx.BORDER_THEME)
        # self.m_bitmap_1.SetMinSize(wx.Size(100, 50))
        # self.m_bitmap_1.SetMaxSize(wx.Size(200, 100))
        gSizer1.Add(self.m_bitmap_1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 10)

        self.m_bitmap_2 = wx.StaticBitmap(self.m_panel7, wx.ID_ANY, wx.Bitmap(u"bass.jpg", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.Size(200, 100), wx.BORDER_THEME)
        # self.m_bitmap_2.SetMinSize(wx.Size(100, 50))
        # self.m_bitmap_2.SetMaxSize(wx.Size(200, 100))
        gSizer1.Add(self.m_bitmap_2, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 10)

        self.m_bitmap_3 = wx.StaticBitmap(self.m_panel7, wx.ID_ANY, wx.Bitmap(u"bass.jpg", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.Size(200, 100), wx.BORDER_THEME)
        # self.m_bitmap_3.SetMinSize(wx.Size(100, 50))
        # self.m_bitmap_3.SetMaxSize(wx.Size(200, 100))
        gSizer1.Add(self.m_bitmap_3, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 10)

        self.m_bitmap_4 = wx.StaticBitmap(self.m_panel7, wx.ID_ANY, wx.Bitmap(u"bass.jpg", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.Size(200, 100), wx.BORDER_THEME)
        # self.m_bitmap_4.SetMinSize(wx.Size(100, 50))
        # self.m_bitmap_4.SetMaxSize(wx.Size(200, 100))
        gSizer1.Add(self.m_bitmap_4, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 10)

        self.m_bitmap_5 = wx.StaticBitmap(self.m_panel7, wx.ID_ANY, wx.Bitmap(u"bass.jpg", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.Size(200, 100), wx.BORDER_THEME)
        # self.m_bitmap_5.SetMinSize(wx.Size(100, 50))
        # self.m_bitmap_5.SetMaxSize(wx.Size(200, 100))
        gSizer1.Add(self.m_bitmap_5, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 10)

        self.m_bitmap_6 = wx.StaticBitmap(self.m_panel7, wx.ID_ANY, wx.Bitmap(u"bass.jpg", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.Size(200, 100), wx.BORDER_THEME)
        # self.m_bitmap_6.SetMinSize(wx.Size(100, 50))
        # self.m_bitmap_6.SetMaxSize(wx.Size(200, 100))
        gSizer1.Add(self.m_bitmap_6, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 10)

        self.m_bitmap_7 = wx.StaticBitmap(self.m_panel7, wx.ID_ANY, wx.Bitmap(u"bass.jpg", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.Size(200, 100), wx.BORDER_THEME)
        # self.m_bitmap_7.SetMinSize(wx.Size(100, 50))
        # self.m_bitmap_7.SetMaxSize(wx.Size(200, 100))
        gSizer1.Add(self.m_bitmap_7, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 10)

        self.m_bitmap_8 = wx.StaticBitmap(self.m_panel7, wx.ID_ANY, wx.Bitmap(u"bass.jpg", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.Size(200, 100), wx.BORDER_THEME)
        # self.m_bitmap_8.SetMinSize(wx.Size(100, 50))
        # self.m_bitmap_8.SetMaxSize(wx.Size(200, 100))
        gSizer1.Add(self.m_bitmap_8, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 10)

        self.m_bitmap_9 = wx.StaticBitmap(self.m_panel7, wx.ID_ANY, wx.Bitmap(u"bass.jpg", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.Size(200, 100), wx.BORDER_THEME)
        # self.m_bitmap_9.SetMinSize(wx.Size(100, 50))
        # self.m_bitmap_9.SetMaxSize(wx.Size(200, 100))
        gSizer1.Add(self.m_bitmap_9, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 10)

        self.m_bitmap_10 = wx.StaticBitmap(self.m_panel7, wx.ID_ANY, wx.Bitmap(u"bass.jpg", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.Size(200, 100), wx.BORDER_THEME)
        # self.m_bitmap_10.SetMinSize(wx.Size(100, 50))
        # self.m_bitmap_10.SetMaxSize(wx.Size(200, 100))
        gSizer1.Add(self.m_bitmap_10, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 10)

        self.m_bitmap_11 = wx.StaticBitmap(self.m_panel7, wx.ID_ANY, wx.Bitmap(u"bass.jpg", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.Size(200, 100), wx.BORDER_THEME)
        # self.m_bitmap_11.SetMinSize(wx.Size(100, 50))
        # self.m_bitmap_11.SetMaxSize(wx.Size(200, 100))
        gSizer1.Add(self.m_bitmap_11, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 10)

        self.m_bitmap_12 = wx.StaticBitmap(self.m_panel7, wx.ID_ANY, wx.Bitmap(u"bass.jpg", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.Size(200, 100), wx.BORDER_THEME)
        # self.m_bitmap_12.SetMinSize(wx.Size(100, 50))
        # self.m_bitmap_12.SetMaxSize(wx.Size(200, 100))
        gSizer1.Add(self.m_bitmap_12, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 10)


        self.m_panel7.SetSizer(gSizer1)
        self.m_panel7.Layout()
        gSizer1.Fit(self.m_panel7)
        self.m_notebook2.AddPage(self.m_panel7, u"Photo Folder", True)

        bSizer9.Add(self.m_notebook2, 0, wx.EXPAND | wx.ALL, 0)

        self.m_panel_grid_panel.SetSizer(bSizer9)
        self.m_panel_grid_panel.Layout()
        bSizer9.Fit(self.m_panel_grid_panel)
        bSizer_main.Add(self.m_panel_grid_panel, 1, wx.ALL | wx.EXPAND, 0)

        self.SetSizer(bSizer_main)
        self.Layout()

        self.Centre(wx.BOTH)


        self.bitmap_list = [self.m_bitmap_1, self.m_bitmap_2, self.m_bitmap_3, self.m_bitmap_4, self.m_bitmap_5,
                            self.m_bitmap_6,
                            self.m_bitmap_7,
                            self.m_bitmap_8, self.m_bitmap_9, self.m_bitmap_10, self.m_bitmap_11, self.m_bitmap_12]
        # Connect Events
        self.m_button_take_photo.Bind(wx.EVT_BUTTON, self.add_picture)
        self.Show()

    def __del__(self):
        pass

    def shoot_pic(self, pic_no):

        # initializing the camera
        pygame.camera.init()

        # make the list of all available cameras
        camlist = pygame.camera.list_cameras()
        print(camlist)

        # if camera is detected or not
        if camlist:

            # initializing the cam variable with default camera
            cam = pygame.camera.Camera(camlist[0], (1280, 720))

            # opening the camera
            cam.start()

            # capturing the single image
            image = cam.get_image()

            # saving the image
            pic_name = "{}.jpg".format(pic_no)
            pygame.image.save(image, pic_name)

        else:
            print("No camera on current device")
            pic_name = ""
        return pic_name

    def add_picture(self, event):
        mysmb = smb('RHEL8', '192.168.1.14', 'Anonymous')
        mysmb.connect_with_smb_share()
        t = len(mysmb.get_img_list(self.folder_id))
        if t < 12:
            img = self.shoot_pic(t)
            mysmb.transfer_image(self.folder_id, img, "{}.jpg".format(t))

            # self.m_bitmap_1.SetBitmap(wx.Image(img, wx.BITMAP_TYPE_ANY).ConvertToBitmap())
            self.bitmap_list[t].SetBitmap(wx.Image(img, wx.BITMAP_TYPE_ANY).ConvertToBitmap())
            print("A picture {} is added to folder {}".format(img, self.folder_id))
        else:
            wx.MessageBox('Max limit reached.\n Only 12 pics can be added per Config Sheet', 'Info', wx.OK | wx.ICON_INFORMATION)
        mysmb.close_connection()
        # event.Skip()

    def on_load(self):
        self.Title = "Config Sheet # " + self.folder_id

    def show_pictures(self):
        self.m_button_take_photo.Hide()
        self.Title = "Config Sheet # " + self.folder_id
        mysmb = smb('RHEL8', '192.168.1.14', 'Anonymous')
        mysmb.connect_with_smb_share()
        img_list = mysmb.get_img_list(self.folder_id)

        l = len(img_list)
        i = 0
        while i < l:
            file1 = mysmb.retrieve_file(img_list[i].filename)
            print(self.bitmap_list[i])
            self.bitmap_list[i].SetBitmap(wx.Image(file1, wx.BITMAP_TYPE_ANY).ConvertToBitmap())
            i += 1

        mysmb.close_connection()
