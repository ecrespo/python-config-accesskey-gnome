#!/usr/bin/env python

from distutils.core import setup


data_files = [('share/applications',['pyloro.desktop']), ('share/pixmaps',['images/pyloro.png','images/pyloro_icono.png']),
    ('share/pyloro',['pyloro.glade','Festival.py','Convert.py','verifyconfig.py','pyloro.png','ConfigurepyLoro.py','Reproducir.py','pyloro.conf']),
    ('share/sounds', ['audio/iniciando.ogg','audio/terminando.ogg'])
    ]

setup(name='pyloro',
      version='0.4',
      description='A graphic document conversor to audio format',
      author='Ernesto Nadir Crespo Avila', 
      author_email='ecrespo@gmail.com',
      url = 'http://code.google.com/p/pyloro/',
      license = "GPL v3",
      scripts = ['pyloro.py'],
      data_files = data_files,
      platforms=['i386','AMD64'],
      requires = ['ConfigParser','shutil','commands','string','os','pygst','gst','gobject','gtk','sys','pygtk','gtk.glade','inspect'],
      py_modules = ['Festival','Convert','ConfigurepyLoro','Reproducir','verifyconfig']
      )




