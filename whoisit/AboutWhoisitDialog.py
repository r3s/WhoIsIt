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

import logging
logger = logging.getLogger('whoisit')

from whoisit_lib.AboutDialog import AboutDialog

# See whoisit_lib.AboutDialog.py for more details about how this class works.
class AboutWhoisitDialog(AboutDialog):
    __gtype_name__ = "AboutWhoisitDialog"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the about dialog"""
        super(AboutWhoisitDialog, self).finish_initializing(builder)

        # Code for other initialization actions should be added here.

