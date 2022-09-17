"""
decorators.py:
    Módulo que contiene la lógica de los decoradores para las funciones 'Create', 'Update' y 'Delete'
    del 'model.py'.
    Además, permite realizar un logging a un archivo 'log.txt' dónde se guardan los eventos de las 
    funciones mencionadas, cuando sea crea, actualiza o borra un registro, dejando en dicho .txt la
    fecha y la hora del evento.
"""
__author__ = "Paula Jesica Vergara De Castro"
__maintrainer__ = "Juan Barreto"
__email__ = "paulajve@gmail.com"
__copyright__ = "Copyright 2022"
__version__ = "1.1"

import datetime


def decorador_create(func_alta):
    def wrapper(*args, **kwargs):
        log = open("log.txt", "a")
        func_alta(*args, **kwargs)
        msg = str("Se ha agregado un registro a la base de datos.")
        log.write(msg + " " + str(datetime.datetime.now()) + "\n")
        log.close()
        print(msg)
        print("Alta OK")

    return wrapper


def decorador_update(func_actualizar):
    def wrapper(*args, **kwargs):
        print("Actualización OK")
        log = open("log.txt", "a")
        func_actualizar(*args, **kwargs)
        msg = str("Se ha actualizado un registro de la base de datos.")
        log.write(msg + " " + str(datetime.datetime.now()) + "\n")
        log.close()
        print(msg)

    return wrapper


def decorador_delete(func_borrar):
    def wrapper(*args, **kwargs):
        print("Borrado OK")
        log = open("log.txt", "a")
        func_borrar(*args, **kwargs)
        msg = str("Se ha borrado un registro de la base de datos.")
        log.write(msg + " " + str(datetime.datetime.now()) + "\n")
        log.close()
        print(msg)

    return wrapper
