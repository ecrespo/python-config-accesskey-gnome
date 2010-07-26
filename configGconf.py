#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Name: configGconf
Description: Aplicación y módulo que permite modificar los accesos rápido de teclas a programas
Version:0.3
License: GPLv3
Copyright: Copyright (C) 2009  Distrito Socialista Tecnologico AIT PDVSA Mérida
Author: Ernesto Nadir Crespo Avila
Email: ecrespo@gmail.com
Changelog:
 0.1: * Agregada multiples opciones de configuración.
 0.2: * Agregada opción de selección de distribución debian, ubuntu o canaima.
      * Agregada información adicional a la hora de desplegar en pantalla.
 0.3: * Agregado el uso del módulo argparse para simplificar la captura de argumentos del comando.
"""
__version = "0.3"
__autor = "Ernesto Nadir Crespo Avila"
__email = "ecrespo@gmail.com"
__copyright = "GPLv3"

#Importar módulo gconf
import gconf


class Conf:
    def __init__(self):
        #Se crea la instancia de la clase de gconf
        self.__gconfClient = gconf.client_get_default()
        #Se crea la tupĺa aplicaciones        
        self.__aplicaciones = ("orca", "gnome-terminal","oowriter","iceweasel","nautilus","ooimpress","pidgin","oocalc","gedit","gnome-calculator","rhythmbox")
        #Se crea la ruta del comando del teclado y la ruta del modificador de teclado
        self.__comando = "/apps/metacity/keybinding_commands/command_"
        self.__asignacion_teclado = "/apps/metacity/global_keybindings/run_command_"
        #Se crea un diccionario teclas con la asociación entre la aplicación y su acceso rápido de teclado
        self.__teclas = {"orca":"<Super>o","gnome-terminal":"<Super>t","oowriter":"<Super>w","iceweasel":"<Super>n","nautilus":"<Super>h","ooimpress":"<Super>i","pidgin":"<Super>p","oocalc":"<Super>x","gedit":"<Super>e","gnome-calculator":"<Super>c","rhythmbox":"<Super>m"}

        

        
    def modificar(self,distribucion):
        """
        modificar: Permite modificar los accesos rápidos del teclado
        Argumentos:
         * distribucion: se le pasa una distribución a utilizar entre debian,ubuntu y canaima.
        """
        cont = 1
        print "Listar accesos rapidos del teclado de gconf"
        print "________________________________________________"
        #Se la distribución no es debian se cambia iceweasel por firefox en las variables aplicaciones y teclas.
        if args.distribucion <> "debian":
            self.__aplicaciones = ("orca", "gnome-terminal","oowriter","firefox","nautilus","ooimpress","pidgin","oocalc","gedit","gnome-calculator","rhythmbox")
            self.__teclas = {"orca":"<Super>o","gnome-terminal":"<Super>t","oowriter":"<Super>w","firefox":"<Super>n","nautilus":"<Super>h","ooimpress":"<Super>i","pidgin":"<Super>p","oocalc":"<Super>x","gedit":"<Super>e","gnome-calculator":"<Super>c","rhythmbox":"<Super>m"}
        #Se genera un ciclo según las aplicaciones
        for aplicacion in self.__aplicaciones:
            #Definición de las rutas del gconf del comando y del modificador del teclado
            ruta1 =  "%s%s" %(self.__comando,cont)
            ruta2 = "%s%s"  %(self.__asignacion_teclado,cont)
            #Se modifica gconf
            self.__gconfClient.set_string(ruta1, "%s" %aplicacion)
            self.__gconfClient.set_string(ruta2, "%s" %self.__teclas[aplicacion])
            #Se imprime en pantalla los cambios logrados.
            print "Configurando aplicacion: %s, acceso teclado: %s" %(aplicacion,self.__teclas[aplicacion])
            cont = cont +1
    
    
    def listar(self):
        """
        listar: Permite listar los accesos rápidos de teclado de gconf
        """
        cont = 1
        print "Listar accesos rapidos del teclado a gconf"
        print "________________________________________________"
        #Se crea un ciclo según la lista de aplicaciones
        for aplicacion in self.__aplicaciones:
            #Se define la ruta del comando del teclado según gconf
            ruta1 =  "%s%s" %(self.__comando,cont)
            #Se define la ruta del modificador del teclado
            ruta2 = "%s%s"  %(self.__asignacion_teclado,cont)
            #Se desplega en pantalla 
            print "Aplicación: " ,self.__gconfClient.get_string(ruta1),self.__gconfClient.get_string(ruta2)
            cont = cont +1


if __name__ == "__main__":
    #Importar módulo argparse para capturar los argumentos del comando    
    import argparse
    #Se instancia la clase Conf en el objeto config
    config = Conf()
    #Se define como global a la variable opciones
    global opciones
    #opciones contiene las claves del diccionario teclas
    opciones = config.teclas.keys()    
    #Creación del parse 
    parser = argparse.ArgumentParser(prog='configGconf',description="Cambiar accesos rapidos en teclado a Gnome")
    #Se agrega las opciones accion, distribucion y version.    
    parser.add_argument('-a','--accion',type=str,choices=["cambiar","listar"],default=["cambiar","listar"],help='lista gconf')
    parser.add_argument('-d','--distribucion',choices=["debian","ubuntu","canaima"],type=str,default=["debian","ubuntu","canaima"],help='seleccione entre Canaima,Debian y ubuntu')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.3')
    #Se captura los argumentos del comando ejecutado.
    args = parser.parse_args()
    # ejecución de las opciones según la acción y la distribución
    if args.accion == "listar":
        #Se lista las configuraciones de los accesos del teclado
        config.listar()
    elif args.distribucion in ('debian','ubuntu','canaima') and args.accion == "cambiar":
        #Se modifican las opciones de los accesos del teclado
        config.modificar(args.distribucion)
