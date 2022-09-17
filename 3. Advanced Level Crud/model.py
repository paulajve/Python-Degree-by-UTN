"""
model.py:
    Módulo que contiene la lógica de datos. Si el estado de los datos cambia, el modelo 'model.py' 
    notifica a la vista 'view.py' para que muestre los datos actualizados. Se implementan decoradores
    para las funciones principales de 'Create', 'Update' y 'Delete. Además, llama a la clase 'Subject'
    del archivo 'observer.py'.
"""
__author__ = "Paula Jesica Vergara De Castro"
__maintrainer__ = "Juan Barreto"
__email__ = "paulajve@gmail.com"
__copyright__ = "Copyright 2022"
__version__ = "1.1"

import tkinter.messagebox as tkMessageBox
import re
import sqlite3
import decorators
from observer import Subject


class Crud(Subject):
    """Se define la clase 'Crud' y se utiliza el método '__init__' para iniciar los atributos
    de los objetos creados.
    """

    def __init__(self):
        pass

    def conexion(self):
        """Se define una función llamada 'conexion' para que conecte y retorne, a través de sqlite3,
        la base de datos del CRUD.
        """
        conn = sqlite3.connect("capa_cal.db")
        return conn

    def create_table(self):
        """Se define una función 'create_table' para que en caso que la base de datos sql no exista, se cree
        una tabla con elementos definidos.
        """
        conn = self.conexion()
        cursor = conn.cursor()
        sql = "Create TABLE IF NOT EXISTS `capareg` (reg_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, title TEXT, emisor TEXT, receptor TEXT, area TEXT, tipocar TEXT, responsable TEXT, gerente TEXT, ocurrencia DATE, contencion DATE, vencimiento DATE, desvio TEXT)"
        cursor.execute(sql)
        conn.commit()
        print("Creación de Tabla OK")

    def clean_fields(
        self,
        title,
        emisor,
        receptor,
        area,
        tipocar,
        responsable,
        gerente,
        ocurrencia,
        contencion,
        vencimiento,
        desvio,
    ):
        """Se define una función auxiliar 'clean_fields' asociada al botón 'Limpiar Campos'. Al ejecutarse,
        permite que los campos 'Entry' del CRUD queden vacíos, para que el usuario pueda cargar un nuevo
        registro."""
        print("Limpieza de campos OK")

    def check_create(self, create):
        """Se define una función 'check_create' que utiliza Regular Expressions (Regex), para validar los
        caracteres ingresados en los campos Entry del CRUD. En esta aplicación y sólo a modo de muestra, se
        verifican los caracteres del Entry 'title' ('Título del desvío', en el GUI).
        En caso de ingresar caracteres no permitidos, el GUI mostrará una ventana de error con instrucciones
        para proceder.

        :param create: una función que permite tomar los elementos ingresados en los campos Entry del CRUD y guardarlos en la base de datos sql ya definida.
        """

        regex_create = r"\b[a-zA-Z -ÁáÉéÍíÓóÚúÑñ\u00f1\u00d1]*\b"
        if re.fullmatch(regex_create, create):
            return True
        else:
            tkMessageBox.showwarning(
                "ERROR",
                "Para el título, ingrese caracteres de la A a la Z y/o números del 0 al 9",
                icon="warning",
            )
        print("Título creado OK.")

    @decorators.decorador_create
    def create(
        self,
        title,
        emisor,
        receptor,
        area,
        tipocar,
        responsable,
        gerente,
        ocurrencia,
        contencion,
        vencimiento,
        desvio,
    ):
        """La función 'create' permite tomar los elementos ingresados en los campos Entry del CRUD por el
        usuario y guardarlos en la base de datos sql ya definida.

        :param title: elemento 'Título del Desvío' de la base de datos.
        :param emisor: elemento 'Emisor' de la base de datos.
        :param receptor: elemento 'Receptor' de la base de datos.
        :param area: elemento 'Área' de la base de datos.
        :param tipocar: elemento 'Tipo de CAR' de la base de datos.
        :param responsable: elemento 'Responsable' de la base de datos.
        :param gerente: elemento 'Gerente' de la base de datos.
        :param ocurrencia: elemento 'Fecha de Ocurrencia' de la base de datos.
        :param contencion: elemento 'Fecha de Contención' de la base de datos.
        :param vencimiento: elemento 'Fecha de Vencimiento' de la base de datos.
        :param desvio: elemento 'Descripción del Desvío' de la base de datos.

        """
        if self.check_create(title) is True:

            conn = self.conexion()
            cursor = conn.cursor()
            data = (
                title,
                emisor,
                receptor,
                area,
                tipocar,
                responsable,
                gerente,
                ocurrencia,
                contencion,
                vencimiento,
                desvio,
            )
            sql = "INSERT INTO `capareg` (title, emisor, receptor, area, tipocar, responsable, gerente, ocurrencia, contencion, vencimiento, desvio) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(sql, data)
            conn.commit()
            if cursor.execute(sql, data):
                tkMessageBox.showwarning(
                    "Carga exitosa",
                    "La información ha sido creada exitosamente.",
                    icon="warning",
                )
                """
                Llamo a la función notificar definida en observer.py
                """
                self.notificar(data)
            return conn

    def read(self, my_tree):
        """En una versión inicial de esta aplicación, la función 'read' sólo estaba asociada al botón 'Leer'
        del GUI y tenía una única funcionalidad: invocar los datos de la base de datos y mostrarlos en el
        Treeview del GUI si el usuario hacía click en el botón. En esta versión 0.1 la función 'read' permite:

        1. Mostrar los datos de la base de datos en el Treeview inmediatamente se corre la aplicación,
        sin hacer click en el botón 'Leer'.

        2. Al crear un nuevo registro en el CRUD, permite que la línea nueva creada se muestre automáticamente
        al final del Treeview sin tener que hacer click en el botón 'Leer'.

        3. Al actualizar un registro del CRUD, también muestra automáticamente la línea actualizada en el Treeview,
        sin hacer click en el botón 'Leer'.

        Independientemente de que el botón 'Leer' está asociado a la función 'read' y dado que 'read' se encuentra
        invocada dentro de otras funciones como 'create' y 'update' y no depende de este botón, se considera
        elimninar el botón 'Leer' en una versión posterior de esta aplicación. ya que el mismo puede considerarse
        innecesario. En esta versión, dicho botón permanece vigente sólo a modo demostrativo.

        :param my_tree: lista jerárquica de los elementos almacenados en la base de datos. Es invocada desde la vista y muestra estos datos con un formato de tabla.
        """

        my_tree.delete(*my_tree.get_children())
        conn = self.conexion()
        cursor = conn.cursor()
        sql = "SELECT * FROM `capareg` ORDER BY `reg_id` ASC"
        cursor.execute(sql)
        fetch = cursor.fetchall()
        my_tree.tag_configure("oddrow", background="white")
        my_tree.tag_configure("evenrow", background="lightblue")
        count = 0
        for data in fetch:
            if count % 2 == 0:
                my_tree.insert(
                    "",
                    "end",
                    iid=count,
                    values=(
                        data[0],
                        data[1],
                        data[2],
                        data[3],
                        data[4],
                        data[5],
                        data[6],
                        data[7],
                        data[8],
                        data[9],
                        data[10],
                        data[11],
                    ),
                    tags=("evenrow",),
                )
            else:
                my_tree.insert(
                    "",
                    "end",
                    iid=count,
                    values=(
                        data[0],
                        data[1],
                        data[2],
                        data[3],
                        data[4],
                        data[5],
                        data[6],
                        data[7],
                        data[8],
                        data[9],
                        data[10],
                        data[11],
                    ),
                    tags=("oddrow",),
                )
            count += 1
        cursor.close()
        conn.close()
        return conn

    @decorators.decorador_update
    def update(
        self,
        title,
        emisor,
        receptor,
        area,
        tipocar,
        responsable,
        gerente,
        ocurrencia,
        contencion,
        vencimiento,
        desvio,
        reg_id,
        my_tree,
    ):
        """La función 'update' permite actualizar una fila de la base de datos del CRUD y está asociada
        al botón 'Actualizar' del GUI. Para ello, es necesario seleccionar la fila del Treeview haciendo
        doble click sobre la misma y una vez que los campos se cargan en los Entry del CRUD, el usuario
        puede sobre-escribirlos y guardarlos en la misma fila dando click al botón 'Actualizar'.

        :param title: elemento 'Título del Desvío' de la base de datos.
        :param emisor: elemento 'Emisor' de la base de datos.
        :param receptor: elemento 'Receptor' de la base de datos.
        :param area: elemento 'Área' de la base de datos.
        :param tipocar: elemento 'Tipo de CAR' de la base de datos.
        :param responsable: elemento 'Responsable' de la base de datos.
        :param gerente: elemento 'Gerente' de la base de datos.
        :param ocurrencia: elemento 'Fecha de Ocurrencia' de la base de datos.
        :param contencion: elemento 'Fecha de Contención' de la base de datos.
        :param vencimiento: elemento 'Fecha de Vencimiento' de la base de datos.
        :param desvio: elemento 'Descripción del Desvío' de la base de datos.
        :param reg_id: identificador de registro del tipo integer que referencia cada fila de la base de datos.
        :param my_tree: lista jerárquica de los elementos almacenados en la base de datos. Es invocada desde la vista y muestra estos datos con un formato de tabla.
        """

        #### PARA SACAR PORQ SE PASÓ A DECORADOR

        if self.check_create(title) is True:
            my_tree.delete(*my_tree.get_children())
            conn = self.conexion()
            cursor = conn.cursor()  # para instanciar
            data = (
                title,
                emisor,
                receptor,
                area,
                tipocar,
                responsable,
                gerente,
                ocurrencia,
                contencion,
                vencimiento,
                desvio,
                reg_id,
            )
            sql = "UPDATE `capareg` SET `title` = ?, `emisor` = ?, `receptor` = ?, `area` =?,  `tipocar` = ?,  `responsable` = ?, `gerente` = ?, `ocurrencia` = ?, `contencion` = ?, `vencimiento` = ?, `desvio` = ? WHERE `reg_id` = ?"
            cursor.execute(sql, data)
            conn.commit()
            cursor.execute("SELECT * FROM `capareg` ORDER BY `reg_id` ASC")
            fetch = cursor.fetchall()
            for elemento in fetch:
                my_tree.insert(
                    "",
                    "end",
                    values=(
                        elemento[0],
                        elemento[1],
                        elemento[2],
                        elemento[3],
                        elemento[4],
                        elemento[5],
                        elemento[6],
                        elemento[7],
                        elemento[8],
                        elemento[9],
                        elemento[10],
                        elemento[11],
                    ),
                )
            if cursor.execute(sql, data):
                tkMessageBox.showwarning(
                    "¡Atención!",
                    "La actualización se realizó exitosamente.",
                    icon="warning",
                )
                self.notificar(data)
            cursor.close()
            conn.close()

    @decorators.decorador_delete
    def delete(self, my_tree):
        """La función 'delete' permite eliminar una fila de la base de datos al seleccionar determinada
        fila del Treeview. Esta función se encuentra asociada al botón 'Borrar', con lo cual la eliminación
        de datos se hace efectiva al hacer click sobre él.

        :param my_tree: lista jerárquica de los elementos almacenados en la base de datos. Es invocada desde la vista y muestra estos datos con un formato de tabla.
        """
        if not my_tree.selection():
            result = tkMessageBox.showwarning(
                "¡Atención!",
                "Por favor, seleccione un item primero",
                icon="warning",
            )
        else:
            result = tkMessageBox.askquestion(
                "Registro de CAR",
                "Está seguro que quiere borrar este elemento?",
                icon="warning",
            )
            if result == "yes":
                curItem = my_tree.focus()
                contents = my_tree.item(curItem)
                selecteditem = contents["values"]
                my_tree.delete(curItem)
                conn = self.conexion()
                cursor = conn.cursor()
                sql = "DELETE FROM `capareg` WHERE `reg_id` = %d" % selecteditem[0]
                cursor.execute(sql)
                if cursor.execute(sql):
                    tkMessageBox.showwarning(
                        "Borrado exitoso",
                        "Elemento borrado exitosamente",
                        icon="warning",
                    )
                    self.notificar(selecteditem)
                conn.commit()
                cursor.close()
                conn.close()

    def exit(self, root):
        """La función 'exit' se asocia al botón 'Salir' y permite cerrar la aplicación CRUD. Antes de efectuarse
        el cierre de la aplicación, emerge una ventana de decisión preguntando al usuario si desea salir.

        :param root: es una instancia de la clase Tk y es la ventana raíz donde se encuentran embebidos todos los widgets de la aplicación de tkinter.
        """
        result = tkMessageBox.askquestion(
            "Registro de CAR",
            "Está seguro que quiere salir?",
            icon="warning",
        )
        if result == "yes":

            # self.server_inst = cliente
            # print("Servidor cerrado.")
            root.destroy()
            exit()
