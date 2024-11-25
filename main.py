from tkinter import Tk
from controlador.controlador import Controlador
from vista.vista import Vista

def main():
    #crear la ventana principal de Tkinter
    root = Tk()
    
    #crear una instancia del controlador
    controlador = Controlador()
    
    #crear una instancia de la vista, pasándole la ventana principal y el controlador
    app = Vista(root, controlador)
    
    #iniciar el bucle principal de la aplicación
    root.mainloop()

if __name__ == "__main__":
    #si el archivo se ejecuta directamente, llama a la función main
    main()
