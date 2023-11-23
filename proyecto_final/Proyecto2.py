import copy
import pandas as pd

# Cargar los datos desde archivos Excel
profesores_df = pd.read_excel('profesores.xlsx')
aulas_df = pd.read_excel('aulas.xlsx')
cursos_df = pd.read_excel('cursos.xlsx')

# Crear instancias de Profesor
profesores = []
for index, row in profesores_df.iterrows():
    cursos = row['cursos'].split(',') if pd.notna(row['cursos']) else []
    disponibilidad = row['disponibilidad'].split(',') if pd.notna(row['disponibilidad']) else []
    profesor = Profesor(row['id'], row['nombre'], cursos, disponibilidad)
    profesores.append(profesor)

# Crear instancias de Aula
aulas = []
for index, row in aulas_df.iterrows():
    equipamiento = row['equipamiento'].split(',') if pd.notna(row['equipamiento']) else []
    aula = Aula(row['id'], row['capacidad'], equipamiento)
    aulas.append(aula)

# Crear instancias de Curso
cursos = []
for index, row in cursos_df.iterrows():
    restricciones = row['restricciones'].split(',') if pd.notna(row['restricciones']) else []
    curso = Curso(row['id'], row['nombre'], row['horas_semana'], restricciones)
    cursos.append(curso)


LM9a11 = "LUNESxMIERCOELES-9AM-A-10:55AM"
LM11a1 = "LUNESxMIERCOELES-11-A-12:55PM"
LM1a3 = "LUNESxMIERCOELES-1-A-2:55PM"
LM3a5 = "LUNESxMIERCOELES-3-A-4:55PM"
MJ9a11 = "MARTESxJUEVES-9AM-A-10:55AM"
MJ11a1 = "MARTESxJUEVES-11-A-12:55PM"
MJ1a3 = "MARTESxJUEVES-1-A-2:55PM"
MJ3a5 = "MARTESxJUEVES-3-A-4:55PM"
V9a11 = "VIERNES-9-A-1"
V1a5 = "VIERNES-1-A-5"

class Profesor:
    def __init__(self, id, nombre, cursos=None, disponibilidad=None):
        self.id = id
        self.nombre = nombre
        self.cursos = cursos if cursos is not None else []
        self.disponibilidad = disponibilidad if disponibilidad is not None else []
        
    def eliminarDisponibilidad(self, horario):
        if horario in self.disponibilidad:
            self.disponibilidad.remove(horario)
            
    def agregarDisponibilidad(self, horario):
        self.disponibilidad.append(horario)
        
    def eliminarCursos(self, materia):
        if materia in self.cursos:
            self.cursos.remove(materia)
            
    def agregarCursos(self, materia):
        self.cursos.append(materia)
     



class Aula:
    LM9a11 = "LUNESxMIERCOELES-9AM-A-10:55AM"
    LM11a1 = "LUNESxMIERCOELES-11-A-12:55PM"
    LM1a3 = "LUNESxMIERCOELES-1-A-2:55PM"
    LM3a5 = "LUNESxMIERCOELES-3-A-4:55PM"
    MJ9a11 = "MARTESxJUEVES-9AM-A-10:55AM"
    MJ11a1 = "MARTESxJUEVES-11-A-12:55PM"
    MJ1a3 = "MARTESxJUEVES-1-A-2:55PM"
    MJ3a5 = "MARTESxJUEVES-3-A-4:55PM"
    V9a11 = "VIERNES-9-A-1"
    V1a5 = "VIERNES-1-A-5"

    disponibilidad_default = [LM9a11, LM11a1, LM1a3, LM3a5, MJ9a11, MJ11a1, MJ1a3, MJ3a5, V9a11, V1a5]

    def __init__(self, id, capacidad, equipamiento, disponibilidad=None):
        self.id = id
        self.capacidad = capacidad
        self.equipamiento = equipamiento
        self.disponibilidad = disponibilidad.copy() if disponibilidad else Aula.disponibilidad_default.copy()

    def eliminarDisponibilidad(self, horario):
        if horario in self.disponibilidad:
            self.disponibilidad.remove(horario)

    def agregarDisponibilidad(self, horario):
        self.disponibilidad.append(horario)


class Curso:
    def __init__(self, id, nombre, horas_semana, restricciones):
        self.id = id
        self.nombre = nombre
        self.horas_semana = horas_semana
        self.restricciones = restricciones


class HorarioAsignado:
    def __init__(self, materia, profesor, aula, horario):
        self.materia = materia
        self.profesor = profesor
        self.aula = aula
        self.horario = horario  # ejemplo de horario es LUNESxMIERCOELES-9-A-11

    def __str__(self):
        return f"Materia: {self.materia.nombre}, Profesor: {self.profesor.nombre}, Aula: {self.aula.id}, Horario: {self.horario}"



class PlanificadorHorarios:
    def __init__(self, profesores, aulas, cursos):
        self.profesores = profesores
        self.aulas = aulas
        self.cursos = cursos
        self.horarios_asignados = []

    def asignar_horarios(self):
        self.horarios_asignados = []  # Limpiar asignaciones anteriores
        self._backtracking()

    def _backtracking(self, asignaciones=[]):
        if len(asignaciones) == len(self.cursos):
            print("¡Solución encontrada!")
            self.horarios_asignados = asignaciones.copy()
            return True
    
        curso_actual = self.cursos[len(asignaciones)]
        print(f"Curso actual: {curso_actual.nombre}")
        
        
        for profesor in self.profesores:
            if len(profesor.cursos) == 0:
                print("!!!!!!!!!!!!!!!!")
                continue
            if curso_actual.nombre in profesor.cursos:
                print(f"Profe actual: {profesor.nombre}")
                for aula in self.aulas:
                    print("Intento",aula.id)
                    
                    if self._es_disponible(profesor, aula):
                        print("Entro",aula.id)
                        horario = self.cualhorariro(profesor, aula)
                        print(f"Asignando {horario} en {aula.id}")
                        asignacion_actual = (curso_actual.nombre, profesor.nombre, aula.id, horario)
                        print(f"Asignación actual: {asignacion_actual}")
                        asignaciones.append(copy.deepcopy(asignacion_actual))
                        profesor.eliminarDisponibilidad(horario)
                        aula.eliminarDisponibilidad(horario)
                        profesor.eliminarCursos(curso_actual.nombre)
                    
                        if self._backtracking(asignaciones):
                            print("¡Solución encontrada!")
                            return True
        
                        asignaciones.pop()
                        print("RESET")
                        profesor.agregarCursos(curso_actual.nombre)
                        profesor.agregarDisponibilidad(horario)
                        aula.agregarDisponibilidad(horario)
                        print(f"Deshaciendo asignación de {curso_actual.nombre} en {aula.id}")
                print(f"No se encontró asignación para {curso_actual.nombre}")
            return False
    
    def _es_disponible(self, profesor, aula):
     for horario_profesor in profesor.disponibilidad:
             if horario_profesor in aula.disponibilidad:
                 return True
     return False
 
    def cualhorariro(self, profesor, aula):
         for horario_profesor in profesor.disponibilidad:
                 if horario_profesor in aula.disponibilidad:
                     return horario_profesor
                
        
            


# Crear instancias de profesores, aulas y cursos



profesor1 = Profesor(1, "Profesor A", ["Matematicas","Algebra"], [LM9a11,LM11a1])
profesor2 = Profesor(2, "Profesor B", [ "Algebra","Matematicas"], [LM11a1,LM9a11])
profesor3 = Profesor(3, "Profesor C", [ "Matematicas","Algebra"], [MJ3a5,V1a5])

aula1 = Aula(101, 30, ["Proyector"])
aula2 = Aula(102, 30, ["Proyector"])
aula3 = Aula(102, 30, ["Proyector"])

matematicas = Curso(1, "Matematicas", 4, ["Proyector"])
algebra = Curso(2, "Algebra", 4, ["Proyector"])

profesores = [profesor1,profesor2,profesor3]
aulas = [aula1,aula2,aula3]
cursos = [matematicas, algebra,algebra,matematicas,matematicas,algebra]

print("Inicio")
#Crear una instancia de PlanificadorHorarios
planificador = PlanificadorHorarios(profesores, aulas, cursos)

# Ejecutar el algoritmo de asignación de horarios
planificador.asignar_horarios()

# Mostrar los horarios asignados
for asignacion in planificador.horarios_asignados:
    print(asignacion)









