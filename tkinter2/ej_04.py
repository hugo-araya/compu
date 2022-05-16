from tkinter import *
import tkinter.messagebox

def saludo():
    print ("Hola mundo .....")
    tkinter.messagebox.showinfo("saludo", "Hola Mundo ...")

def principal():
    ventana = Tk()
    ventana.title('Labels')
    label1 = Label(ventana,text='Primer Label')
    label1.grid(row = 1, column = 1)
    boton1 = Button(ventana,text='Saludar', command = saludo)
    boton1.grid(row = 1, column = 2)
    ventana.mainloop()

if __name__ == "__main__":
    principal()