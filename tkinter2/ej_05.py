from tkinter import *
import tkinter.messagebox

def hola(ev):
	print ("Hola "+ ev)

def principal():
    ventana = Tk()
    ventana.title('Botones')
    label1 = Label(ventana,text='Tu Nombre')
    label1.grid(row = 1, column = 1)
    variable_string = StringVar()
    caja = Entry(ventana,textvariable=variable_string) 
    caja.grid(row=1,column=2)
    
    b1 = Button(ventana,text='B 1', command = lambda: hola(caja.get()))
    b1.grid(row = 2, column = 2)
    ventana.mainloop()

if __name__ == "__main__":
    principal()