from tkinter import * 

def hello():
   sal_1.set("Salida 1")
   sal_2.set("Salida 2")

if __name__ == "__main__":
	ventana = Tk()
	ventana.title("Analisis de correos")
	#tkMessageBox.showinfo("Inicio ", "Fin")
	label1=Label(ventana,text="Nombre Archivo de Correos:")
	label1.pack()
	variable_string = StringVar()
	caja = Entry(ventana,textvariable=variable_string)
	caja.pack()
	boton1 = Button(ventana,text="Procesar", command = hello)
	boton1.pack()
	sal_1 = StringVar()
	salida_1 = Entry(ventana,textvariable=sal_1)
	salida_1.pack()
	sal_2 = StringVar()
	salida_2 = Entry(ventana,textvariable=sal_2)
	salida_2.pack()
	salida = Button(ventana,text="Salir", command = quit)
	salida.pack()
	ventana.mainloop()