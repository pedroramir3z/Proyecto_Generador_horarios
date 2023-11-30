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
        
        
        