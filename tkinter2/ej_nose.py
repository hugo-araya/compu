from tkinter import *
import tkinter.messagebox

top = Tk()
top.geometry("200x100")
def hello():
   tkinter.messagebox.showinfo("Digo Hola", "Hola Mundo")

B1 = Button(top, text = "Digo Hola", bg = 'red', command = hello)
B1.place(x = 35,y = 50)

top.mainloop()