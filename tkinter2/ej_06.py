from tkinter import *
import tkinter.messagebox

def principal():
	ventana=Tk()
	ventana.title('Usando Entry')
	variable_string = StringVar()
	caja = Entry(ventana,textvariable=variable_string) 
	caja.grid(row=1,column=1)
	ventana.mainloop()

if __name__ == "__main__":
	principal()