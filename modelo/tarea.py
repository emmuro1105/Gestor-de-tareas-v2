class Tarea:
    def __init__(self, nombre, descripcion, fecha_vencimiento, estado=False, materia=None):
        self.nombre = nombre  #inicializa el nombre de la tarea
        self.descripcion = descripcion  #inicializa la descripción de la tarea
        self.fecha_vencimiento = fecha_vencimiento  #inicializa la fecha de vencimiento
        self.estado = estado  #estado "False" por defecto
        self.materia = materia  #inicializa la materia como None por defecto

    def completar(self):
        self.estado = "completada"  #cambia el estado de la tarea a "completada"

    def editar(self, nombre, descripcion, fecha_vencimiento, materia):
        self.nombre = nombre  #actualiza el nombre de la tarea
        self.descripcion = descripcion  #actualiza la descripción de la tarea
        self.fecha_vencimiento = fecha_vencimiento  #actualiza la fecha de vencimiento
        self.materia = materia  #actualiza la materia de la tarea

    def eliminar(self):
        del self  #elimina la instancia de tarea

    def mostrar_materia(self):
            return f"Materia: {self.materia.nombre}" #retorna el nombre de la materia
