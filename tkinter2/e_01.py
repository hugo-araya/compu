from tkinter import *
import tkinter.messagebox

def saludar(e):
	print ("Hola mundo")
	ret = tkinter.messagebox.askyesnocancel("Nombre : ", e.get())
	print (ret)

def main():
	v = Tk()
	v.title("Hola")
	l1 = Label(v,text="Etiqueta 1")
	l1.grid(row = 1, column = 1)
	l2 = Label(v,text="Etiqueta 2")
	l2.grid(row = 1, column = 3)
	v_t = StringVar()
	e1 = Entry(v,textvariable=v_t)
	e1.grid(row = 2, column = 2)
	b1 = Button(v,text = "Salir", command = quit)
	b1.grid(row=3, column = 2)
	b2 = Button(v,text = "Saludar", command = lambda: saludar(e1))
	b2.grid(row=4, column = 2)
	v.mainloop()

if __name__ == '__main__':
	main()