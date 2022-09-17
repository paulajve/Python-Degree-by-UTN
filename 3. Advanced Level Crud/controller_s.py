"""
controller_s.py:
    Módulo que realiza la comunicación con el archivo 'view_s.py' del servidor. 
    Contiene la clase Controller y llama a la clase Panel del módulo vista que 
    crea la ventana principal de encendido y apagado del servidor.
"""
__author__ = "Paula Jesica Vergara De Castro"
__maintrainer__ = "Juan Barreto"
__email__ = "paulajve@gmail.com"
__copyright__ = "Copyright 2022"
__version__ = "1.1"

from tkinter import Tk
import view_s


class Controller:
    """Se define la clase 'Controller' y se utiliza el método '__init__' para iniciar los atributos
    de los objetos creados.

    :param root: base de la interfaz gráfica (raíz, contenedor base de los widgets que forman la interfaz).

    """

    def __init__(self, root):
        self.root_controller = root
        self.objeto_vista = view_s.InicioServidor(self.root_controller)


if __name__ == "__main__":
    root_tk = Tk()
    application = Controller(root_tk)
    root_tk.mainloop()
