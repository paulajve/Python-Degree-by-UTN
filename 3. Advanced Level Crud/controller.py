"""
controller.py:
    Módulo que realiza la comunicación entre los archivos 'view.py' y 'model.py' al momento que el usuario,
    mediante la ejecución de eventos definidos en el CRUD, solicita información a la aplicación. En síntesis,
    el 'controlador' es el cerebro que controla y decide cómo mostrar los datos, iniciando la 'vista' (view.py)
    y modificando el 'modelo' (model.py).
"""
__author__ = "Paula Jesica Vergara De Castro"
__maintrainer__ = "Juan Barreto"
__email__ = "paulajve@gmail.com"
__copyright__ = "Copyright 2022"
__version__ = "1.1"

from tkinter import Tk
import view
import observer


class Controlador:
    """Se define la clase 'Controlador' y se utiliza el método '__init__' para iniciar los atributos
    de los objetos creados. Además, introduce el patrón UML (patrón Observador).

    :param root_w: base de la interfaz gráfica (raíz, contenedor base de los widgets que forman la interfaz).

    """

    def __init__(self, root_w):
        """Método del constructor"""
        self.root = root_w
        self.view_object = view.Panel(self.root)
        self.el_observador = observer.ConcreteObserverA(
            self.view_object.mod_inst
        )  # línea agregada para patrón UML


if __name__ == "__main__":
    root_tk = Tk()
    my_app = Controlador(root_tk)
    root_tk.mainloop()
