from tkinter import *
import tkinter.messagebox

def saludar(caja):
    print ("Hola mundo")
    tkinter.messagebox.showinfo("Saludo", "Hola "+caja.get())

def principal():
    ventana = Tk()
    ventana.title('Captura y funcion')
    label1 = Label(ventana,text='Tu Nombre')
    label1.grid(row = 1, column = 1)
    variable_string = StringVar()
    caja = Entry(ventana,textvariable=variable_string) 
    caja.grid(row=1,column=2)
    b1 = Button(ventana, text = "Salir", command = quit)
    b1.grid(row=2,column=1)
    b2 = Button(ventana, text = "Saludar", command = lambda: saludar(caja))
    b2.grid(row=2,column=2)
    ventana.mainloop()

if __name__ == "__main__":
    principal()
