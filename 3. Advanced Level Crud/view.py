"""
view.py:
    Módulo que contiene la interfaz gráfica de usuario (GUI) y define cómo se muestran los datos de la
    aplicación y cómo estos interactúan con el usuario. Actualiza los datos a través de configuradores y 
    controladores de eventos.
    Además, contiene información sobre el lanzamiento de la aplicación como cliente para conectarse y 
    enviar datos al servidor.
"""
__author__ = "Paula Jesica Vergara De Castro"
__maintrainer__ = "Juan Barreto"
__email__ = "paulajve@gmail.com"
__copyright__ = "Copyright 2022"
__version__ = "1.1"

from tkinter import Label
from tkinter import Frame
from tkinter import Entry
from tkinter import HORIZONTAL, VERTICAL, LEFT, RIGHT, BOTTOM, TOP, NO, W, Y, X, END
from tkinter import DISABLED
from tkinter import ttk
from tkinter import Button
from tkinter import Scrollbar
from tkcalendar import DateEntry
from tkinter import StringVar
import model
import os
import sys
import subprocess
import threading
from pathlib import Path

###esto es nuevo para el cliente
proceso = ""


class Panel:
    """La clase 'Panel' utiliza el método __init__ para iniciar los atributos de los objetos creados en
    el módulo 'vista.py'.
    Además, permite conectarse al archivo 'cliente.py' y devolver la comunicación con el servidor. Para
    ello se definieron las funciones 'try_connection' y 'lanzar_cliente'.

    :param window: ventana raíz de la interfaz gráfica.
    """

    def __init__(self, window):
        self.root = window
        self.mod_inst = model.Crud()

        ### Nueva línea cliente
        self.try_connection()
        ###

        # self.objeto_base = Crud()  # agregado UML
        try:
            self.mod_inst.conexion()
            self.mod_inst.create_table()

        except:
            print("Hay un error")

        # Configuración de la raíz

        self.root.title("Registro de CAR")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        width = 1300
        height = 630
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.root.resizable(0, 0)

        # ==================================VARIABLES==========================================

        self.TITLE = StringVar()
        self.EMISOR = StringVar()
        self.RECEPTOR = StringVar()
        self.AREA = StringVar()
        self.TIPOCAR = StringVar()
        self.RESPONSABLE = StringVar()
        self.GERENTE = StringVar()
        self.OCURRENCIA = StringVar()
        self.CONTENCION = StringVar()
        self.VENCIMIENTO = StringVar()
        self.DESVIO = StringVar()

        # ==================================FRAME==============================================

        # configurar el grid

        self.root.columnconfigure(0, weight=2)
        self.root.columnconfigure(1, weight=2)
        self.root.columnconfigure(3, weight=2)

        # ==TÍTULO DEL DESVÍO==
        self.title_frame = Frame(self.root, bd=2, relief="groove")
        self.title_frame.grid(
            column=0, row=0, sticky="ne", padx=5, pady=5, columnspan=2
        )

        # ==CAR#==
        self.car_number_frame = Frame(self.root, bd=2, relief="groove")
        self.car_number_frame.grid(column=2, row=0, sticky="w", padx=5, pady=5)

        # ==BUTTONS==
        self.box_buttons = Frame(self.root, bd=2, relief="groove")
        self.box_buttons.grid(column=2, sticky="nsew", padx=5, pady=5, rowspan=1)

        self.box_but_bot = Frame(self.root, bd=2, relief="groove")
        self.box_but_bot.grid(column=2, sticky="nsew", padx=5, pady=5, rowspan=1)

        # ==DATOS DE CARGA==
        self.who_frame = Frame(self.root, bd=2, relief="groove")
        self.who_frame.grid(column=0, row=1, sticky="new", padx=5, pady=5)

        # ==EQUIPO==
        self.team_frame = Frame(self.root, bd=2, relief="groove")
        self.team_frame.grid(column=0, row=2, sticky="new", padx=5, pady=5)

        # ==FECHAS==

        self.date_frame = Frame(self.root, bd=2, relief="groove")
        self.date_frame.grid(column=1, row=1, sticky="new", padx=5, pady=5)

        # ==DESCRIPCIÓN DEL DESVÍO==

        self.desvio_frame = Frame(self.root, width=20, height=20, bd=2, relief="groove")
        self.desvio_frame.grid(column=1, row=2, sticky="new", padx=5, pady=5)

        # ==LISTA DE DESVÍOS CARGADOS==

        self.bottom_list = Frame(
            self.root, width=300, height=250, bd=2, relief="groove"
        )
        self.bottom_list.grid(sticky="nsew", padx=5, pady=5, columnspan=3)

        # ==================================LABEL WIDGET=======================================

        # ==TÍTULO DEL DESVÍO==
        txt_title = Label(
            self.title_frame,
            width=20,
            font=("open sans", 14, "bold"),
            text="TÍTULO DEL DESVÍO:",
            anchor="w",
        )
        txt_title.grid(row=0, sticky="w", ipadx=5, padx=5)

        # ==CAR #==
        txt_car_number_frame = Label(
            self.car_number_frame,
            width=20,
            font=("open sans", 14, "bold"),
            text="REGISTRO DE CAR",
            anchor="n",
            bg="midnightblue",
            fg="seashell2",
        )
        txt_car_number_frame.grid(row=0, sticky="w")

        # ==BUTTONS==
        txt_box_buttons = Label(
            self.box_buttons,
            width=20,
            font=("open sans", 14, "bold"),
            text="GESTIÓN DE CAR",
        )
        txt_box_buttons.pack()

        txt_box_but_bottom = Label(
            self.box_but_bot,
            width=20,
            font=("open sans", 14, "bold"),
            text="MENÚ DE APLICACIÓN",
        )
        txt_box_but_bottom.pack()

        # txt_result = Label(self.box_buttons)
        # txt_result.pack(side=TOP)

        # ==DATOS DE CARGA==
        txt_who_frame = Label(
            self.who_frame, text="DATOS DE CARGA:", font=("open sans", 14, "bold")
        )
        txt_who_frame.grid(row=1, sticky="e")
        txt_emisor = Label(self.who_frame, text="Emisor:", font=("arial", 14), bd=5)
        txt_emisor.grid(row=3, sticky="e")
        txt_receptor = Label(self.who_frame, text="Receptor:", font=("arial", 14), bd=5)
        txt_receptor.grid(row=4, sticky="e")
        txt_area = Label(self.who_frame, text="Área:", font=("arial", 14), bd=5)
        txt_area.grid(row=5, sticky="e")
        txt_tipocar = Label(
            self.who_frame, text="Tipo de CAR:", font=("arial", 14), bd=5
        )
        txt_tipocar.grid(row=6, sticky="e")

        # ==EQUIPO==
        txt_team_frame = Label(
            self.team_frame, text="DATOS DE EQUIPO:", font=("open sans", 14, "bold")
        )
        txt_team_frame.grid(row=1, sticky="e")
        txt_responsable = Label(
            self.team_frame, text="Responsable:", font=("arial", 14), bd=5
        )
        txt_responsable.grid(row=3, sticky="e")
        txt_gerente = Label(self.team_frame, text="Gerente:", font=("arial", 14), bd=5)
        txt_gerente.grid(row=4, sticky="e")

        # ==FECHAS==
        txt_date_frame = Label(
            self.date_frame, text="FECHAS:", font=("open sans", 14, "bold")
        )
        txt_date_frame.grid(row=1, sticky="w")
        txt_ocurrencia = Label(
            self.date_frame, text="Ocurrencia:", font=("arial", 14), bd=5
        )
        txt_ocurrencia.grid(row=2, sticky="e")
        txt_contencion = Label(
            self.date_frame, text="Contención:", font=("arial", 14), bd=5
        )
        txt_contencion.grid(row=3, sticky="e")
        txt_vencimiento = Label(
            self.date_frame, text="Vencimiento:", font=("arial", 14), bd=5
        )
        txt_vencimiento.grid(row=4, sticky="e")

        # ==DESCRIPCIÓN DEL DESVÍO==
        txt_desvio_desc = Label(
            self.desvio_frame,
            text="DESCRIPCIÓN DEL DESVÍO:",
            font=("open sans", 14, "bold"),
            bd=5,
        )
        txt_desvio_desc.grid(sticky="w", pady=4, padx=5)

        # ==================================ENTRY WIDGET=======================================

        # ==TÍTULO DEL DESVÍO==

        self.title_entry = Entry(
            self.title_frame,
            textvariable=self.TITLE,
            width=128,
        )
        self.title_entry.grid(row=0, padx=220, pady=5)

        # ==DATOS DE CARGA==
        self.emisor = Entry(self.who_frame, textvariable=self.EMISOR, width=55)
        self.emisor.grid(row=3, column=1)
        self.receptor = Entry(self.who_frame, textvariable=self.RECEPTOR, width=55)
        self.receptor.grid(row=4, column=1)
        self.area = Entry(self.who_frame, textvariable=self.AREA, width=55)
        self.area.grid(row=5, column=1)
        self.tipocar = Entry(self.who_frame, textvariable=self.TIPOCAR, width=55)
        self.tipocar.grid(row=6, column=1)

        # ==EQUIPO==
        self.responsable = Entry(
            self.team_frame, textvariable=self.RESPONSABLE, width=55
        )
        self.responsable.grid(row=3, column=1)
        self.gerente = Entry(self.team_frame, textvariable=self.GERENTE, width=55)
        self.gerente.grid(row=4, column=1)

        # ==FECHAS==

        self.ocurrencia = DateEntry(
            self.date_frame,
            textvariable=self.OCURRENCIA,
            width=30,
            year=2022,
            date_pattern="dd/mm/yy",
        )

        self.ocurrencia.grid(row=2, column=1)
        self.contencion = DateEntry(
            self.date_frame,
            textvariable=self.CONTENCION,
            width=30,
            year=2022,
            date_pattern="dd/mm/yy",
        )
        self.contencion.grid(row=3, column=1)
        self.vencimiento = DateEntry(
            self.date_frame,
            textvariable=self.VENCIMIENTO,
            width=30,
            year=2022,
            date_pattern="dd/mm/yy",
        )
        self.vencimiento.grid(row=4, column=1)

        # ==DESCRIPCIÓN DEL DESVÍO==
        self.desvio = Entry(self.desvio_frame, textvariable=self.DESVIO, width=50)
        self.desvio.grid(row=4, column=0, padx="5", pady=5, ipadx=60, ipady=40)

        # ==================================BUTTONS WIDGET=====================================

        """
        self.btn_cliente = Button(
            self.box_but_bot,
            width=15,
            font=("arial", 14),
            text="Conectar Cliente",
            command=lambda: self.try_connection(),
        )
        self.btn_cliente.pack(side=TOP)
        
        """

        btn_clean = Button(
            self.box_but_bot,
            width=15,
            font=("arial", 14),
            text="Limpiar campos",
            command=lambda: self.mod_inst.clean_fields(
                self.TITLE.set(""),
                self.EMISOR.set(""),
                self.RECEPTOR.set(""),
                self.AREA.set(""),
                self.TIPOCAR.set(""),
                self.RESPONSABLE.set(""),
                self.GERENTE.set(""),
                self.OCURRENCIA.set(""),
                self.CONTENCION.set(""),
                self.VENCIMIENTO.set(""),
                self.DESVIO.set(""),
            ),
        )
        btn_clean.pack(side=TOP)

        btn_create = Button(
            self.box_buttons,
            width=10,
            font=("arial", 14),
            text="Crear",
            command=lambda: [
                self.mod_inst.create(
                    self.TITLE.get(),
                    self.EMISOR.get(),
                    self.RECEPTOR.get(),
                    self.AREA.get(),
                    self.TIPOCAR.get(),
                    self.RESPONSABLE.get(),
                    self.GERENTE.get(),
                    self.OCURRENCIA.get(),
                    self.CONTENCION.get(),
                    self.VENCIMIENTO.get(),
                    self.DESVIO.get(),
                ),
                self.mod_inst.read(self.my_tree),
            ],
        )
        btn_create.pack(side=TOP)

        btn_read = Button(
            self.box_but_bot,
            width=10,
            font=("arial", 14),
            text="Leer",
            command=lambda: self.mod_inst.read(self.my_tree),
        )
        btn_read.pack(side=TOP)

        btn_update = Button(
            self.box_buttons,
            width=10,
            font=("arial", 14),
            text="Actualizar",
            # state=DISABLED,
            command=lambda: [
                self.mod_inst.update(
                    self.TITLE.get(),
                    self.EMISOR.get(),
                    self.RECEPTOR.get(),
                    self.AREA.get(),
                    self.TIPOCAR.get(),
                    self.RESPONSABLE.get(),
                    self.GERENTE.get(),
                    self.OCURRENCIA.get(),
                    self.CONTENCION.get(),
                    self.VENCIMIENTO.get(),
                    self.DESVIO.get(),
                    reg_id,
                    self.my_tree,
                ),
                self.mod_inst.read(self.my_tree),
            ],
        )
        btn_update.pack(side=TOP)

        btn_delete = Button(
            self.box_buttons,
            width=10,
            font=("arial", 14),
            text="Borrar",
            command=lambda: self.mod_inst.delete(self.my_tree),
        )
        btn_delete.pack(side=TOP)

        btn_exit = Button(
            self.box_but_bot,
            width=10,
            font=("arial", 14),
            text="Salir",
            command=lambda: self.mod_inst.exit(self.my_tree),
        )
        btn_exit.pack(side=TOP)

        # ==================================TREEVIEW WIDGET========================================

        # == ESTILO DEL TREEVIEW ==#

        style = ttk.Style()

        # Elegir Theme
        style.theme_use("clam")

        # Color del Treeview
        style.configure(
            "Treeview",
            background="silver",
            foreground="black",
            rowheight=25,
            fieldbackground="silver",
        )
        style.map("Treeview", background=[("selected", "midnightblue")])

        # ==TREEVIEW DE DESVÍOS CARGADOS==

        scrollbary = Scrollbar(self.bottom_list, orient=VERTICAL)
        scrollbarx = Scrollbar(self.bottom_list, orient=HORIZONTAL)

        self.my_tree = ttk.Treeview(
            self.bottom_list,
            columns=(
                "car_number",
                "title",
                "emisor",
                "receptor",
                "area",
                "tipocar",
                "responsable",
                "gerente",
                "ocurrencia",
                "contencion",
                "vencimiento",
                "desvio",
            ),
            selectmode="extended",
            height=7,
            yscrollcommand=scrollbary.set,
            xscrollcommand=scrollbarx.set,
        )
        scrollbary.config(command=self.my_tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=self.my_tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        self.my_tree.heading("car_number", text="CAR #", anchor=W)
        self.my_tree.heading("title", text="Título", anchor=W)
        self.my_tree.heading("emisor", text="Emisor", anchor=W)
        self.my_tree.heading("receptor", text="Receptor", anchor=W)
        self.my_tree.heading("area", text="Área", anchor=W)
        self.my_tree.heading("tipocar", text="Tipo CAR", anchor=W)
        self.my_tree.heading("responsable", text="Responsable", anchor=W)
        self.my_tree.heading("gerente", text="Gerente", anchor=W)
        self.my_tree.heading("ocurrencia", text="Ocur.", anchor=W)
        self.my_tree.heading("contencion", text="Cont.", anchor=W)
        self.my_tree.heading("vencimiento", text="Venc.", anchor=W)
        self.my_tree.heading("desvio", text="Descripción", anchor=W)
        self.my_tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.my_tree.column("#1", stretch=NO, minwidth=0, width=50)
        self.my_tree.column("#2", stretch=NO, minwidth=0, width=120)
        self.my_tree.column("#3", stretch=NO, minwidth=0, width=120)
        self.my_tree.column("#4", stretch=NO, minwidth=0, width=120)
        self.my_tree.column("#5", stretch=NO, minwidth=0, width=120)
        self.my_tree.column("#6", stretch=NO, minwidth=0, width=120)
        self.my_tree.column("#7", stretch=NO, minwidth=0, width=120)
        self.my_tree.column("#8", stretch=NO, minwidth=0, width=120)
        self.my_tree.column("#9", stretch=NO, minwidth=0, width=60)
        self.my_tree.column("#10", stretch=NO, minwidth=0, width=60)
        self.my_tree.column("#11", stretch=NO, minwidth=0, width=60)
        self.my_tree.column("#12", stretch=NO, minwidth=0, width=420)
        self.my_tree.pack()

        self.mod_inst.read(self.my_tree)

        # Bindings

        self.my_tree.bind(
            "<Double-Button-1>", lambda event: on_selected(self.my_tree, event)
        )

        def on_selected(my_tree, event):
            global reg_id
            curItem = self.my_tree.focus()
            contents = self.my_tree.item(curItem)
            selecteditem = contents["values"]
            reg_id = selecteditem[0]
            for value in self.my_tree.item(curItem)["values"]:
                print(value)

            print("fila seleccionada")

            self.title_entry.delete(0, END)
            self.title_entry.insert(0, selecteditem[1])

            self.emisor.delete(0, END)
            self.emisor.insert(0, selecteditem[2])

            self.receptor.delete(0, END)
            self.receptor.insert(0, selecteditem[3])

            self.area.delete(0, END)
            self.area.insert(0, selecteditem[4])

            self.tipocar.delete(0, END)
            self.tipocar.insert(0, selecteditem[5])

            self.responsable.delete(0, END)
            self.responsable.insert(0, selecteditem[6])

            self.gerente.delete(0, END)
            self.gerente.insert(0, selecteditem[7])

            self.ocurrencia.delete(0, END)
            self.ocurrencia.insert(0, selecteditem[8])

            self.contencion.delete(0, END)
            self.contencion.insert(0, selecteditem[9])

            self.vencimiento.delete(0, END)
            self.vencimiento.insert(0, selecteditem[10])

            self.desvio.delete(0, END)
            self.desvio.insert(0, selecteditem[11])

        ### esto es nuevo para el cliente

    def try_connection(self):
        global proceso  # agregado
        if proceso != "":
            proceso.kill()
            threading.Thread(
                target=self.lanzar_cliente, args=(True,), daemon=True
            ).start()
        else:
            threading.Thread(
                target=self.lanzar_cliente, args=(True,), daemon=True
            ).start()

    def lanzar_cliente(self, var):
        self.run_cliente()

    def run_cliente(self):
        os.system('python "cliente.py"')
