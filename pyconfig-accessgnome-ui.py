#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gtk


class AccessGnomeConfig:
	def __init__(self):
		self.glade_file = "ui.glade"
		self.glade = gtk.Builder()
		self.glade.add_from_file(self.glade_file)
		# get widgets
		self.window = self.glade.get_object('dialog1')
		self.button1 = self.glade.get_object('button1')
		self.button2 = self.glade.get_object('button2')
		self.checkbutton1 = self.glade.get_object('checkbutton1')
		self.checkbutton2 = self.glade.get_object('checkbutton2')
		self.checkbutton3 = self.glade.get_object('checkbutton3')
		self.checkbutton4 = self.glade.get_object('checkbutton4')
		self.checkbutton5 = self.glade.get_object('checkbutton5')
		self.checkbutton6 = self.glade.get_object('checkbutton6')
		self.checkbutton7 = self.glade.get_object('checkbutton7')
		self.checkbutton8 = self.glade.get_object('checkbutton8')
		self.checkbutton9 = self.glade.get_object('checkbutton9')
		self.checkbutton10 = self.glade.get_object('checkbutton10')
		self.checkbutton11 = self.glade.get_object('checkbutton11')
		self.checkbutton12 = self.glade.get_object('checkbutton12')
		self.checkbutton13 = self.glade.get_object('checkbutton13')
		self.aplicaciones = []
		
		
		
		# signals
		self.window.connect ("close",self.on_dialog1_close)
		self.window.connect("destroy",self.on_dialog1_destroy)
		self.button1.connect ("clicked",self.on_button1_clicked)
		self.button2.connect ("clicked",self.on_button2_clicked)
		self.checkbutton1.connect("toggled",self.on_checkbutton1_toggled)
		self.checkbutton2.connect("toggled",self.on_checkbutton2_toggled)
		self.checkbutton3.connect("toggled",self.on_checkbutton3_toggled)
		self.checkbutton4.connect("toggled",self.on_checkbutton4_toggled)
		self.checkbutton5.connect("toggled",self.on_checkbutton5_toggled)
		self.checkbutton6.connect("toggled",self.on_checkbutton6_toggled)
		self.checkbutton7.connect("toggled",self.on_checkbutton7_toggled)
		self.checkbutton8.connect("toggled",self.on_checkbutton8_toggled)
		self.checkbutton9.connect("toggled",self.on_checkbutton9_toggled)
		self.checkbutton10.connect("toggled",self.on_checkbutton10_toggled)
		self.checkbutton11.connect("toggled",self.on_checkbutton11_toggled)
		self.checkbutton12.connect("toggled",self.on_checkbutton12_toggled)
		self.checkbutton13.connect("toggled",self.on_checkbutton13_toggled)
		#Config widgets
		self.window.set_title("Configuración de accesos rapidos de Aplicaciones en Gnome")
		self.window.show_all()
	
	def on_checkbutton1_toggled(self,*args):
		variable = self.checkbutton1.get_active()
		if variable == True:
			self.aplicaciones.append("orca")
		else:
			self.__eliminacion("orca")
	
	def on_checkbutton2_toggled(self,*args):
		variable = self.checkbutton2.get_active()
		if variable == True:
			self.aplicaciones.append("nautilus")
		else:
			self.__eliminacion("nautilus")
			
	def on_checkbutton3_toggled(self,*args):
		variable = self.checkbutton3.get_active()
		if  variable == True:
			self.aplicaciones.append("oowriter")
		else:
			self.__eliminacion("oowriter")
	
	def on_checkbutton4_toggled(self,*args):
		variable = self.checkbutton4.get_active()
		if  variable == True:
			self.aplicaciones.append("iceweasel")
		else:
			self.__eliminacion("iceweasel")
			
	def on_checkbutton5_toggled(self,*args):
		variable = self.checkbutton5.get_active()
		if  variable == True:
			self.aplicaciones.append("pidgin")
		else:
			self.__eliminacion("pidgin")
	
	def on_checkbutton6_toggled(self,*args):
		variable = self.checkbutton6.get_active()
		if  variable == True:
			self.aplicaciones.append("gedit")
		else:
			self.__eliminacion("gedit")
		
	def on_checkbutton7_toggled(self,*args):
		variable = self.checkbutton7.get_active()
		if  variable == True:
			self.aplicaciones.append("ooimpress")
		else:
			self.__eliminacion("ooimpress")
	
	def on_checkbutton8_toggled(self,*args):
		variable = self.checkbutton8.get_active()
		if  variable == True:
			self.aplicaciones.append("gnome-calculator")
		else:
			self.__eliminacion("gnome-calculator")
	
	def on_checkbutton9_toggled(self,*args):
		variable = self.checkbutton9.get_active()
		if  variable == True:
			self.aplicaciones.append("oocalc")
		else:
			self.__eliminacion("oocalc")
			
	def on_checkbutton10_toggled(self,*args):
		variable = self.checkbutton10.get_active()
		if  variable == True:
			self.aplicaciones.append("rhythmbox")
		else:
			self.__eliminacion("rhythmbox")
			
	def on_checkbutton11_toggled(self,*args):
		variable = self.checkbutton11.get_active()
		if  variable == True:
			self.aplicaciones.append("gnome-terminal")
		else:
			self.__eliminacion("gnome-terminal")
			
	def on_checkbutton12_toggled(self,*args):
		pass
		"""
		variable = self.checkbutton12.get_active()
		if  variable == True:
			print "daltonicos"
		else:
			print "nada de daltonicos"
		"""
	def __eliminacion(self,aplicacion):
		if len(self.aplicaciones) >= 2:
			for i in range(len(self.aplicaciones)):
				print i, self.aplicaciones[i], self.aplicaciones
				if self.aplicaciones[i] == aplicacion:
					self.aplicaciones[i:i+1] = []
				else:
					continue
		elif len(self.aplicaciones) == 1:
			if self.aplicaciones[0] == aplicacion:
				self.aplicaciones = []
			else:
				pass
		else:
			pass
				
			
	def on_checkbutton13_toggled(self,*args):
		variable = self.checkbutton13.get_active()
		if  variable == True:
			self.checkbutton1.set_active(1)
			self.checkbutton2.set_active(1)
			self.checkbutton3.set_active(1)
			self.checkbutton4.set_active(1)
			self.checkbutton5.set_active(1)
			self.checkbutton6.set_active(1)
			self.checkbutton7.set_active(1)
			self.checkbutton8.set_active(1)
			self.checkbutton9.set_active(1)
			self.checkbutton10.set_active(1)
			self.checkbutton11.set_active(1)
			#self.checkbutton12.set_active(1)
		else:
			self.checkbutton1.set_active(0)
			self.checkbutton2.set_active(0)
			self.checkbutton3.set_active(0)
			self.checkbutton4.set_active(0)
			self.checkbutton5.set_active(0)
			self.checkbutton6.set_active(0)
			self.checkbutton7.set_active(0)
			self.checkbutton8.set_active(0)
			self.checkbutton9.set_active(0)
			self.checkbutton10.set_active(0)
			self.checkbutton11.set_active(0)
			#self.checkbutton12.set_active(0)

		
	def on_dialog1_close(self,*args):
		gtk.main_quit()
	
	def on_dialog1_destroy(self,*args):
		gtk.main_quit()
	
	def on_button1_clicked(self,*args):
		gtk.main_quit()
	
	def on_button2_clicked(self,*args):
		print self.aplicaciones
	
	def main(self):
		gtk.main()
		
		


if __name__ == "__main__":
	app = AccessGnomeConfig()
	app.main()
