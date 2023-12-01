import pandas as pd
from profesor import Profesor
from aula import Aula
from curso import Curso
from planificador_horarios import PlanificadorHorarios

from forms.form_master import MasterPanel

# Definición de horarios 
LM9a11 = "LUNESxMIERCOLES-9AM-A-10:55AM"
LM11a1 = "LUNESxMIERCOLES-11AM-A-12:55PM"
LM1a3 = "LUNESxMIERCOLES-1PM-A-2:55PM"
LM3a5 = "LUNESxMIERCOlES-3PM-A-4:55PM"
MJ9a11 = "MARTESxJUEVES-9AM-A-10:55AM"
MJ11a1 = "MARTESxJUEVES-11AM-A-12:55PM"
MJ1a3 = "MARTESxJUEVES-1PM-A-2:55PM"
MJ3a5 = "MARTESxJUEVES-3PM-A-4:55PM"
V9a1 = "VIERNES-9AM-A-1PM"
V1a5 = "VIERNES-1PM-A-5PM"

#Lee los archivos exel 
profesores_df = pd.read_excel('profesores.xlsx')
aulas_df = pd.read_excel('aulas.xlsx')
cursos_df = pd.read_excel('cursos.xlsx')



profesores = []
for index, row in profesores_df.iterrows():
    if 'cursos ' in profesores_df.columns:
        cursoss = row['cursos '].split(',') if pd.notna(row['cursos ']) else []
        disponibilidad = row['disponibilidad'].split(',') if pd.notna(row['disponibilidad']) else []
        profesor = Profesor(row['id '], row['nombre'], cursoss, disponibilidad)
        profesores.append(profesor)
    else:
        print("Column 'cursos ' no encontrada.")

aulas = []
for index, row in aulas_df.iterrows():
    
    if 'id ' in aulas_df.columns:
        equipamiento = row['equipamiento'].split(',') if pd.notna(row['equipamiento']) else []
        aula = Aula(row['id '], row['capacidad'], equipamiento)
        aulas.append(aula)
    else:
        print("Column 'id ' no encontrada.")

cursos = []
for index, row in cursos_df.iterrows():
    restricciones = row['restricciones'].split(',') if pd.notna(row['restricciones']) else []
    curso = Curso(row['id'], row['nombre'], row['horas_semana'], restricciones)
    cursos.append(curso)




cursosFinales=[]
for curso  in cursos:
    for profe in profesores:
        if curso.nombre in profe.cursos:
            cursosFinales.append(curso)

        
print("Inicio")

#Crear una instancia de PlanificadorHorarios
planificador = PlanificadorHorarios(profesores, aulas, cursosFinales)
# Ejecutar el algoritmo de asignación de horarios
planificador.asignar_horarios()

horarioos=planificador.horarios_asignados

# Mostrar los horarios asignados
for asignacion in planificador.horarios_asignados:
    print(asignacion)



MasterPanel(horarioos)