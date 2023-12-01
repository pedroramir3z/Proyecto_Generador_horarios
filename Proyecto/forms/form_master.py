import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl
from tkinter import *
from tkinter import ttk
from forms.generar import genera
from forms.agregar import agrega

class MasterPanel:

    def botonGenerar(self):
        genera(self.lista)
    
    def botonAgregar(self):
        agrega()
                                      
    def __init__(self, lista):   
        self.lista = lista
        self.ventana = tk.Tk()                             
        self.ventana.title('Master panel')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)            
        
        logo =utl.leer_imagen("./imagenes/logo.png", (250, 350))

        #frame_logo
        frame_logo=tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10,pady=10,bg='black')
        frame_logo.pack(side="left",expand=tk.NO,fill=tk.BOTH)
        label=tk.Label( frame_logo, image=logo,bg='black')
        label.place(x=0,y=0,relwidth=1, relheight=1)
        
        
        #frame_form
        frame_form=tk.Frame(self.ventana,bd=0,relief=tk.SOLID,bg='#fcfcfc')
        frame_form.pack(side="right",expand=tk.YES,fill=tk.BOTH)
        
        #frame_form_top
        frame_form_top=tk.Frame(frame_form,height=50,bd=0,relief=tk.SOLID,bg='black')
        frame_form_top.pack(side="top",fill=tk.X)
        title = tk.Label(frame_form_top, text="HORARIO PROFESORES",font=('Times',30),fg="#666a88",bg='#fcfcfc',pady=50)
        title.pack(expand=tk.YES,fill=tk.BOTH)
        
        
        #botones
        
        inicio = tk.Button(frame_form, text="Generar", font=('Times', 15,BOLD), bg='black', bd=0, fg="#fff",command=self.botonGenerar)
        inicio.pack(fill=tk.X, padx=20, pady=20)
        inicio.bind("<Return>",(lambda event: self.botonGenerar()))
        
        """
        #tabla
        tabla = ttk.Treeview(frame_form,columns=2)
        tabla.insert("",END,text="Principe",values=("10"))
        tabla.pack(expand=tk.YES,fill=tk.BOTH)
        tabla.heading("#0",text="Nombre",anchor=CENTER)
        tabla.heading("#1",text="Precio",anchor=CENTER)
        """
        
        self.ventana.mainloop()