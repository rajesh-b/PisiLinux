#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--with-gtk \
			 --with-pic \
			 --with-qt \
			 --enable-pch \
			 --disable-rpath \
			 --enable-theora \
			 --enable-cairo \
			 --without-arts \
			 --with-lua")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR=%s' % get.installDIR())
