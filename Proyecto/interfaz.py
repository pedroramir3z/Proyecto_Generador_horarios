

import tkinter as tk
from tkinter import ttk

class VentanaHorarios:
    def __init__(self, root, horarios):
        self.root = root
        self.root.title("Horarios")

        # Crear un Treeview para mostrar los horarios
        self.tree = ttk.Treeview(root, columns=("Curso", "Profesor", "Aula", "Horario"), show="headings")
        self.tree.heading("Curso", text="Curso")
        self.tree.heading("Profesor", text="Profesor")
        self.tree.heading("Aula", text="Aula")
        self.tree.heading("Horario", text="Horario")
        
        # Insertar los horarios en el Treeview
        for horario in horarios:
            self.tree.insert("", "end", values=horario)

        # Ajustar las columnas para que se ajusten al contenido
        for col in ("Curso", "Profesor", "Aula", "Horario"):
            # Obtener la longitud máxima de los elementos en la columna
            max_width = max([len(str(self.tree.item(item, 'values')[self.tree['columns'].index(col)])) for item in self.tree.get_children()])
            
            # Establecer el ancho de la columna
            self.tree.column(col, width=max_width * 10)  # Puedes ajustar el factor multiplicador según tus necesidades

        # Agregar el Treeview a la ventana
        self.tree.pack(padx=10, pady=10)

def interfaz(horarios=[]):
    # Lista de horarios (reemplaza esto con tu lista de horarios)

    # Crear la ventana principal
    root = tk.Tk()
    
    # Crear la instancia de la ventana de horarios
    ventana_horarios = VentanaHorarios(root, horarios)

    # Iniciar el bucle principal
    root.mainloop()

