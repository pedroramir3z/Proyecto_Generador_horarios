# Proyecto_Generador_horarios

Este proyecto deberá ser capáz de generar un horario para profesores, este contendrá una respectiva lista de maestros, una lista también de materias para poder asignarle una a su respectivo profesor, las aulas que se encontrarán disponibles para su uso con sus capacidades y restricciones, además de que deberá tener la capacidad de leer los horarios en los que los profesores no se encontrarán disponibles. 
Debe contener la parte del frontend a modo llamativo ya que sería una pagina visualmente atractiva para su venta conteniendo todos los botones necesarios para un manejo sencillo pensando en el usuario que lo portará, a la vez que el reto principal será poder ligarlo al código de la sección del backend, el cual tiene que tener una funcionalidad completa.
Se debe de optimizar la asignación de cursos y cumplir con las restricciones dadas.

##### Integrantes

- Paulina Amezcua García-**Generalista**
- Guillermo Gómez Castañeda-**Frontend**
- Christian Francisco Rojas Espinoza-**Backend**
- Pedro Ángel Ramírez Martínez-**Tester**
- Víctor Alejandro Hernández Briseño-**Administrador**

# Documentación

### FRONTEND

*****IDEA*****

Para tener una visualización más clara de lo que llevaría el frontend generamos diferentes listas, como las materias y los horarios disponibles.
Después comenzamos trabajando la visualización de lo que serían las pantallas que proximamente crearíamos, haciendo unos bocetos bastante simples en una hoja y después de confirmar el que todos estuvieramos de a cuerdo, lo pasamos justamente a un documento.

Las listas creadas fueron las siguientes:

##### **Datos de materias:**

Una lista de materias para ICOM.
ICOM

	FUNDAMENTOS DE LA PROGRAMACION 
	ETICA Y LEGISLACION
	LOGICA MATEMATICA 
	PRECALCULO
	FUNDAMENTOS DE FISICA
	INTRODUCCION A LA INGENIERIA 
	PROGRAMACION ESTRUCTURADA
	MATEMATICA DISCRETA
	CALCULO DIFERENCIAL E INTEGRAL
	MECANICA 
	ADMINISTRACION DE PROYECTOS TECNOLOGICOS
	EXPRESION ORAL Y ESCRITA 
	PROGRAMACION ORIENTADA A OBJETOS
	ALGEBRA LINEAL
	ECUACIONES DIFERENCIALES
	CIRCUITOS ELECTRICOS Y ELECTROMAGNETISMO 
	SISTEMAS DIGITALES
	ADMINISTRACION 
	ESTRUCTURA DE DATOS 
	PROBABILIDAD Y ESTADISTICA 
	METODOS NUMERICOS 
	ARQUITECTURA DE COMPUTADORAS 
	PROGRAMACION PARA INTERNET 
	LIDERAZGO Y EMPRENDIMIENTO 
	ANALISIS DE ALGORITMOS
	BASES DE DATOS
	SISTEMA OPERATIVOS
	FUNDAMENTOS DE INTELIGENCIA ARTIFICIAL
	REDES DE COMPUTADORAS 
	SEMINARIO DE INTEGRACION DE PROTOCOLO 
	INNOVACION TECNOLOGICA 
	INTERACCION HUMANO COMPUTADORA 
	INGENIERIA DE SOFTWARE 
	PROGRAMACION DE BAJO NIVEL 
	TEORIA DE LA COMPUTACION 
	SEMINARIO DE INTEGRACION DE DESARROLLO 
	LABORATORIO ABIERTO: DISEÑO 
	COMPILADORES 
	SEGURIDAD EN LA INFORMACION 
	LABORATORIO ABIERTO: CONSTRUCCION 
	PROGRAMACION PARALELA Y CONCURRENTE
	SEMINARIO DE INTEGRACION COMUNICACION 
	LABORATORIO ABIERTO: PRUEBA

Y una lista de materias para INFO.
INFO

	LOGICA Y CONJUNTOS
	INTRODUCCION A LA FISICA
	TALLER DE INTRODUCCION A LA COMPUTACION
	TALLER DE COMUNICACION ORAL Y ESCRITA
	INTRODUCCION A LA COMPUTACION 
	TALLER DE REDACCION 
	INTRODUCCION A LA PROGRAMACION 
	ELEMENTOS DE PROBABILIDAD Y ESTADISTICA 
	TALLER DE PROGRAMACION ORIENTADA A OBJETOS
	AUDITORIA DE SISTEMAS 
	SISTEMAS DE INFORMACION FINANCIEROS
	SISTEMAS DE INFORMACION PARA LA MANOFACTURA
	TALLER DE ESTRUCTURA DE DATOS
	ADMINISTRACION DE RECURSOS HUMANOS
	PROGRAMACION Y LOGICA FUNCIONAL
	LEGISLACION EN INFORMATICA 
	TALLER DE PROGRAMACION DE SISTEMAS
	SISTEMAS DE INFORMACION ADMINISTRATIVOS 
	INVESTIGACION DE OPERACIONES
	GRAFICAS POR COMPUTADORA

Además de los horarios disponibles de la universidad desde donde inician las clases en un día normal hasta la hora en que se dan por finalizadas.
HORARIOS 

	09:00 am - 10:55 am
	11:00 am - 12:55 pm
	01:00 pm - 02:55 pm
	03:00 pm - 04:55 pm

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Se han creado el diseño de las dos ventanas, la principal y ventana de agregar profesor ambas con sus bloques de herramienta e interacción. Se han realizado a través de la aplicación QT Designer, la cual se instala al escribir el comando pip install pqt5 tools, como parte de las herramientas que brinda PQT5.

**Ventana 1 (Ventana Principal):** 
Se estableció un tamaño fijo de 838x579 pixeles para la ventana por lo cual no se agregaron botones de maximizar ni minimizar, únicamente se tiene una barra superior en color verde y dentro de esta se encuentra un botón a la derecha que tiene un icono en 20x20 pixeles que hace la función de cerrar el programa.
Se agregó una etiqueta “Asignador de Horarios” como título de la pagina principal debajo de este se agregaron dos botones, ambos en color verde y cada uno con su ícono como representación gráfica de “Agregar profesor” y “Generar Horario”. Se usaron dos barras horizontales como parte del diseño una en la parte superior y la otra en la parte inferior


**Ventana 2 (Agregar Profesor):**
En esta se estableció un tamaño fijo de 838x579 pixeles para la ventana por lo cual no se agregaron botones de maximizar ni minimizar, únicamente se tiene una barra superior en color verde y dentro de esta se encuentra un botón a la derecha que tiene un icono en 20x20 pixeles que hace la función de cerrar el programa.
Se agregó una etiqueta “Asignador de Horarios” como título de la página principal, debajo otra etiqueta que indica el área para agregar a los profesores.
Tres etiquetas de texto con los nombres de “Nombre del profesor”, “Horas que no tiene disponibles” y “Materias Asignadas”. Cada uno cuenta con un bloque de interacción de input del lado derecho. Se tiene un editor de texto input en color blanco para el nombre del profesor y para materia asignada, el único diferente es el de las horas, se agregaron dos bloques de edición de horario modo input para asegurar el ingreso de los datos en el formato requerido. Por ultimo, se agregó un botón verde con el texto guardar el cual tiene un icono como representación grafica de agregar profesor. El botón guardará los datos ingresados en las 4 casillas anteriores. 

<p>
Todo esto de hace de acuerdo con el diagrama de usuario y a las propuestas de diseño aceptadas por todo el equipo 3:
</p>

![](https://github.com/pedroramir3z/Proyecto_Generador_horarios/blob/master/imagenes/0f69ea0f-6f37-47ff-a967-7418a5c21d0b.jfif)
![](https://github.com/pedroramir3z/Proyecto_Generador_horarios/blob/master/imagenes/c4857c6c-7c38-47cf-97d2-773788f080a3.jfif)
![](https://github.com/pedroramir3z/Proyecto_Generador_horarios/blob/master/imagenes/cf1ec78d-da56-4350-91d4-f2f3c433294d.jfif)


La idea del como se verá surgió con esas listas, para tener en cuenta que se dividirán en dos secciones, las de ICOM y las de INFO teniendo 43 y 20 materias cada sección respectivamente. Nos percatamos que sería más sencillo para el usuario tener en automatico una lista desplegable de las materias para una mayor facilidad de asignación.
Será una lista con dos opciones:

*ICOM*

*INFO*

Al dar click sobre cualquiera de las dos se desplegará tambien una lista de materias de su debida carrera y el usuario como mencionamos anteriormente, podra simplemente dar click sobre la materia que el profesor impartirá la clase.
Si el profesor da clase a más de una materia de igual manera podrá elegir diferentes opciones agregables.

Hicimos lo mismo para la lista de horarios, así el plan es que el usuario pueda elegir las horas que el profesor NO puede trabajar de manera sencilla con un solo click sobre las horas especificas que desea agregar.
En horas que no tiene disponibles va a lanzar dos listas ya echas:

La primera será de horario:

*HORARIO:*

09:00 am - 10:55 am
11:00 am - 12:55 pm
01:00 pm - 02:55 pm
03:00 pm - 04:55 pm

Y LA sugunda tendrá el día, justamente para especificar en que día no puede cumplir el horario anteriormente asignado.

*DIA:*

LUNES
MARTES
MIÉRCOLES
JUEVES
VIERNES
SÁBADO

De igual manera una vez seleccionado un horario que no pueda puede debe poder ingresar aún más para que no sea tan limitado.

A diferencia del nombre, aquí no aparecerá ninguna lista predicha ya que este será totalmente escrito por el usuario en cuestión.

*****MANUAL DE USUARIO*****

Para utilizar el programa con total eficiencia creamos esta sección llamada manual de usuario, dedicada en hacer la experiencia de este programa más sencilla y confortante

Al iniciar el sistema te aparecerán dos botones, cada uno con su temática principal, el primer botón llamado **"Agregar profesor"**
Y el segundo botón llamado **"Generar horario"**

Al hacer click en el primer botón nos lanza a una segunda pestaña o pantalla
La cual sirve para efectivamente agregar a un nuevo profesor
En esta sección podemos realizar 3 cosas
- Primero colocar el nombre completo del profesor que se agregará manualmente, esto es dando click en el recuadro blanco de la derecha
- Después podemos también seleccionar los horarios en los días que el profesor NO podrá asistir, se realiza igual dando click en el primer recuadro
En este aparecerá una lista desplegable del día de la semana en el cual seleccionarás el horario.
Y en el recuadro siguiente justamente el horario que no puede asistir ese día.
(Se pueden agregar diferentes horarios y días según las necesidades del profesor)

- Y la tercer capacidad realizable es asignarle una o varias materias al profesor
Al darle click al recuadro blanco de la derecha de "Materia(s) asignada(s)"
Se desplegará igual una lista con dos nombres de carreras
"ICOM"
e 
"INFO"

Usted cómo usuario elegirá la carrera que imparte el profesor y al seleccionarla volverá a aparecer otra lista desplegable de todas las materias de esa carrera, seleccionando así usted la que su profesor imparte.

Una vez finalizado el llenado de este pequeño formulario dará click en el botón de más abajo llamado **"Guardar"**

Para que el sistema pueda asignarle al profesor su horario cosrrespondiente respetando así sus necesidades horaricas.

Regresando después a la primer pantalla inicial

Ahora seleccionaremos la opción de **"Generar horario"**
Y podemos ver qué nos manda a una tabla con las materias impartidas, los profesores que las imparten (Los cuales el usuario fué agregando manualmente), los horarios en los que se encuentran junto al día, y el aula correspondiente.


***DIFICULTADES PRESENTADAS AL INICIO DE LA REALIZACION DE LA INTERFAZ***

Nuestra primer dificultad fué a la hora de buscar en donde la reslizaríamos, encontramos muchas opciones de librerías las cuales ya estaban bastante obsoletas, después con una busqyueda un poco más superficial llegamos con PyQT, y viendo bastantes tutoriales de uso nos enteramos de que una más facil de utilizar y con más funciones usables era su version algo más actualizada llamada PyQT5, fué un pequeño caos el encontrar que versiones eran compatibles con otras versiones de python llegando a notar que las que teníamos instaladas no las leería, entonces tuvimos que re intalar python en su versión 3.9 para así poder movernos con una mayor libertad en este entorno. Fué un poco confuso al inicio pero una vez resulto pudimos comenzar con el aprendizaje de creaciones de interfaces de esta manera, ya que ptra dificultad fue:
El poco conocimiento sobre esta herramienta.

### BACKEND

(palabras de Cristian)
<p>
Realice cambios en la disponibilidad de profesor y aula, ya que me causaba mucho conflictos a la hora de eliminar y agregar, ya que esto lo necesito para el algoritmo backtraking, asi que cambie con horarios prestablecidos. Y aun asi con estos horarios prestablecidos tuve muchos de los mismos problemas y me percate que el problema que puedo que me tardara mucho mas de lo que quería fue en la clase Aula, descubrí que al eliminar un campo de disponibilidad, se afectaban todas las aulas. La raíz del problema estaba en el uso de constantes, que resolví declarándolas dentro de la clase.
</p>
<p>
Para darme cuenta de esto hice muchas corridas de escritorio, porque realmente no tenía por qué hacer eso el programa, pregunté hasta chatgpt sobre el aula y dice que estaba bien, que no encontraba problemas en la implementación de aula, pero con las corridas de escritorio me di cuenta de todo lo que se hacia mal, por que si, como eso no tendría que pasar cambie mucho del código pensando que era eso. Pero el gran problema como mencionado fue las constantes declaradas.
</p>
**Ejemplo de corrida de escirtorio: **

**Inicio**

	Curso actual: Matematicas
	Profe actual: Profesor A
	Entro 101
	Asignando LUNESxMIERCOELES-9AM-A-10:55AM en 101
	Asignación actual: ('Matematicas', 'Profesor A', 101, 'LUNESxMIERCOELES-9AM-A-10:55AM')
	['LUNESxMIERCOELES-9AM-A-10:55AM', 'LUNESxMIERCOELES-11-A-12:55PM', 'LUNESxMIERCOELES-1-A-2:55PM', 'LUNESxMIERCOELES-3-A-4:55PM', 'MARTESxJUEVES-9AM-A-10:55AM', 'MARTESxJUEVES-11-A-12:55PM', 'MARTESxJUEVES-1-A-2:55PM', 'MARTESxJUEVES-3-A-4:55PM', 'VIERNES-9-A-1', 'VIERNES-1-A-5']
	
	Curso actual: Algebra
	Profe actual: Profesor A
	Entro 101
	Asignando LUNESxMIERCOELES-11-A-12:55PM en 101
	Asignación actual: ('Algebra', 'Profesor A', 101, 'LUNESxMIERCOELES-11-A-12:55PM')
	['LUNESxMIERCOELES-11-A-12:55PM', 'LUNESxMIERCOELES-1-A-2:55PM', 'LUNESxMIERCOELES-3-A-4:55PM', 'MARTESxJUEVES-9AM-A-10:55AM', 'MARTESxJUEVES-11-A-12:55PM', 'MARTESxJUEVES-1-A-2:55PM', 'MARTESxJUEVES-3-A-4:55PM', 'VIERNES-9-A-1', 'VIERNES-1-A-5']

	Curso actual: Matematicas
	!!!!!!!!!!!!!!!!
	Profe actual: Profesor B
	Entro 102
	Asignando LUNESxMIERCOELES-11-A-12:55PM en 102
	Asignación actual: ('Matematicas', 'Profesor B', 102, 'LUNESxMIERCOELES-11-A-12:55PM')
	['LUNESxMIERCOELES-9AM-A-10:55AM', 'LUNESxMIERCOELES-11-A-12:55PM', 'LUNESxMIERCOELES-1-A-2:55PM', 'LUNESxMIERCOELES-3-A-4:55PM', 'MARTESxJUEVES-9AM-A-10:55AM', 'MARTESxJUEVES-11-A-12:55PM', 'MARTESxJUEVES-1-A-2:55PM', 'MARTESxJUEVES-3-A-4:55PM', 'VIERNES-9-A-1', 'VIERNES-1-A-5']

	Curso actual: Algebra
	!!!!!!!!!!!!!!!!
	Profe actual: Profesor B
	Entro 102
	Asignando LUNESxMIERCOELES-9AM-A-10:55AM en 102
	Asignación actual: ('Algebra', 'Profesor B', 102, 'LUNESxMIERCOELES-9AM-A-10:55AM')
	['LUNESxMIERCOELES-9AM-A-10:55AM', 'LUNESxMIERCOELES-1-A-2:55PM', 'LUNESxMIERCOELES-3-A-4:55PM', 'MARTESxJUEVES-9AM-A-10:55AM', 'MARTESxJUEVES-11-A-12:55PM', 'MARTESxJUEVES-1-A-2:55PM', 'MARTESxJUEVES-3-A-4:55PM', 'VIERNES-9-A-1', 'VIERNES-1-A-5']

	Curso actual: Matematicas
	!!!!!!!!!!!!!!!!
	!!!!!!!!!!!!!!!!
	Profe actual: Profesor C
	Entro 101
	Asignando VIERNES-1-A-5 en 101
	Asignación actual: ('Matematicas', 'Profesor C', 101, 'VIERNES-1-A-5')
	['LUNESxMIERCOELES-1-A-2:55PM', 'LUNESxMIERCOELES-3-A-4:55PM', 'MARTESxJUEVES-9AM-A-10:55AM', 'MARTESxJUEVES-11-A-12:55PM', 'MARTESxJUEVES-1-A-2:55PM', 'MARTESxJUEVES-3-A-4:55PM', 'VIERNES-9-A-1', 'VIERNES-1-A-5']

	Curso actual: Algebra
	!!!!!!!!!!!!!!!!
	!!!!!!!!!!!!!!!!
	Profe actual: Profesor C
	Entro 104
	Asignando LUNESxMIERCOELES-11-A-12:55PM en 104
	Asignación actual: ('Algebra', 'Profesor C', 104, 'LUNESxMIERCOELES-11-A-12:55PM')
	['LUNESxMIERCOELES-9AM-A-10:55AM', 'LUNESxMIERCOELES-11-A-12:55PM', 'LUNESxMIERCOELES-1-A-2:55PM', 'LUNESxMIERCOELES-3-A-4:55PM', 'MARTESxJUEVES-9AM-A-10:55AM', 'MARTESxJUEVES-11-A-12:55PM', 'MARTESxJUEVES-1-A-2:55PM', 'MARTESxJUEVES-3-A-4:55PM', 'VIERNES-9-A-1', 'VIERNES-1-A-5']
	¡Solución encontrada!
	¡Solución encontrada!
	¡Solución encontrada!
	¡Solución encontrada!
	¡Solución encontrada!
	¡Solución encontrada!
	¡Solución encontrada!
	('Matematicas', 'Profesor A', 101, 'LUNESxMIERCOELES-9AM-A-10:55AM')
	('Algebra', 'Profesor A', 101, 'LUNESxMIERCOELES-11-A-12:55PM')
	('Matematicas', 'Profesor B', 102, 'LUNESxMIERCOELES-11-A-12:55PM')
	('Algebra', 'Profesor B', 102, 'LUNESxMIERCOELES-9AM-A-10:55AM')
	('Matematicas', 'Profesor C', 101, 'VIERNES-1-A-5')
	('Algebra', 'Profesor C', 104, 'LUNESxMIERCOELES-11-A-12:55PM')
 
**Solo usando estos datos**

	profesor1 = Profesor(1, "Profesor A", ["Matematicas","Algebra"], [LM9a11,LM11a1])
	profesor2 = Profesor(2, "Profesor B", [ "Algebra","Matematicas"], [LM11a1,LM9a11])
	profesor3 = Profesor(3, "Profesor C", [ "Matematicas","Algebra"], [LM11a1,V1a5])
	aula1 = Aula(101, 30, ["Proyector"])
	aula2 = Aula(102, 30, ["Proyector"])
	aula3 = Aula(103, 30, ["Pintaroon"])
	aula3 = Aula(104, 30, ["Proyector"])
	matematicas = Curso(1, "Matematicas", 4, ["Proyector"])
	algebra = Curso(2, "Algebra", 4, ["Proyector"])

### TESTING
![tester_plan](https://github.com/pedroramir3z/Proyecto_Generador_horarios/assets/150998867/123dbb15-6a6b-4ea4-b743-396cc4b45e5d)


### CRONOGRAMA
