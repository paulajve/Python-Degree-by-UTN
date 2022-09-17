"""
main.py:
    Módulo que corre la aplicación MVC invocando a 'controller.py' a través de 'os.system'.
"""
import os

__author__ = "Paula Jesica Vergara De Castro"
__maintrainer__ = "Juan Barreto"
__email__ = "paulajve@gmail.com"
__copyright__ = "Copyright 2022"
__version__ = "0.1"


def run_app(file):

    """
    :param file: Archivo a ejecutar con el comando 'os.system'.
    :returns: Inicializa el archivo 'controller.py'.
    """

    os.system(file)


run_app("python /utn/crud/p_sphinx/archivos/controller.py")
