"""
view_s.py:
    Módulo de vista del servidor que contiene la clase InicioServidor, que 
    crea la ventana principal y permite el encendido y apagado del mismo. 
    A su vez, permite la conexión al 'controller.py' de la aplicación CRUD, 
    la cual funciona como cliente del servidor.

"""
__author__ = "Paula Jesica Vergara De Castro"
__maintrainer__ = "Juan Barreto"
__email__ = "paulajve@gmail.com"
__copyright__ = "Copyright 2022"
__version__ = "1.1"

from tkinter import Canvas
from tkinter import Label
from tkinter import Button
from tkinter import Frame
from tkinter import HORIZONTAL, VERTICAL, LEFT, RIGHT, BOTTOM, TOP, NO, W, Y, X, END
import os
import sys
from pathlib import Path
import subprocess
import threading
import tkinter as tk
from tkinter import ttk

proceso = ""


class InicioServidor:
    """Se define la clase Inicio_Servidor que utiliza el método __init__
    para iniciar los objetos de la ventana principal del servidor.
    Se define encendido y apagado del servidor. Además, posee definido
    un llamado a la Aplicación CRUD que funciona como cliente.

    :param window: ventana de la interfaz gráfica.

    """

    def __init__(self, window):
        self.root = window
        self.root.title("Conexión a Servidor y Aplicación Cliente")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        width = 300
        height = 250
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.root.resizable(0, 0)
        self.root.columnconfigure(0, weight=2)
        self.root.columnconfigure(1, weight=2)
        self.root.columnconfigure(3, weight=2)

        self.raiz = Path(__file__).resolve().parent
        self.ruta_server = os.path.join(self.raiz, "src", "servidor", "udp_server_t.py")

        self.title_frame = Frame(self.root, bd=2, relief="groove")
        self.title_frame.grid(column=0, row=0, sticky="n", padx=5, pady=5, columnspan=4)

        self.titulo = Label(
            self.title_frame,
            width=20,
            font=("open sans", 14, "bold"),
            text="Seleccionar Opción",
            anchor="n",
        )
        self.titulo.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky="w")

        self.box_buttons = Frame(self.root, bd=2, relief="groove")
        self.box_buttons.grid(column=2, sticky="nsew", padx=5, pady=5, rowspan=1)

        self.box_but_bot = Frame(self.root, bd=2, relief="groove")
        self.box_but_bot.grid(column=2, sticky="nsew", padx=5, pady=5, rowspan=1)

        self.boton_encender = Button(
            self.box_buttons,
            width=10,
            font=("arial", 14),
            text="Encender",
            command=lambda: self.try_connection(),
        )
        self.boton_encender.pack(side=TOP)

        self.boton_apagar = Button(
            self.box_buttons,
            width=10,
            font=("arial", 14),
            text="Apagar",
            command=lambda: self.stop_server(),
        )
        self.boton_apagar.pack(side=TOP)

        self.boton_app = Button(
            self.box_but_bot,
            width=25,
            font=("arial", 14),
            text="Abrir Aplicación CRUD",
            command=lambda: self.run(),
        )
        self.boton_app.pack(side=TOP)

        self.cvs = Canvas(
            self.box_buttons,
            width=30,
            height=30,
            borderwidth=0,
            highlightthickness=0,
            relief="ridge",
        )
        self.luz = self.cvs.create_oval(5, 5, 20, 20, fill="white", tags="luz")
        self.cvs.tag_bind("luz", "<1>")
        self.cvs.pack(side=TOP)

    def try_connection(
        self,
    ):
        if proceso != "":
            proceso.kill()
            threading.Thread(
                target=self.lanzar_servidor, args=(True,), daemon=True
            ).start()
        else:
            threading.Thread(
                target=self.lanzar_servidor, args=(True,), daemon=True
            ).start()

    def lanzar_servidor(self, var):
        the_path = self.ruta_server
        if var is True:
            global proceso
            proceso = subprocess.Popen([sys.executable, the_path])
            proceso.communicate()
            self.cvs.itemconfigure(self.luz, fill="green")
            # print("Servidor encendido correctamente.")
        else:
            print("")

    def run(self):
        os.system('python "controller.py"')

    def stop_server(
        self,
    ):
        global proceso
        if proceso != "":
            proceso.kill()
            self.cvs.itemconfigure(self.luz, fill="red")
            print("Servidor apagado correctamente.")
