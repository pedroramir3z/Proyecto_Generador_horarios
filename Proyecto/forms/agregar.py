import tkinter as tk 
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from tkinter import *
from tkinter import ttk

def agrega():
    
    def crear_interfaz():
        
        def guardar_datos():
            curso = entry_curso.get()
            nombre = entry_nombre.get()
            aula= entry_aula.get()
            dia = entry_dia.get()
            hora = entry_hora.get()
            conector=str(dia)+"-"+str(hora)
            info_guardada = [curso, nombre, aula, conector]
            print("Información guardada:", info_guardada)
            label_resultado = tk.Label(root, text=info_guardada)
            label_resultado.pack()
            # Aquí podrías guardar la información en un arreglo o realizar alguna acción con los datos.
        
        root = tk.Tk()
        root.title("AGREGAR PROFESORES")
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()                                    
        root.geometry("%dx%d+0+0" % (w, h))
        root.config(bg='black')
        root.resizable(width=0, height=0)  
        
        label_curso = tk.Label(root, text="Curso actual:", font=('Times', 15,BOLD))
        label_curso.pack()
        global entry_nombre
        entry_curso = tk.Entry(root,width=60, font=('Times', 15,BOLD))
        entry_curso.pack()

        label_nombre = tk.Label(root, text="Nombre:", font=('Times', 15,BOLD))
        label_nombre.pack()
        global entry_nombre
        entry_nombre = tk.Entry(root,width=60, font=('Times', 15,BOLD))
        entry_nombre.pack()
        
        label_aula = tk.Label(root, text="Numero de aula:", font=('Times', 15,BOLD))
        label_aula.pack()
        global entry_aula
        entry_aula = tk.Entry(root,width=60, font=('Times', 15,BOLD))
        entry_aula.pack()

        label_dia = tk.Label(root, text="Rango de dias: (EJ. MARTESxJUEVES)", font=('Times', 15,BOLD))
        label_dia.pack()
        global entry_dia
        entry_dia = tk.Entry(root,width=60, font=('Times', 15,BOLD))
        entry_dia.pack()
        
        label_hora = tk.Label(root, text="Rango de horas: (EJ. 11AM-A-12:55PM)", font=('Times', 15,BOLD))
        label_hora.pack()
        global entry_hora
        entry_hora = tk.Entry(root,width=60, font=('Times', 15,BOLD))
        entry_hora.pack()

        

        # Botón para guardar los datos
        boton_guardar = tk.Button(root, text="Guardar", font=('Times', 15,BOLD), bg='black', bd=0, fg="#fff" ,command=guardar_datos)
        boton_guardar.pack()

        root.mainloop()

    # Ejecutar la función para crear la interfaz
    crear_interfaz()
    
    