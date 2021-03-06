#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kde4
from pisi.actionsapi import pisitools

def setup():
    kde4.configure("-DBUILD_RELEASE:BOOL=ON")

def build():
    kde4.make()

def install():
    kde4.install()

    pisitools.dodoc("AUTHORS", "README", "LICENSE*")
