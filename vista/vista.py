from tkinter import *
from tkinter import messagebox

class Vista:
    def __init__(self, root, controlador):
        #widget de ventana principal
        self.controlador = controlador
        self.root = root
        self.root.title("gestión de tareas")  #título de la ventana
        self.root.geometry("750x450")  #tamaño de la ventana
        self.root.config(bg="#2c2c2c")  #color de fondo

        #estilo de los widgets
        label_bg = "#404040"  #color de fondo de las etiquetas
        label_fg = "#ffffff"  #color del texto de las etiquetas
        entry_bg = "#3d3d3d"  #fondo de los campos de texto
        entry_fg = "#ffffff"  #color del texto en los campos de texto
        button_bg = "#555555"  #fondo de los botones
        button_fg = "#ffffff"  #color del texto en los botones
        list_bg = "#404040"  #fondo de la lista
        list_fg = "#ffffff"  #color del texto en la lista

        #contenedor del formulario
        self.frameFormulario = Frame(self.root, bg="#4d4d4d")
        self.frameFormulario.pack(pady=10, padx=10)

        #campo de nombre de la tarea
        self.lblNombre = Label(self.frameFormulario, text="nombre de la tarea", bg=label_bg, fg=label_fg)
        self.lblNombre.grid(row=0, column=0, padx=5, pady=5, sticky=E)
        self.entryNombre = Entry(self.frameFormulario, bg=entry_bg, fg=entry_fg)
        self.entryNombre.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        #campo de fecha de vencimiento
        self.lblFecha = Label(self.frameFormulario, text="fecha de vencimiento", bg=label_bg, fg=label_fg)
        self.lblFecha.grid(row=1, column=0, padx=5, pady=5, sticky=E)
        self.entryFecha = Entry(self.frameFormulario, bg=entry_bg, fg=entry_fg)
        self.entryFecha.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        #lista desplegable para el estado de la tarea
        self.lblEstado = Label(self.frameFormulario, text="estado de la tarea", bg=label_bg, fg=label_fg)
        self.lblEstado.grid(row=2, column=0, padx=5, pady=5, sticky=E)
        self.estadoVar = StringVar(value="pendiente")
        self.dropdownEstado = OptionMenu(self.frameFormulario, self.estadoVar, "pendiente", "completada")
        self.dropdownEstado.config(bg=button_bg, fg=button_fg)
        self.dropdownEstado.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        #lista desplegable para la materia de la tarea
        self.lblMateria = Label(self.frameFormulario, text="materia de la tarea", bg=label_bg, fg=label_fg)
        self.lblMateria.grid(row=3, column=0, padx=5, pady=5, sticky=E)
        self.materiaVar = StringVar(value="Matemática")
        self.dropdownMateria = OptionMenu(self.frameFormulario, self.materiaVar, "Matemática", "Biología", "Química", "Lenguaje", "Inglés")
        self.dropdownMateria.config(bg=button_bg, fg=button_fg)
        self.dropdownMateria.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        #botón para agregar tarea dentro del formulario
        self.btnAgregar = Button(self.frameFormulario, text='agregar tarea', command=self.agregar_tarea, bg=button_bg, fg=button_fg)
        self.btnAgregar.grid(row=4, columnspan=2, pady=10)

        #contenedor para la lista de tareas y los botones
        self.frameLista = Frame(self.root, bg="#4d4d4d")
        self.frameLista.pack(pady=10, padx=10, fill="both", expand=True)

        #lista de tareas
        self.lista_tareas = Listbox(self.frameLista, bg=list_bg, fg=list_fg)
        self.lista_tareas.pack(side=LEFT, fill="both", expand=True)

        #contenedor para los botones de acciones
        self.frameBotones = Frame(self.frameLista, bg="#4d4d4d")
        self.frameBotones.pack(side=RIGHT, padx=10)

        #botón para cambiar el estado de la tarea
        self.btnCambiarEstado = Button(self.frameBotones, text='cambiar estado', command=self.cambiar_estado_tarea, bg=button_bg, fg=button_fg)
        self.btnCambiarEstado.pack(pady=5)

        #botón para eliminar tarea
        self.btnEliminar = Button(self.frameBotones, text='eliminar tarea', command=self.eliminar_tarea, bg=button_bg, fg=button_fg)
        self.btnEliminar.pack(pady=5)

    def agregar_tarea(self):
        #obtener datos del formulario
        nombre = self.entryNombre.get()
        descripcion = "" 
        fecha_vencimiento = self.entryFecha.get()
        estado = self.estadoVar.get()
        materia = self.materiaVar.get()
        #agregar tarea
        self.controlador.agregar_tarea(nombre, descripcion, fecha_vencimiento, estado, materia)
        self.actualizar_lista_tareas()

    def eliminar_tarea(self):
        #eliminar tarea seleccionada con el cursor
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            tarea_index = seleccion[0]
            self.controlador.eliminar_tarea(tarea_index)
            self.actualizar_lista_tareas()
        else:
            messagebox.showwarning("advertencia", "seleccione una tarea para eliminar")

    def cambiar_estado_tarea(self):
        #cambiar el estado de la tarea seleccionada
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            tarea_index = seleccion[0]
            self.controlador.cambiar_estado_tarea(tarea_index)
            self.actualizar_lista_tareas()
        else:
            messagebox.showwarning("advertencia", "seleccione una tarea para cambiar el estado")  # alerta si no se selecciona una tarea

    #actualiza toda la lista según los datos dados
    def actualizar_lista_tareas(self):
        self.lista_tareas.delete(0, END)
        for tarea in self.controlador.listar_tareas():
            self.lista_tareas.insert(END, f"{tarea.nombre} - {tarea.fecha_vencimiento} - {tarea.estado} - {tarea.mostrar_materia()}")
