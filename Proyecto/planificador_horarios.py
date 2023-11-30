import copy

class PlanificadorHorarios:
    def __init__(self, profesores, aulas, cursos):
        self.profesores = profesores
        self.aulas = aulas
        self.cursos = cursos
        self.horarios_asignados = []

    def asignar_horarios(self):
        #Asigna horarios a los cursos utilizando el algoritmo de backtracking.
        self.horarios_asignados = []  # Limpiar asignaciones anteriores
        self._backtracking()

    def _backtracking(self, asignaciones=[]):   # Algoritmo de backtracking para asignar horarios a los cursos.
    
        if len(asignaciones) == len(self.cursos):
            print("!!!!!Solución encontrada!!!!")
            self.horarios_asignados = asignaciones.copy()
            return True
        curso_actual = self.cursos[len(asignaciones)]
        
        for profesor in self.profesores:
            if len(profesor.cursos) == 0:
                continue
            if curso_actual.nombre not in profesor.cursos:
                continue
            if curso_actual.nombre in profesor.cursos:
                for aula in self.aulas:
                    if self._es_disponible(profesor, aula) and self.es_disponibleAulaCurso(curso_actual,aula):
                        horario = self.cualhorariro(profesor, aula)
                        asignacion_actual = (curso_actual.nombre, profesor.nombre, aula.id, horario)
                        asignaciones.append(copy.deepcopy(asignacion_actual))
                        profesor.eliminarDisponibilidad(horario)
                        aula.eliminarDisponibilidad(horario)
                        profesor.eliminarCursos(curso_actual.nombre)
                    
                        if self._backtracking(asignaciones):
                            print("Solución encontrada")
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
                
 
    def es_disponibleAulaCurso(self, curso, aula):
        for restriciones in curso.restricciones:
                if restriciones in aula.equipamiento:
                    return True
        return False   
 
    def cualhorariro(self, profesor, aula):
         for horario_profesor in profesor.disponibilidad:
                 if horario_profesor in aula.disponibilidad:
                     return horario_profesor