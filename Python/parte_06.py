import os
from tkinter import *
import tkinter.messagebox


def lee_correos(nombre):
	correos = []
	archivo = open(nombre)
	lineas = archivo.readlines()
	for linea in lineas:
		if linea[-1] == "\n":
			# linea = linea.rstrip("\n")
			linea = linea[:-1]
		correos.append(linea)
	archivo.close()
	return correos

def elimina_repetidos(dominios):
	nueva = []
	for elemento in dominios:
		if not elemento in nueva:
			nueva.append(elemento)
	return nueva

def elimina_genericos(dominios):
	genericos = ['com', 'gov' ,'edu' ,'org' ,'net' ,'mil']
	dominios_sin_repetidos = []
	for dominio in dominios:
		tld = dominio[len(dominio)-3:]
		if not tld in genericos:
			dominios_sin_repetidos.append(dominio)
	return dominios_sin_repetidos

def todos_los_dominios(correos):
	dominios = []
	for correo in correos:
		posicion = correo.rfind("@")
		dominios.append(correo[posicion+1:])	
	return dominios

def obtener_dominios(correos):
	dominios = todos_los_dominios(correos)
	dominios = elimina_repetidos(dominios)
	# dominios = list(set(dominios))
	dominios = elimina_genericos(dominios)
	dominios.sort()
	return dominios

def contar_tld(correos):
	dominios = todos_los_dominios(correos)
	dominios = elimina_genericos(dominios)
	tlds = []
	lista_tld = []
	for dominio in dominios:
		tld = dominio[len(dominio)-2:]
		tlds.append(tld)
	tlds_a_contar = list(set(tlds))
	for t in tlds_a_contar:
		contar = tlds.count(t)
		lista_tld.append([t, contar])
	return lista_tld

def salida(dominios_sin_repetidos, tlds):
	os.system("clear")
	print ("Analisis del listado de correos de INDUSTRIALES S.A.")
	print ("----------------------------------------------------")
	print ()
	print ("Listado de Dominios sin Repeticion:\n")
	print (dominios_sin_repetidos)
	print ()
	print ("Ubicaciones de los correos y su conteo:\n")
	print (tlds)	
	print ()
	print ("Tansmision finalizada\n")

def procesar():
	# print "Estoy procesando ....."
	tkinter.messagebox.showinfo("Estoy en ", "procesar")
	nombre = caja.get()
	correos = lee_correos(nombre)
	dominios_sin_repetidos = obtener_dominios(correos)
	tlds = contar_tld(correos)
	sal_1.set(dominios_sin_repetidos)
	sal_2.set(tlds)
	#salida(dominios_sin_repetidos, tlds)

if __name__ == "__main__":
	ventana = Tk()
	ventana.title("Analisis de correos")
	label1=Label(ventana,text="Nombre Archivo de Correos:")
	label1.pack()
	variable_string = StringVar()
	caja = Entry(ventana,textvariable=variable_string)
	caja.pack()
	boton1 = Button(ventana,text="Procesar", command = procesar)
	boton1.pack()
	sal_1 = StringVar()
	salida_1 = Entry(ventana,textvariable=sal_1)
	salida_1.pack()
	sal_2 = StringVar()
	salida_2 = Entry(ventana,textvariable=sal_2)
	salida_2.pack()
	salir = Button(ventana,text="Salir", command = quit)
	salir.pack()
	ventana.mainloop()

