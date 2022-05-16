from tkinter import *
from tkinter import messagebox
def salir():
    print(variable_string.get())
    variable_1.set(variable_1.get()+variable_string.get())
    messagebox.showinfo(message="Mensaje", title="Título")


if __name__ == "__main__":
    ventana=Tk()
    ventana.title('Usando Entry')
    ventana.geometry("400x200")
    label1=Label(ventana,text="Usuario: ")
    label1.grid(row=1,column=1)
    boton = Button(ventana, text = "Aceptar", command = salir)
    variable_string = StringVar()
    caja = Entry(ventana,textvariable=variable_string)
    caja.grid(row=1,column=2)
    boton.grid(row=1,column=3)
    variable_1 = StringVar()
    caja1 = Entry(ventana,textvariable=variable_1)
    caja1.grid(row=2,column=2) 
    ventana.mainloop()
