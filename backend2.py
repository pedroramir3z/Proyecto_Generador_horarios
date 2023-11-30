"""
EQUIPO 3
BACK 2 (Sin uso de archivos) By. Paulina Amezcua
"""
import random

profesores = []


def mostrar_menu_horas_no_trabajo():
    print("\nSeleccione el horario en el cual el profesor no puede trabajar:")
    print("\n1- 09:00 am - 10:55 am LUNES")
    print("2- 11:00 am - 12:55 pm LUNES")
    print("3- 01:00 pm - 02:55 pm LUNES")
    print("4- 03:00 pm - 04:55 pm LUNES\n")
    print("\n5- 09:00 am - 10:55 am MARTES")
    print("6- 11:00 am - 12:55 pm MARTES")
    print("7- 01:00 pm - 02:55 pm MARTES")
    print("8- 03:00 pm - 04:55 pm MARTES\n")
    print("\n9- 09:00 am - 10:55 am MIERCOLES")
    print("10- 11:00 am - 12:55 pm MIERCOLES")
    print("11- 01:00 pm - 02:55 pm MIERCOLES")
    print("12- 03:00 pm - 04:55 pm MIERCOLES\n")
    print("\n13 09:00 am - 10:55 am JUEVES")
    print("14- 11:00 am - 12:55 pm JUEVES")
    print("15- 01:00 pm - 02:55 pm JUEVES")
    print("16- 03:00 pm - 04:55 pm JUEVES\n")
    print("\n17 09:00 am - 10:55 am VIERNES")
    print("18- 11:00 am - 12:55 pm VIERNES")
    print("19- 01:00 pm - 02:55 pm VIERNES")
    print("20- 03:00 pm - 04:55 pm VIERNES\n")


def mostrar_menu_carreras():
    print("\nSeleccione la carrera que imparte el profesor:")
    print("\n1- INGENIERIA EN INFORMATICA")
    print("2- INGENIERIA EN COMPUTACION\n")


def mostrar_menu_materias(carrera):
    print("\nElija la materia que el profesor imparte:")

    if carrera == "1":
        # Grupo de 20 materias para INGENIERIA EN INFORMATICA
        materias = [
            "LOGICA Y CONJUNTOS", "INTRODUCCION A LA FISICA", "TALLER DE INTRODUCCION A LA COMPUTACION",
            "TALLER DE COMUNICACION ORAL Y ESCRITA", "INTRODUCCION A LA COMPUTACION (SI)", "TALLER DE REDACCION",
            "INTRODUCCION A LA PROGRAMACION (SI)", "ELEMENTOS DE PROBABILIDAD Y ESTADISTICA",
            "TALLER DE PROGRAMACION ORIENTADA A OBJETOS (SI)", "AUDITORIA DE SISTEMAS (SI)",
            "SISTEMAS DE INFORMACION FINANCIEROS", "SISTEMAS DE INFORMACION PARA LA MANOFACTURA",
            "TALLER DE ESTRUCTURA DE DATOS", "ADMINISTRACION DE RECURSOS HUMANOS", "PROGRAMACION Y LOGICA FUNCIONAL (SI)",
            "LEGISLACION EN INFORMATICA", "TALLER DE PROGRAMACION DE SISTEMAS (SI)",
            "SISTEMAS DE INFORMACION ADMINISTRATIVOS", "INVESTIGACION DE OPERACIONES", "GRAFICAS POR COMPUTADORA (SI)"
        ]
    elif carrera == "2":
        # Grupo de 43 materias para INGENIERIA EN COMPUTACION
        materias = [
            "FUNDAMENTOS DE LA PROGRAMACION (SI)", "ETICA Y LEGISLACION", "LOGICA MATEMATICA",
            "PRECALCULO", "FUNDAMENTOS DE FISICA", "INTRODUCCION A LA INGENIERIA", "PROGRAMACION ESTRUCTURADA (SI)",
            "MATEMATICA DISCRETA", "CALCULO DIFERENCIAL E INTEGRAL", "MECANICA",
            "ADMINISTRACION DE PROYECTOS TECNOLOGICOS",
            "EXPRESION ORAL Y ESCRITA", "PROGRAMACION ORIENTADA A OBJETOS (SI)", "ALGEBRA LINEAL",
            "ECUACIONES DIFERENCIALES", "CIRCUITOS ELECTRICOS Y ELECTROMAGNETISMO (SI)", "SISTEMAS DIGITALES (SI)",
            "ADMINISTRACION", "ESTRUCTURA DE DATOS (SI)", "PROBABILIDAD Y ESTADISTICA", "METODOS NUMERICOS",
            "ARQUITECTURA DE COMPUTADORAS (SI)", "PROGRAMACION PARA INTERNET (SI)", "LIDERAZGO Y EMPRENDIMIENTO",
            "ANALISIS DE ALGORITMOS (SI)", "BASES DE DATOS (SI)", "SISTEMA OPERATIVOS (SI)",
            "FUNDAMENTOS DE INTELIGENCIA ARTIFICIAL (SI)", "REDES DE COMPUTADORAS (SI)",
            "SEMINARIO DE INTEGRACION DE PROTOCOLO",
            "INNOVACION TECNOLOGICA", "INTERACCION HUMANO COMPUTADORA (SI)", "INGENIERIA DE SOFTWARE (SI)",
            "PROGRAMACION DE BAJO NIVEL (SI)", "TEORIA DE LA COMPUTACION", "SEMINARIO DE INTEGRACION DE DESARROLLO",
            "LABORATORIO ABIERTO: DISEÑO (SI)", "COMPILADORES (SI)", "SEGURIDAD EN LA INFORMACION (SI)",
            "LABORATORIO ABIERTO: CONSTRUCCION (SI)", "PROGRAMACION PARALELA Y CONCURRENTE (SI)",
            "SEMINARIO DE INTEGRACION COMUNICACION", "LABORATORIO ABIERTO: PRUEBA (SI)"
        ]
    else:
        materias = []

    for index, materia in enumerate(materias, start=1):
        print(f"{index}. {materia}")


def agregar_profesor():
    nombre = input("\nIngrese el nombre del profesor: ")

    mostrar_menu_horas_no_trabajo()
    user_input = int(input("Seleccione una opción: "))

    while user_input < 1 or user_input > 20:
        print("Entrada inválida. Por favor introduzca un número entre 1 y 20.")
        user_input = int(input("Seleccione una opción: "))

    random_number = random.randint(1, 20)

    while random_number == user_input:
        random_number = random.randint(1, 20)

    horas_no_trabajo = ""
    if random_number == 1:
        horas_no_trabajo = "09:00 am - 10:55 am LUNES"
    elif random_number == 2:
        horas_no_trabajo = "11:00 am - 12:55 pm LUNES"
    elif random_number == 3:
        horas_no_trabajo = "01:00 pm - 02:55 pm LUNES"
    elif random_number == 4:
        horas_no_trabajo = "03:00 pm - 04:55 pm LUNES"
    elif random_number == 5:
        horas_no_trabajo = "09:00 am - 10:55 am MARTES"
    elif random_number == 6:
        horas_no_trabajo = "11:00 am - 12:55 pm MARTES"
    elif random_number == 7:
        horas_no_trabajo = "01:00 pm - 02:55 pm MARTES"
    elif random_number == 8:
        horas_no_trabajo = "03:00 pm - 04:55 pm MARTES"
    elif random_number == 9:
        horas_no_trabajo = "09:00 am - 10:55 am MIERCOLES"
    elif random_number == 10:
        horas_no_trabajo = "11:00 am - 12:55 pm MIERCOLES"
    elif random_number == 11:
        horas_no_trabajo = "01:00 pm - 02:55 pm MIERCOLES"
    elif random_number == 12:
        horas_no_trabajo = "03:00 pm - 04:55 pm MIERCOLES"
    elif random_number == 13:
        horas_no_trabajo = "09:00 am - 10:55 am JUEVES"
    elif random_number == 14:
        horas_no_trabajo = "11:00 am - 12:55 pm JUEVES"
    elif random_number == 15:
        horas_no_trabajo = "01:00 pm - 02:55 pm JUEVES"
    elif random_number == 16:
        horas_no_trabajo = "03:00 pm - 04:55 pm JUEVES"
    elif random_number == 17:
        horas_no_trabajo = "09:00 am - 10:55 am VIERNES"
    elif random_number == 18:
        horas_no_trabajo = "11:00 am - 12:55 pm VIERNES"
    elif random_number == 19:
        horas_no_trabajo = "01:00 pm - 02:55 pm VIERNES"
    elif random_number == 20:
        horas_no_trabajo = "03:00 pm - 04:55 pm VIERNES"
    else:
        print("Opción seleccionada")

    mostrar_menu_carreras()
    opcion_carrera = input("Seleccione una opción: ")


    carrera = ""
    if opcion_carrera == "1":
        carrera = "INGENIERIA EN INFORMATICA"
    elif opcion_carrera == "2":
        carrera = "INGENIERIA EN COMPUTACION"
    else:
        print("Opción no válida. Se dejará la carrera vacía.")

    if opcion_carrera in ["1", "2"]:
        mostrar_menu_materias(opcion_carrera)
        opcion_materia = input("Seleccione una opción: ")

        materia = ""
        if 1 <= int(opcion_materia) <= (20 if opcion_carrera == "1" else 43):
            materias = [
                "LOGICA Y CONJUNTOS", "INTRODUCCION A LA FISICA", "TALLER DE INTRODUCCION A LA COMPUTACION",
                "TALLER DE COMUNICACION ORAL Y ESCRITA", "INTRODUCCION A LA COMPUTACION (SI)", "TALLER DE REDACCION",
                "INTRODUCCION A LA PROGRAMACION (SI)", "ELEMENTOS DE PROBABILIDAD Y ESTADISTICA",
                "TALLER DE PROGRAMACION ORIENTADA A OBJETOS (SI)", "AUDITORIA DE SISTEMAS (SI)",
                "SISTEMAS DE INFORMACION FINANCIEROS", "SISTEMAS DE INFORMACION PARA LA MANOFACTURA",
                "TALLER DE ESTRUCTURA DE DATOS", "ADMINISTRACION DE RECURSOS HUMANOS", "PROGRAMACION Y LOGICA FUNCIONAL (SI)",
                "LEGISLACION EN INFORMATICA", "TALLER DE PROGRAMACION DE SISTEMAS (SI)",
                "SISTEMAS DE INFORMACION ADMINISTRATIVOS", "INVESTIGACION DE OPERACIONES", "GRAFICAS POR COMPUTADORA (SI)"
            ] if opcion_carrera == "1" else [
                "FUNDAMENTOS DE LA PROGRAMACION (SI)", "ETICA Y LEGISLACION", "LOGICA MATEMATICA",
                "PRECALCULO", "FUNDAMENTOS DE FISICA", "INTRODUCCION A LA INGENIERIA", "PROGRAMACION ESTRUCTURADA (SI)",
                "MATEMATICA DISCRETA", "CALCULO DIFERENCIAL E INTEGRAL", "MECANICA",
                "ADMINISTRACION DE PROYECTOS TECNOLOGICOS",
                "EXPRESION ORAL Y ESCRITA", "PROGRAMACION ORIENTADA A OBJETOS (SI)", "ALGEBRA LINEAL",
                "ECUACIONES DIFERENCIALES", "CIRCUITOS ELECTRICOS Y ELECTROMAGNETISMO (SI)", "SISTEMAS DIGITALES (SI)",
                "ADMINISTRACION", "ESTRUCTURA DE DATOS (SI)", "PROBABILIDAD Y ESTADISTICA", "METODOS NUMERICOS",
                "ARQUITECTURA DE COMPUTADORAS (SI)", "PROGRAMACION PARA INTERNET (SI)", "LIDERAZGO Y EMPRENDIMIENTO",
                "ANALISIS DE ALGORITMOS (SI)", "BASES DE DATOS (SI)", "SISTEMA OPERATIVOS (SI)",
                "FUNDAMENTOS DE INTELIGENCIA ARTIFICIAL (SI)", "REDES DE COMPUTADORAS (SI)",
                "SEMINARIO DE INTEGRACION DE PROTOCOLO",
                "INNOVACION TECNOLOGICA", "INTERACCION HUMANO COMPUTADORA (SI)", "INGENIERIA DE SOFTWARE (SI)",
                "PROGRAMACION DE BAJO NIVEL (SI)", "TEORIA DE LA COMPUTACION", "SEMINARIO DE INTEGRACION DE DESARROLLO",
                "LABORATORIO ABIERTO: DISEÑO (SI)", "COMPILADORES (SI)", "SEGURIDAD EN LA INFORMACION (SI)",
                "LABORATORIO ABIERTO: CONSTRUCCION (SI)", "PROGRAMACION PARALELA Y CONCURRENTE (SI)",
                "SEMINARIO DE INTEGRACION COMUNICACION", "LABORATORIO ABIERTO: PRUEBA (SI)"
            ]

            materia = materias[int(opcion_materia) - 1]
        else:
            print("Opción no válida. Se dejará la materia vacía.")

    profesor = {
        "Nombre": nombre,
        "Horas_no_trabajo": horas_no_trabajo,
        "Carrera": carrera,
        "Materia": materia
    }

    profesores.append(profesor)
    print("Profesor agregado exitosamente.")


def generar_tabla_horarios():
    print("\nTabla de Horarios para Profesores:")
    print("{:<20} {:<20} {:<20} {:<20}".format("Nombre", "Horas no trabajo",
                                               "Carrera", "Materia"))

    for i, profesor in enumerate(profesores):
        print("{:<20} {:<20} {:<20} {:<20}".format(profesor["Nombre"],
                                                   profesor["Horas_no_trabajo"], profesor["Carrera"],
                                                   profesor["Materia"]))

    if not profesores:
        print("No hay profesores en la lista.")
        return

    opcion_eliminar = input("\nIngrese el número del profesor que desea eliminar (o '0' para volver): ")

    if opcion_eliminar == "0":
        return
    try:
        indice_profesor = int(opcion_eliminar) - 1
        if 0 <= indice_profesor < len(profesores):
            profesor_eliminado = profesores.pop(indice_profesor)
            print(f"Profesor '{profesor_eliminado['Nombre']}' eliminado exitosamente.")
        else:
            print("Número de profesor no válido.")
    except ValueError:
        print("Por favor, ingrese un número válido.")


def main():
    while True:
        print("\nMenú:")
        print("\n1. Agregar profesor")
        print("2. Generar tabla de horarios")
        print("3. Salir\n")

        opcion_menu_principal = input("\nSeleccione una opción: ")

        if opcion_menu_principal == "1":
            while True:
                print("\nSubmenú - Agregar Profesor:")
                print("\n1. Nombre del profesor")
                print("2. Horas que no puede trabajar")
                print("4. Carrera")
                print("5. Volver al menú principal\n")

                opcion_submenu_agregar_profesor = input("\nSeleccione una opción: ")

                if opcion_submenu_agregar_profesor == "1":
                    agregar_profesor()
                elif opcion_submenu_agregar_profesor == "2":
                    mostrar_menu_horas_no_trabajo()
                    mostrar_menu_carreras()
                    opcion_carrera = input("\nSeleccione una opción: ")
                    if opcion_carrera in ["1", "2"]:
                        mostrar_menu_materias(opcion_carrera)
                    else:
                        print("Opción no válida.")
                elif opcion_submenu_agregar_profesor == "3":
                    mostrar_menu_carreras()
                    opcion_carrera = input("\nSeleccione una opción: ")
                    if opcion_carrera in ["1", "2"]:
                        mostrar_menu_materias(opcion_carrera)
                    else:
                        print("Opción no válida.")
                elif opcion_submenu_agregar_profesor == "4":
                    mostrar_menu_carreras()
                    opcion_carrera = input("\nSeleccione una opción: ")
                    if opcion_carrera in ["1", "2"]:
                        mostrar_menu_materias(opcion_carrera)
                    else:
                        print("Opción no válida.")
                elif opcion_submenu_agregar_profesor == "5":
                    break
                else:
                    print("Opción no válida. Inténtelo de nuevo.")

        elif opcion_menu_principal == "2":
            generar_tabla_horarios()

        elif opcion_menu_principal == "3":
            print("Saliendo del programa. FIN")
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()