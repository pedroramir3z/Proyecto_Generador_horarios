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

### TESTING
![tester_plan](https://github.com/pedroramir3z/Proyecto_Generador_horarios/assets/150998867/123dbb15-6a6b-4ea4-b743-396cc4b45e5d)


### CRONOGRAMA
