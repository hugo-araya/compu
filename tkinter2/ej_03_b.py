from tkinter import *
import tkinter.messagebox 

def saludo():
	print ("Hola mundo")

def principal():
    ventana = Tk()
    ventana.title('titulo de mi ventana')
    et1 = Label(ventana, text = "Wena los cauros")
    et1.grid(row = 1, column = 0)
    et2 = Label(ventana, text = "Hablen bien c....")
    et2.grid(row = 1, column = 2)
    et3 = Label(ventana, text = "ya poooo")
    et3.grid(row = 2, column = 1)
    bt1 = Button(ventana, text = "Saludo", command = saludo)
    bt1.grid(row = 3, column = 1)
    bt2 = Button(ventana, text = "Salir", command = quit)
    bt2.grid(row = 4, column = 1)

    ventana.mainloop()

if __name__ == "__main__":
    principal()