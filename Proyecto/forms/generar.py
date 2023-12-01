import tkinter as tk 

def genera(mi_matriz=[]):
    
    def crear_tabla(matriz):
        root = tk.Tk()
        root.title("GENERAR HORARIO")
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()                                    
        root.geometry("%dx%d+0+0" % (w, h))
        root.config(bg='black')
        root.resizable(width=0, height=0)  

        num_filas = len(matriz)
        num_columnas = len(matriz[0])

        # Nombres de columnas
        nombres_columnas = ["Materia", "Profesor", "Aula", "Horario"]

        # Crear el marco para la tabla
        frame = tk.Frame(root)
        frame.pack()

        # Crear etiquetas para las columnas
        for j in range(num_columnas):
            label = tk.Label(frame, text=nombres_columnas[j], relief=tk.RIDGE, width=30)
            label.grid(row=0, column=j)

        # Agregar datos a la tabla
        for i in range(num_filas):
            for j in range(num_columnas):
                label = tk.Label(frame, text=str(matriz[i][j]), relief=tk.RIDGE, width=30)
                label.grid(row=i+1, column=j)

        root.mainloop()

    # Ejemplo de matriz
    crear_tabla(mi_matriz)

