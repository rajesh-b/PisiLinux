#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    pisitools.dosed("config.make.in", "^elispdir = .*$", "elispdir = $(datadir)/emacs/site-lisp/lilypond")

    autotools.configure("--with-ncsb-dir=/usr/share/fonts/default/ghostscript")

def build():
    shelltools.export("LC_ALL", "C")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s vimdir=/usr/share/vim/vimfiles" % get.installDIR())

    pisitools.dodoc("COPYING", "NEWS.txt", "README.txt", "THANKS", "VERSION", "ROADMAP")
