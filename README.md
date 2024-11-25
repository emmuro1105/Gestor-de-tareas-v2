Este programa permite gestionar tareas mediante una interfaz gráfica de usuario (GUI) utilizando Tkinter. El programa sigue el patrón de diseño MVC (Modelo-Vista-Controlador), donde las clases Tarea y Materia representan los datos y las reglas de negocio, la clase Vista maneja la interfaz gráfica, y la clase Controlador maneja las interacciones entre la vista y el modelo.

Funcionamiento
El programa se compone principalmente de dos partes:
Formulario de Tareas:
	Campos para ingresar los atributos de la tarea, tales como el nombre, fecha de vencimiento, estado de la tarea y materia.
Panel de Control:
	Botones para agregar, eliminar o cambiar el estado de la tarea seleccionada.

Diagrama de Clases
El siguiente diagrama de clases ilustra las clases principales y sus relaciones:
Clase Tarea
	Atributos:

	-nombre: Nombre de la tarea.

	-descripcion: Descripción de la tarea.

	-fecha_vencimiento: Fecha de vencimiento de la tarea.

	-estado: Estado de la tarea (completada o no).
	
	-materia: Materia a la que pertenece la tarea

	Métodos:

	-completar(): Marca la tarea como completada.

	-editar(nombre, descripcion, fecha_vencimiento): Edita los atributos de la tarea.

	-eliminar(): Elimina la tarea.

	-mostrar_materia(): Retorna el nombre de la materia.


Clase Materia
	Atributos: 

	-nombre: Nombre de la materia
	
	

Objetivos y Requerimientos
Objetivos
	Proveer una interfaz intuitiva y fácil de usar para la gestión de tareas.
	Permitir a los usuarios agregar, editar y eliminar tareas de manera eficiente.
	Facilitar la visualización y actualización del estado de las tareas.

Requerimientos
	Hardware: Computadora con capacidad para ejecutar Python.
	Software:Python 3.x
	Bibliotecas necesarias: Tkinter (incluida en Python estándar)

Consideraciones
Usabilidad: La interfaz debe ser intuitiva y fácil de navegar.
Rendimiento: La aplicación debe responder rápidamente a las acciones del usuario.