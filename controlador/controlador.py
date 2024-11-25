from modelo.tarea import Tarea  #importar la clase "Tarea" del modelo
from modelo.materia import Materia  #importar la clase "Materia" del modelo

class Controlador:
    def __init__(self):
        self.tareas = []  # inicializa una lista vacía para almacenar tareas
        self.materias = [Materia("Matemática"), Materia("Biología"), Materia("Química"), Materia("Lenguaje"), Materia("Inglés")]  # lista de materias predefinidas

    def agregar_tarea(self, nombre, descripcion, fecha_vencimiento, estado, materia_nombre):
        materia = self.obtener_materia_por_nombre(materia_nombre)
        nueva_tarea = Tarea(nombre, descripcion, fecha_vencimiento, estado, materia)
        self.tareas.append(nueva_tarea)

    def eliminar_tarea(self, index):
        if 0 <= index < len(self.tareas):
            del self.tareas[index]  # elimina la tarea en el índice especificado

    def cambiar_estado_tarea(self, index):
        if 0 <= index < len(self.tareas):
            tarea = self.tareas[index]
            if tarea.estado == "pendiente":
                tarea.estado = "completada"  # cambia el estado de la tarea a "completada"
            else:
                tarea.estado = "pendiente"  # cambia el estado de la tarea a "pendiente"

    def listar_tareas(self):
        return self.tareas  #retorna la lista de tareas

    def obtener_materia_por_nombre(self, nombre):
        for materia in self.materias:
            if materia.nombre == nombre:
                return materia
        return None
