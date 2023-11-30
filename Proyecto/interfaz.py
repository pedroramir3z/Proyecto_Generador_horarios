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
            self.tree.column(col, anchor="center", width=100)
            self.tree.heading(col, anchor="center")

        # Agregar el Treeview a la ventana
        self.tree.pack(padx=10, pady=10)

def main():
    # Lista de horarios (reemplaza esto con tu lista de horarios)
    horarios = [
        ('FUNDAMENTOS DE LA PROGRAMACION', 'Claudia Sánchez Rodríguez', 101, 'MARTESxJUEVES-11AM-A-12:55PM'),
        # Agrega más horarios si es necesario
    ]

    # Crear la ventana principal
    root = tk.Tk()
    
    # Crear la instancia de la ventana de horarios
    ventana_horarios = VentanaHorarios(root, horarios)

    # Iniciar el bucle principal
    root.mainloop()

if __name__ == "__main__":
    main()

main();