class Aula:
    LM9a11 = "LUNESxMIERCOLES-9AM-A-10:55AM"
    LM11a1 = "LUNESxMIERCOLES-11AM-A-12:55PM"
    LM1a3 = "LUNESxMIERCOLES-1PM-A-2:55PM"
    LM3a5 = "LUNESxMIERCOLES-3PM-A-4:55PM"
    MJ9a11 = "MARTESxJUEVES-9AM-A-10:55AM"
    MJ11a1 = "MARTESxJUEVES-11AM-A-12:55PM"
    MJ1a3 = "MARTESxJUEVES-1PM-A-2:55PM"
    MJ3a5 = "MARTESxJUEVES-3PM-A-4:55PM"
    V9a1 = "VIERNES-9AM-A-1PM"
    V1a5 = "VIERNES-1PM-A-5PM"

    disponibilidad_default = [LM9a11, LM11a1, LM1a3, LM3a5, MJ9a11, MJ11a1, MJ1a3, MJ3a5, V9a1, V1a5]

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

