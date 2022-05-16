from tkinter import *
import tkinter.messagebox

def saludar():
    print ("Hola mundo")
    tkinter.messagebox.showerror("Titulo", "Hola Mundo Grafico")

def principal():
    ventana = Tk()
    ventana.title('Captura y funcion')
    b1 = Button(ventana, text = "Saludar", command = saludar)
    b1.pack()
    ventana.mainloop()

if __name__ == "__main__":
    principal()
