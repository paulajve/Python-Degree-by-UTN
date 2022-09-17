from tkinter import *
from tkcalendar import Calendar, DateEntry
import tkinter as tk
from tkinter import ttk
import re
from re import T
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
from turtle import title


# Configuración de la raíz
root = Tk()
root.title("Registro de CAR")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 1300
height = 630
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

# ==================================METHODS============================================
def Database():
    global conn, cursor
    conn = sqlite3.connect("capa_cal.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `capareg` (reg_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, title TEXT, emisor TEXT, receptor TEXT, area TEXT, tipocar TEXT, responsable TEXT, gerente TEXT, ocurrencia DATE, contencion DATE, vencimiento DATE, desvio TEXT)"
    )


def Create():
    if (
        TITLE.get() == ""
        or EMISOR.get() == ""
        or RECEPTOR.get() == ""
        or AREA.get() == ""
        or TIPOCAR.get() == ""
        or RESPONSABLE.get() == ""
        or GERENTE.get() == ""
        or OCURRENCIA.get() == ""
        or CONTENCION.get() == ""
        or VENCIMIENTO.get() == ""
        or DESVIO.get() == ""
    ):
        txt_result.config(text="Por favor complete los campos requeridos!", fg="red")
    else:
        Database()
        cursor.execute(
            "INSERT INTO `capareg` (title, emisor, receptor, area, tipocar, responsable, gerente, ocurrencia, contencion, vencimiento, desvio) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                str(TITLE.get()),
                str(EMISOR.get()),
                str(RECEPTOR.get()),
                str(AREA.get()),
                str(TIPOCAR.get()),
                str(RESPONSABLE.get()),
                str(GERENTE.get()),
                str(OCURRENCIA.get()),
                str(CONTENCION.get()),
                str(VENCIMIENTO.get()),
                str(DESVIO.get()),
            ),
        )
    tree.delete(*tree.get_children())
    cursor.execute("SELECT * FROM `capareg` ORDER BY `reg_id` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert(
            "",
            "end",
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
        )
    conn.commit()
    TITLE.set("")
    EMISOR.set("")
    RECEPTOR.set("")
    AREA.set("")
    TIPOCAR.set("")
    RESPONSABLE.set("")
    GERENTE.set("")
    OCURRENCIA.set("")
    CONTENCION.set("")
    VENCIMIENTO.set("")
    DESVIO.set("")
    cursor.close()
    conn.close()
    txt_result.config(text="Reporte CAR creado!", fg="green")


def Read():
    tree.delete(*tree.get_children())
    Database()
    cursor.execute("SELECT * FROM `capareg` ORDER BY `reg_id` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert(
            "",
            "end",
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
        )
    cursor.close()
    conn.close()
    txt_result.config(text="Información leída exitosamente", fg="black")


def Update():
    Database()
    tree.delete(*tree.get_children())
    cursor.execute(
        "UPDATE `capareg` SET `title` = ?, `emisor` = ?, `receptor` = ?, `area` =?,  `tipocar` = ?,  `responsable` = ?, `gerente` = ?, `ocurrencia` = ?, `contencion` = ?, `vencimiento` = ?, `desvio` = ? WHERE `reg_id` = ?",
        (
            str(TITLE.get()),
            str(EMISOR.get()),
            str(RECEPTOR.get()),
            str(AREA.get()),
            str(TIPOCAR.get()),
            str(RESPONSABLE.get()),
            str(GERENTE.get()),
            str(OCURRENCIA.get()),
            str(CONTENCION.get()),
            str(VENCIMIENTO.get()),
            str(DESVIO.get()),
            int(reg_id),
        ),
    )
    conn.commit()
    cursor.execute("SELECT * FROM `capareg` ORDER BY `reg_id` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert(
            "",
            "end",
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
        )
        cursor.close()
        conn.close()
        TITLE.set("")
        EMISOR.set("")
        RECEPTOR.set("")
        AREA.set("")
        TIPOCAR.set("")
        RESPONSABLE.set("")
        GERENTE.set("")
        OCURRENCIA.set("")
        CONTENCION.set("")
        VENCIMIENTO.set("")
        DESVIO.set("")
        btn_create.config(state=NORMAL)
        btn_read.config(state=NORMAL)
        btn_update.config(state=DISABLED)
        btn_delete.config(state=NORMAL)
        txt_result.config(text="Actualización realizada con éxito", fg="black")


def OnSelected(event):
    global reg_id
    curItem = tree.focus()
    contents = tree.item(curItem)
    selecteditem = contents["values"]
    reg_id = selecteditem[0]
    TITLE.set("")
    EMISOR.set("")
    RECEPTOR.set("")
    AREA.set("")
    TIPOCAR.set("")
    RESPONSABLE.set("")
    GERENTE.set("")
    OCURRENCIA.set("")
    CONTENCION.set("")
    VENCIMIENTO.set("")
    DESVIO.set("")
    TITLE.set(selecteditem[1])
    EMISOR.set(selecteditem[2])
    RECEPTOR.set(selecteditem[3])
    AREA.set(selecteditem[4])
    TIPOCAR.set(selecteditem[5])
    RESPONSABLE.set(selecteditem[6])
    GERENTE.set(selecteditem[7])
    OCURRENCIA.set(selecteditem[8])
    CONTENCION.set(selecteditem[9])
    VENCIMIENTO.set(selecteditem[10])
    DESVIO.set(selecteditem[11])
    btn_create.config(state=DISABLED)
    btn_read.config(state=DISABLED)
    btn_update.config(state=NORMAL)
    btn_delete.config(state=DISABLED)


def Delete():
    if not tree.selection():
        txt_result.config(text="Por favor, seleccione un item primero", fg="red")
    else:
        result = tkMessageBox.askquestion(
            "Registro de CAR",
            "Está seguro que quiere borrar este elemento?",
            icon="warning",
        )
        if result == "yes":
            curItem = tree.focus()
            contents = tree.item(curItem)
            selecteditem = contents["values"]
            tree.delete(curItem)
            Database()
            cursor.execute(
                "DELETE FROM `capareg` WHERE `reg_id` = %d" % selecteditem[0]
            )
            conn.commit()
            cursor.close()
            conn.close()
            txt_result.config(text="Elemento borrado exitosamente", fg="black")


def Exit():
    result = tkMessageBox.askquestion(
        "Registro de CAR",
        "Está seguro que quiere salir?",
        icon="warning",
    )
    if result == "yes":
        root.destroy()
        exit()


# ==================================VARIABLES==========================================
TITLE = StringVar()
EMISOR = StringVar()
RECEPTOR = StringVar()
AREA = StringVar()
TIPOCAR = StringVar()
RESPONSABLE = StringVar()
GERENTE = StringVar()
OCURRENCIA = StringVar()
CONTENCION = StringVar()
VENCIMIENTO = StringVar()
DESVIO = StringVar()

# ==================================FRAME==============================================

# configurar el grid

root.columnconfigure(0, weight=2)
root.columnconfigure(1, weight=2)
root.columnconfigure(3, weight=2)

# ==TÍTULO DEL DESVÍO==
title_frame = Frame(root, bd=2, relief="groove")
title_frame.grid(column=0, row=0, sticky="ne", padx=5, pady=5, columnspan=2)

# ==CAR#==
car_number_frame = Frame(root, bd=2, relief="groove")
car_number_frame.grid(column=2, row=0, sticky="w", padx=5, pady=5)

# ==BUTTONS==
box_buttons = Frame(root, bd=2, relief="groove")
box_buttons.grid(column=2, sticky="nsew", padx=5, pady=5, rowspan=3)

# ==DATOS DE CARGA==
who_frame = Frame(root, bd=2, relief="groove")
who_frame.grid(column=0, row=1, sticky="new", padx=5, pady=5)

# ==EQUIPO==
team_frame = Frame(root, bd=2, relief="groove")
team_frame.grid(column=0, row=2, sticky="new", padx=5, pady=5)

# ==FECHAS==

date_frame = Frame(root, bd=2, relief="groove")
date_frame.grid(column=1, row=1, sticky="new", padx=5, pady=5)

# ==DESCRIPCIÓN DEL DESVÍO==

desvio_frame = Frame(root, width=20, height=20, bd=2, relief="groove")
desvio_frame.grid(column=1, row=2, sticky="new", padx=5, pady=5)

# ==LISTA DE DESVÍOS CARGADOS==

bottom_list = Frame(root, width=300, height=250, bd=2, relief="groove")
bottom_list.grid(sticky="nsew", padx=5, pady=5, columnspan=3)

# ==================================LABEL WIDGET=======================================

# ==TÍTULO DEL DESVÍO==
txt_title = Label(
    title_frame,
    width=20,
    font=("open sans", 14, "bold"),
    text="TÍTULO DEL DESVÍO:",
    anchor="w",
)
txt_title.grid(row=0, sticky="w", ipadx=5, padx=5)

# ==CAR #==
txt_car_number_frame = Label(
    car_number_frame,
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
    box_buttons, width=20, font=("open sans", 14, "bold"), text="MENÚ"
)
txt_box_buttons.pack()
txt_result = Label(box_buttons)
txt_result.pack(side=TOP)

# ==DATOS DE CARGA==

txt_who_frame = Label(who_frame, text="DATOS DE CARGA:", font=("open sans", 14, "bold"))
txt_who_frame.grid(row=1, sticky="e")
txt_emisor = Label(who_frame, text="Emisor:", font=("arial", 14), bd=5)
txt_emisor.grid(row=3, sticky="e")
txt_receptor = Label(who_frame, text="Receptor:", font=("arial", 14), bd=5)
txt_receptor.grid(row=4, sticky="e")
txt_area = Label(who_frame, text="Área:", font=("arial", 14), bd=5)
txt_area.grid(row=5, sticky="e")
txt_tipocar = Label(who_frame, text="Tipo de CAR:", font=("arial", 14), bd=5)
txt_tipocar.grid(row=6, sticky="e")

# ==EQUIPO==

txt_team_frame = Label(
    team_frame, text="DATOS DE EQUIPO:", font=("open sans", 14, "bold")
)
txt_team_frame.grid(row=1, sticky="e")
txt_responsable = Label(team_frame, text="Responsable:", font=("arial", 14), bd=5)
txt_responsable.grid(row=3, sticky="e")
txt_gerente = Label(team_frame, text="Gerente:", font=("arial", 14), bd=5)
txt_gerente.grid(row=4, sticky="e")

# ==FECHAS==

txt_date_frame = Label(date_frame, text="FECHAS:", font=("open sans", 14, "bold"))
txt_date_frame.grid(row=1, sticky="w")
txt_ocurrencia = Label(date_frame, text="Ocurrencia:", font=("arial", 14), bd=5)
txt_ocurrencia.grid(row=2, sticky="e")
txt_contencion = Label(date_frame, text="Contención:", font=("arial", 14), bd=5)
txt_contencion.grid(row=3, sticky="e")
txt_vencimiento = Label(date_frame, text="Vencimiento:", font=("arial", 14), bd=5)
txt_vencimiento.grid(row=4, sticky="e")

# ==DESCRIPCIÓN DEL DESVÍO==

txt_desvio_desc = Label(
    desvio_frame,
    text="DESCRIPCIÓN DEL DESVÍO:",
    font=("open sans", 14, "bold"),
    bd=5,
)
txt_desvio_desc.grid(sticky="w", pady=4, padx=5)

# txt_desvio = Text(desvio_frame, width=53, height=6)
# txt_desvio.grid(column=0, rowspan=2, pady=1, ipady=1)


# ==================================ENTRY WIDGET=======================================

# ==TÍTULO DEL DESVÍO==

title_entry = Entry(title_frame, textvariable=TITLE, width=128)
title_entry.grid(row=0, padx=220, pady=5)

# ==CAR#==

# car_number_frame_entry = Entry(car_number_frame, width=30)
# car_number_frame_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

# ==DATOS DE CARGA==

emisor = Entry(who_frame, textvariable=EMISOR, width=55)
emisor.grid(row=3, column=1)
receptor = Entry(who_frame, textvariable=RECEPTOR, width=55)
receptor.grid(row=4, column=1)
area = Entry(who_frame, textvariable=AREA, width=55)
area.grid(row=5, column=1)
tipocar = Entry(who_frame, textvariable=TIPOCAR, width=55)
tipocar.grid(row=6, column=1)

# ==EQUIPO==

responsable = Entry(team_frame, textvariable=RESPONSABLE, width=55)
responsable.grid(row=3, column=1)
gerente = Entry(team_frame, textvariable=GERENTE, width=55)
gerente.grid(row=4, column=1)

# ==FECHAS==

ocurrencia = DateEntry(
    date_frame, textvariable=OCURRENCIA, width=30, year=2022, date_pattern="dd/mm/yy"
)
ocurrencia.grid(row=2, column=1)
contencion = DateEntry(
    date_frame, textvariable=CONTENCION, width=30, year=2022, date_pattern="dd/mm/yy"
)
contencion.grid(row=3, column=1)
vencimiento = DateEntry(
    date_frame, textvariable=VENCIMIENTO, width=30, year=2022, date_pattern="dd/mm/yy"
)
vencimiento.grid(row=4, column=1)

# ==DESCRIPCIÓN DEL DESVÍO==

desvio = Entry(desvio_frame, textvariable=DESVIO, width=50)
desvio.grid(row=4, column=0, padx="5", pady=5, ipadx=60, ipady=40)

# ==================================BUTTONS WIDGET=====================================

# btn_lastid = Button(car_number_frame, width=10, text="CAR #", command=Lastid)

btn_create = Button(
    box_buttons, width=10, font=("arial", 14), text="Crear", command=Create
)
btn_create.pack(side=TOP)
btn_read = Button(box_buttons, width=10, font=("arial", 14), text="Leer", command=Read)
btn_read.pack(side=TOP)
btn_update = Button(
    box_buttons,
    width=10,
    font=("arial", 14),
    text="Actualizar",
    command=Update,
    state=DISABLED,
)
btn_update.pack(side=TOP)
btn_delete = Button(
    box_buttons, width=10, font=("arial", 14), text="Borrar", command=Delete
)
btn_delete.pack(side=TOP)
btn_exit = Button(box_buttons, width=10, font=("arial", 14), text="Salir", command=Exit)
btn_exit.pack(side=TOP)

# ==================================LIST WIDGET========================================

# ==LISTA DE DESVÍOS CARGADOS==
scrollbary = Scrollbar(bottom_list, orient=VERTICAL)
scrollbarx = Scrollbar(bottom_list, orient=HORIZONTAL)
tree = ttk.Treeview(
    bottom_list,
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
    height=9,
    yscrollcommand=scrollbary.set,
    xscrollcommand=scrollbarx.set,
)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading("car_number", text="CAR #", anchor=W)
tree.heading("title", text="Título", anchor=W)
tree.heading("emisor", text="Emisor", anchor=W)
tree.heading("receptor", text="Receptor", anchor=W)
tree.heading("area", text="Área", anchor=W)
tree.heading("tipocar", text="Tipo CAR", anchor=W)
tree.heading("responsable", text="Responsable", anchor=W)
tree.heading("gerente", text="Gerente", anchor=W)
tree.heading("ocurrencia", text="Ocur.", anchor=W)
tree.heading("contencion", text="Cont.", anchor=W)
tree.heading("vencimiento", text="Venc.", anchor=W)
tree.heading("desvio", text="Descripción", anchor=W)
tree.column("#0", stretch=NO, minwidth=0, width=0)
tree.column("#1", stretch=NO, minwidth=0, width=50)
tree.column("#2", stretch=NO, minwidth=0, width=120)
tree.column("#3", stretch=NO, minwidth=0, width=120)
tree.column("#4", stretch=NO, minwidth=0, width=120)
tree.column("#5", stretch=NO, minwidth=0, width=120)
tree.column("#6", stretch=NO, minwidth=0, width=120)
tree.column("#7", stretch=NO, minwidth=0, width=120)
tree.column("#8", stretch=NO, minwidth=0, width=120)
tree.column("#9", stretch=NO, minwidth=0, width=60)
tree.column("#10", stretch=NO, minwidth=0, width=60)
tree.column("#11", stretch=NO, minwidth=0, width=60)
tree.column("#12", stretch=NO, minwidth=0, width=420)
tree.pack()
tree.bind("<Double-Button-1>", OnSelected)


# ==================================INITIALIZATION=====================================
if __name__ == "__main__":
    root.mainloop()
