# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# Copyright (C) 2013 Rahul.ES rahul.es@ovi.com
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU General Public License version 3, as published 
# by the Free Software Foundation.
# 
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranties of 
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR 
# PURPOSE.  See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along 
# with this program.  If not, see <http://www.gnu.org/licenses/>.
### END LICENSE

import gettext
from gettext import gettext as _
gettext.textdomain('whoisit')

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('whoisit')

from whoisit_lib import Window
from whoisit.AboutWhoisitDialog import AboutWhoisitDialog
from whoisit.NetQuery import *
import pyperclip
from threading import Thread
from Tkinter import Tk
# See whoisit_lib.Window.py for more details about how this class works
class WhoisitWindow(Window):
    __gtype_name__ = "WhoisitWindow"
    details=None
    url=None
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(WhoisitWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutWhoisitDialog
        
        # Code for other initialization actions should be added here.


    def get_server_details(self):
        if self.url != None:
            who = NetQuery()
            self.details = who.get_details(self.url)    
        
        

    def update_server_details(self):
        
        #set status as error if we didnt receive anything
        if self.details==None:
            self.ui.statuslabel.set_text('Error!')
        ##otherwise, get the values and display them in the textview
        else:
            for key,value in self.details.__dict__.items():

                key_text = key.capitalize()
                key_name = key_text.replace('_',' ') + "  : "
                self.ui.detailsview.get_buffer().insert(
                                                    self.ui.detailsview.get_buffer().get_end_iter(),
                                                    str(key_name))

                if isinstance(value,set):
                    for item in value:
                        itemname = str(item)
                        self.ui.detailsview.get_buffer().insert(
                                                        self.ui.detailsview.get_buffer().get_end_iter(),
                                                        str(itemname)+"  ")

                else:
                        self.ui.detailsview.get_buffer().insert(
                                                        self.ui.detailsview.get_buffer().get_end_iter(),
                                                        str(value)+"\n\r")
            self.ui.detailsview.get_buffer().insert(
                                                    self.ui.detailsview.get_buffer().get_end_iter(),
                                            "\n\r"+("___"*20)+"\n\r")


    def on_executebutton_clicked(self,widget,data=None):
        """Get and display the server details"""
        #Set the status text for the statusbar label.
        self.ui.statuslabel.set_text('Working...')
        url = self.ui.urlentry.get_text()
        self.url=url
        #query the details by using the NetQuery class which returns details
        x=Thread(target=self.get_server_details)
        x.start()
        x.join()
        self.update_server_details()

        #set the status text to done.
        self.ui.statuslabel.set_text('Done!')


    def on_clearbutton_clicked(self,widget,data=None):
        """Clear the text view"""
        self.ui.detailsview.get_buffer().set_text("")

    def on_clipboardbutton_clicked(self,widget,data=None):

        buf = self.ui.detailsview.get_buffer()
        start = buf.get_start_iter()
        end = buf.get_end_iter()
        pyperclip.copy(buf.get_text(start,end,True))
        spam=pyperclip.paste()
