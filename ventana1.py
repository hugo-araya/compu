from tkinter import * 
def salir():
    print(nombre_str.get())

if __name__ == "__main__":
    root = Tk()
    root.geometry("300x150")
    root.title('Formulario 1')
    nombre_label=Label(root,text="Nombre:")
    nombre_label.grid(row=1,column=1)
    nombre_str = StringVar()
    nombre_entry=Entry(root,textvariable=nombre_str)
    nombre_entry.grid(row=1,column=2)
    last_label=Label(root,text="Apellido: ")
    last_label.grid(row=2,column=1)
    last_str=StringVar()
    last_entry=Entry(root,textvariable=last_str)
    last_entry.grid(row=2,column=2)
    mail_label=Label(root,text="Email: ")
    mail_label.grid(row=3,column=1)
    mail_str=StringVar()
    mail_entry=Entry(root,textvariable=mail_str)
    mail_entry.grid(row=3,column=2)
    finish=Button(root,text="Finalizar", command=salir)
    finish.grid(row=4,column=2)
    root.mainloop()
