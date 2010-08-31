#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Name: pyconfig-accessgnome-uy
Description: Aplicación gráfica que permite configurar los accesos rápidos de teclado a gconf
Version:0.3
License: GPLv3
Copyright: Copyright (C) 2009  Ernesto Nadir Crespo Avila <ecrespo@gmail.com>
Author: Ernesto Nadir Crespo Avila
Email: ecrespo@gmail.com
Changelog:
 0.1: * Creado el programa para la interfaz gráfica que permite cambiar las configuración de gconf
 0.2: * Adaptación a la nueva versión de configGconf
 0.3: * Modificado el programa y la interfaz para manejar libglade


"""
licencia = "GPLv3"
autor = "Ernesto Nadir Crespo Avila"
correo = "ecrespo@gmail.com"




#Importando el módulo gtk y configGconf
import gtk,configGconf
import pygtk
pygtk.require('2.0')
import gtk, gtk.glade, inspect, sys


#Creando la clase AccessGnomeConfig
class AccessGnomeConfig:
    #Inicializando la clase con el método constructor
	def __init__(self):
        #Asignando a una variable el nombre del archivo glade
		self.__glade_file = "/usr/local/share/python-config-accesskey-gnome/pyconfig-accessgnome.glade"
        #Creando el objeto de la clase bulder
		self.__w_tree = gtk.glade.XML(self.__glade_file)
		# Asociando los widgets de la interfaz gráfica 
		self.__window = self.__w_tree.get_widget('ventana')
		self.__bsalir = self.__w_tree.get_widget('bsalir')
		self.__baceptar = self.__w_tree.get_widget('baceptar')
		self.__orca = self.__w_tree.get_widget('orca')
		self.__writer = self.__w_tree.get_widget('writer')
		self.__pidgin = self.__w_tree.get_widget('pidgin')
		self.__impress = self.__w_tree.get_widget('impress')
		self.__calc = self.__w_tree.get_widget('calc')
		self.__terminal = self.__w_tree.get_widget('terminal')
		self.__nautilus = self.__w_tree.get_widget('nautilus')
		self.__navegador = self.__w_tree.get_widget('navegador')
		self.__editor = self.__w_tree.get_widget('editor')
		self.__calculadora = self.__w_tree.get_widget('calculadora')
		self.__reproductor = self.__w_tree.get_widget('reproductor')
		self.__todas = self.__w_tree.get_widget('todas')
		self.__distribucion = self.__w_tree.get_widget('distribucion')
        	#Creando una lista vacía
        	self.__aplicaciones = []
		self.__distribuciones = ""
		self.__nav_distro = { "debian":"iceweasel","ubuntu":"firefox","canaima":"firefox"}
		#Se asocia los eventos con las señales
		self.__w_tree.signal_autoconnect(dict(inspect.getmembers(self)))
		
        def on_distribucion_changed(self,*args):
		self.__distribuciones = self.__distribucion.get_active_text()
		if self.__distribuciones == "":
			self.__distribuciones == "debian"
			
    	#Definiendo los métodos de los botones de check creados
    	def on_orca_toggled(self,*args):
		variable = self.__orca.get_active()
		if variable == True:
			self.__aplicaciones.append("orca")
		else:
			self.__eliminacion("orca")
	
	def on_nautilus_toggled(self,*args):
		variable = self.__nautilus.get_active()
		if variable == True:
			self.__aplicaciones.append("nautilus")
		else:
			self.__eliminacion("nautilus")
			
	def on_writer_toggled(self,*args):
		variable = self.__writer.get_active()
		if  variable == True:
			self.__aplicaciones.append("oowriter")
		else:
			self.__eliminacion("oowriter")
	
	def on_navegador_toggled(self,*args):
		variable = self.__navegador.get_active()
		if self.__distribuciones.lower() == "":
			self.__distribuciones = "debian"
		if  variable == True:
			self.__aplicaciones.append(self.__nav_distro[self.__distribuciones.lower()])
		else:
			self.__eliminacion(self.__nav_distro[self.__distribuciones.lower()])
			
	def on_pidgin_toggled(self,*args):
		variable = self.__pidgin.get_active()
		if  variable == True:
			self.__aplicaciones.append("pidgin")
		else:
			self.__eliminacion("pidgin")
	
	def on_editor_toggled(self,*args):
		variable = self.__editor.get_active()
		if  variable == True:
			self.__aplicaciones.append("gedit")
		else:
			self.__eliminacion("gedit")
		
	def on_impress_toggled(self,*args):
		variable = self.__impress.get_active()
		if  variable == True:
			self.__aplicaciones.append("ooimpress")
		else:
			self.__eliminacion("ooimpress")
	
	def on_calculadora_toggled(self,*args):
		variable = self.__calculadora.get_active()
		if  variable == True:
			self.__aplicaciones.append("gnome-calculator")
		else:
			self.__eliminacion("gnome-calculator")
	
	def on_calc_toggled(self,*args):
		variable = self.__calc.get_active()
		if  variable == True:
			self.__aplicaciones.append("oocalc")
		else:
			self.__eliminacion("oocalc")
			
	def on_reproductor_toggled(self,*args):
		variable = self.__reproductor.get_active()
		if  variable == True:
			self.__aplicaciones.append("rhythmbox")
		else:
			self.__eliminacion("rhythmbox")
			
	def on_terminal_toggled(self,*args):
		variable = self.__terminal.get_active()
		if  variable == True:
			self.__aplicaciones.append("gnome-terminal")
		else:
			self.__eliminacion("gnome-terminal")
    	#Método que elimina aplicaciones seleccionadas
	def __eliminacion(self,aplicacion):
		if len(self.__aplicaciones) >= 2:
			for i in range(len(self.__aplicaciones)):
				if self.__aplicaciones[i] == aplicacion:
					self.__aplicaciones[i:i+1] = []
					break
				else:
					continue
		elif len(self.__aplicaciones) == 1:
			if self.__aplicaciones[0] == aplicacion:
				self.__aplicaciones = []
			else:
				pass
		else:
			pass
				
			
	def on_todas_toggled(self,*args):
		variable = self.__todas.get_active()
		if  variable == True:
			self.__orca.set_active(1)
			self.__writer.set_active(1)
			self.__calc.set_active(1)
			self.__impress.set_active(1)
			self.__calculadora.set_active(1)
			self.__reproductor.set_active(1)
			self.__editor.set_active(1)
			self.__navegador.set_active(1)
			self.__nautilus.set_active(1)
			self.__terminal.set_active(1)
			self.__pidgin.set_active(1)
			
		else:
			self.__orca.set_active(0)
			self.__writer.set_active(0)
			self.__impress.set_active(0)
			self.__calc.set_active(0)
			self.__calculadora.set_active(0)
			self.__reproductor.set_active(0)
			self.__editor.set_active(0)
			self.__terminal.set_active(0)
			self.__pidgin.set_active(0)
			self.__navegador.set_active(0)
			self.__nautilus.set_active(0)
			

    	
    	#Método que cierra la aplicación
	def on_ventana_destroy(self,*args):
		gtk.main_quit()
	
    	#Método que cierra la aplicación al darle al botón salir
	def on_bsalir_clicked(self,*args):
		gtk.main_quit()
	
	
    	#Método que ejecuta la configuración de los accesos rápidos
	def on_baceptar_clicked(self,*args):
		Config = configGconf.Conf()
		for aplicacion in self.__aplicaciones:
			Config.modificar_opcion(aplicacion,self.__distribuciones.lower(),1)
			

    
    
	#Método principal de la clase
	def main(self):
		#Se muestra la ventana.
        	self.__window.show()
		gtk.main()
		
		


if __name__ == "__main__":
	app = AccessGnomeConfig()
	app.main()
