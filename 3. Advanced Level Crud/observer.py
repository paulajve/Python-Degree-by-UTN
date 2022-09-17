"""
observer.py:
    Módulo que contiene la lógica del modelo Observador (UML).
"""
__author__ = "Paula Jesica Vergara De Castro"
__maintrainer__ = "Juan Barreto"
__email__ = "paulajve@gmail.com"
__copyright__ = "Copyright 2022"
__version__ = "1.1"


class Subject:
    """Se define la clase 'Subject' para agregar, quitar y notificar observadores.

    :param obj: objeto del observador.

    """

    observadores = []

    def agregar(self, obj):
        self.observadores.append(obj)

    def quitar(self, obj):
        pass

    def notificar(self, *args):
        for observador in self.observadores:
            observador.update(args)


class Observer:
    """Se define la clase 'Observer' para permitir la delegación de las actualizaciones."""

    def update(self):
        raise NotImplementedError("Delegación de actualización")


class ConcreteObserverA(Observer):
    """Se define la clase 'ConcreteObserverA' para permitir que este observador muestre los
    parámetros de las actualizaciones.
    """

    def __init__(self, obj):
        self.observado_a = obj
        self.observado_a.agregar(self)

    def update(self, *args):
        print("Actualización dentro de Observador ConcreteObserverA")
        print("Aquí están los parámetros: ", args)
