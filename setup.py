#!/usr/bin/env python

from distutils.core import setup  

data_files = [('share/applications',['pyconfig-accessgnome-ui.desktop']),
    ('share/python-config-accesskey-gnome',['COPYING','configGconf.py','pyconfig-accessgnome.glade','pyconfig-accessgnome-ui.py','README','TODO'])]

setup(name='python-gconf-keybinding',
      version='0.4',
      description='Allow config keyboard access application with gconf',
      author='Ernesto Nadir Crespo Avila', 
      author_email='ecrespo@gmail.com',
      url = 'http://code.google.com/p/python-config-accesskey-gnome/',
      license = "GPL v3",
      scripts = ['pyconfig-accessgnome-ui.py', 'configGconf.py'],
      data_files = [('share/applications',['pyconfig-accessgnome-ui.desktop']), ('share/python-config-accesskey-gnome',['COPYING','configGconf.py','pyconfig-accessgnome.glade','pyconfig-accessgnome-ui.py','README','TODO'])],
      platforms=['i386','AMD64'],
      requires = ['gtk','gconf','pygtk','gtk.glade'],
      py_modules = ['configGconf']
      )




