from tkinter import *
from tkinter import ttk

class Aplicacion():
    ventana = 0    
    posx_y = 0
        
    def __init__(self):
        self.raiz = Tk()
        self.raiz.geometry('300x200+500+50')
        self.raiz.resizable(0,0)
        self.raiz.title("Ventana de aplicación")
        boton = ttk.Button(self.raiz, text='Abrir', command=self.abrir)
        boton.pack(side=BOTTOM, padx=20, pady=20)
        self.raiz.mainloop()

    def abrir(self):
        self.dialogo = Toplevel()
        Aplicacion.ventana+=1
        Aplicacion.posx_y += 50
        tamypos = '200x100+'+str(Aplicacion.posx_y)+'+'+ str(Aplicacion.posx_y)
        self.dialogo.geometry(tamypos)
        self.dialogo.resizable(0,0)
        ident = self.dialogo.winfo_id()
        titulo = str(Aplicacion.ventana)+": "+str(ident)
        self.dialogo.title(titulo)        
        boton = ttk.Button(self.dialogo, text='Cerrar', command=self.dialogo.destroy)   
        boton.pack(side=BOTTOM, padx=20, pady=20)
        self.raiz.wait_window(self.dialogo)
    
def main():
    mi_app = Aplicacion()
    return(0)

if __name__ == '__main__':
    main()