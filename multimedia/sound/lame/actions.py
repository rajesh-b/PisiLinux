#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

# WorkDir = "lame-398-2"

def setup():
    shelltools.export("AT_M4DIR", get.curDIR())
    #libtools.libtoolize("--copy --force")
    #autotools.autoreconf("-fi")

    shelltools.makedirs("libmp3lame/i386/.libs")
    autotools.configure("--disable-mp3x \
                         --disable-static \
                         --enable-shared \
                         --disable-mp3rtp \
                         --enable-nasm")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s" pkghtmldir="/%s/%s/html"' % (get.installDIR(), get.docDIR(), get.srcNAME()))

    pisitools.dodoc("API", "ChangeLog", "HACKING", "README*", "STYLEGUIDE", "TODO", "USAGE")
    pisitools.dohtml("misc/*", "Dll/*")
    pisitools.dobin("misc/mlame")
