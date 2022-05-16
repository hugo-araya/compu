from tkinter import *
import tkinter.messagebox 

def hola(caja):
	print ("Hola "+caja.get())

def principal():
    ventana = Tk()
    ventana.title('Entrada')
    label1 = Label(ventana,text='Tu Nombre')
    label1.grid(row = 1, column = 1)
    variable_string = StringVar()
    caja = Entry(ventana,textvariable=variable_string) 
    caja.grid(row=1,column=2)
    boton = Button(ventana, text = 'Saludo', command=hola(caja))
    boton.grid(row = 2, column = 2)
    ventana.mainloop()

if __name__ == "__main__":
    principal()