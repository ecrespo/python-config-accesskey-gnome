#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Name: pyconfig-accessgnome-uy
Description: Aplicación gráfica que permite configurar los accesos rápidos de teclado a gconf
Version:0.2
License: GPLv3
Copyright: Copyright (C) 2009  Distrito Socialista Tecnologico AIT PDVSA Mérida
Author: Ernesto Nadir Crespo Avila
Email: ecrespo@gmail.com
Changelog:
 0.1: * Creado el programa para la interfaz gráfica que permite cambiar las configuración de gconf
 0.2: * Adaptación a la nueva versión de configGconf


"""
__licencia = "GPLv3"
__autor = "Ernesto Nadir Crespo Avila"
__correo = "ecrespo@gmail.com"





import gtk,configGconf



class AccessGnomeConfig:
	def __init__(self):
		self.__glade_file = "pyconfig-accessgnome"
		self.__glade = gtk.Builder()
		self.__glade.add_from_file(self.__glade_file)
		# get widgets
		self.__window = self.__glade.get_object('dialog1')
		self.__button1 = self.__glade.get_object('button1')
		self.__button2 = self.__glade.get_object('button2')
		self.__checkbutton1 = self.__glade.get_object('checkbutton1')
		self.__checkbutton2 = self.__glade.get_object('checkbutton2')
		self.__checkbutton3 = self.__glade.get_object('checkbutton3')
		self.__checkbutton4 = self.__glade.get_object('checkbutton4')
		self.__checkbutton5 = self.__glade.get_object('checkbutton5')
		self.__checkbutton6 = self.__glade.get_object('checkbutton6')
		self.__checkbutton7 = self.__glade.get_object('checkbutton7')
		self.__checkbutton8 = self.__glade.get_object('checkbutton8')
		self.__checkbutton9 = self.__glade.get_object('checkbutton9')
		self.__checkbutton10 = self.__glade.get_object('checkbutton10')
		self.__checkbutton11 = self.__glade.get_object('checkbutton11')
		#self.__checkbutton12 = self.__glade.get_object('checkbutton12')
		self.__checkbutton13 = self.__glade.get_object('checkbutton13')
		self.__aplicaciones = []
        	
		# signals
		self.__window.connect ("close",self.on_dialog1_close)
		self.__window.connect("destroy",self.on_dialog1_destroy)
		self.__button1.connect ("clicked",self.on_button1_clicked)
		self.__button2.connect ("clicked",self.on_button2_clicked)
		self.__checkbutton1.connect("toggled",self.on_checkbutton1_toggled)
		self.__checkbutton2.connect("toggled",self.on_checkbutton2_toggled)
		self.__checkbutton3.connect("toggled",self.on_checkbutton3_toggled)
		self.__checkbutton4.connect("toggled",self.on_checkbutton4_toggled)
		self.__checkbutton5.connect("toggled",self.on_checkbutton5_toggled)
		self.__checkbutton6.connect("toggled",self.on_checkbutton6_toggled)
		self.__checkbutton7.connect("toggled",self.on_checkbutton7_toggled)
		self.__checkbutton8.connect("toggled",self.on_checkbutton8_toggled)
		self.__checkbutton9.connect("toggled",self.on_checkbutton9_toggled)
		self.__checkbutton10.connect("toggled",self.on_checkbutton10_toggled)
		self.__checkbutton11.connect("toggled",self.on_checkbutton11_toggled)
		#self.__checkbutton12.connect("toggled",self.on_checkbutton12_toggled)
		self.__checkbutton13.connect("toggled",self.on_checkbutton13_toggled)
		#Config widgets
		self.__window.set_title("Configuración de accesos rapidos de Aplicaciones en Gnome")
		self.__window.show_all()
			
	def on_checkbutton1_toggled(self,*args):
		variable = self.__checkbutton1.get_active()
		if variable == True:
			self.__aplicaciones.append("orca")
		else:
			self.__eliminacion("orca")
	
	def on_checkbutton2_toggled(self,*args):
		variable = self.__checkbutton2.get_active()
		if variable == True:
			self.__aplicaciones.append("nautilus")
		else:
			self.__eliminacion("nautilus")
			
	def on_checkbutton3_toggled(self,*args):
		variable = self.__checkbutton3.get_active()
		if  variable == True:
			self.__aplicaciones.append("oowriter")
		else:
			self.__eliminacion("oowriter")
	
	def on_checkbutton4_toggled(self,*args):
		variable = self.__checkbutton4.get_active()
		if  variable == True:
			self.__aplicaciones.append("iceweasel")
		else:
			self.__eliminacion("iceweasel")
			
	def on_checkbutton5_toggled(self,*args):
		variable = self.__checkbutton5.get_active()
		if  variable == True:
			self.__aplicaciones.append("pidgin")
		else:
			self.__eliminacion("pidgin")
	
	def on_checkbutton6_toggled(self,*args):
		variable = self.__checkbutton6.get_active()
		if  variable == True:
			self.__aplicaciones.append("gedit")
		else:
			self.__eliminacion("gedit")
		
	def on_checkbutton7_toggled(self,*args):
		variable = self.__checkbutton7.get_active()
		if  variable == True:
			self.__aplicaciones.append("ooimpress")
		else:
			self.__eliminacion("ooimpress")
	
	def on_checkbutton8_toggled(self,*args):
		variable = self.__checkbutton8.get_active()
		if  variable == True:
			self.__aplicaciones.append("gnome-calculator")
		else:
			self.__eliminacion("gnome-calculator")
	
	def on_checkbutton9_toggled(self,*args):
		variable = self.__checkbutton9.get_active()
		if  variable == True:
			self.__aplicaciones.append("oocalc")
		else:
			self.__eliminacion("oocalc")
			
	def on_checkbutton10_toggled(self,*args):
		variable = self.__checkbutton10.get_active()
		if  variable == True:
			self.__aplicaciones.append("rhythmbox")
		else:
			self.__eliminacion("rhythmbox")
			
	def on_checkbutton11_toggled(self,*args):
		variable = self.__checkbutton11.get_active()
		if  variable == True:
			self.__aplicaciones.append("gnome-terminal")
		else:
			self.__eliminacion("gnome-terminal")
			
	"""def on_checkbutton12_toggled(self,*args):
    
		
		variable = self.__checkbutton12.get_active()
		if  variable == True:
			print "daltonicos"
		else:
			print "nada de daltonicos"
		
    """
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
				
			
	def on_checkbutton13_toggled(self,*args):
		variable = self.__checkbutton13.get_active()
		if  variable == True:
			self.__checkbutton1.set_active(1)
			self.__checkbutton2.set_active(1)
			self.__checkbutton3.set_active(1)
			self.__checkbutton4.set_active(1)
			self.__checkbutton5.set_active(1)
			self.__checkbutton6.set_active(1)
			self.__checkbutton7.set_active(1)
			self.__checkbutton8.set_active(1)
			self.__checkbutton9.set_active(1)
			self.__checkbutton10.set_active(1)
			self.__checkbutton11.set_active(1)
			#self.__checkbutton12.set_active(1)
		else:
			self.__checkbutton1.set_active(0)
			self.__checkbutton2.set_active(0)
			self.__checkbutton3.set_active(0)
			self.__checkbutton4.set_active(0)
			self.__checkbutton5.set_active(0)
			self.__checkbutton6.set_active(0)
			self.__checkbutton7.set_active(0)
			self.__checkbutton8.set_active(0)
			self.__checkbutton9.set_active(0)
			self.__checkbutton10.set_active(0)
			self.__checkbutton11.set_active(0)
			#self.__checkbutton12.set_active(0)

		
	def on_dialog1_close(self,*args):
		gtk.main_quit()
	
	def on_dialog1_destroy(self,*args):
		gtk.main_quit()
	
	def on_button1_clicked(self,*args):
		gtk.main_quit()
	
	def on_button2_clicked(self,*args):
		Config = configGconf.Conf()
		for aplicacion in self.__aplicaciones:
			Config.modificar_opcion(aplicacion,1)

    
    
	
	def main(self):
		gtk.main()
		
		


if __name__ == "__main__":
	app = AccessGnomeConfig()
	app.main()
