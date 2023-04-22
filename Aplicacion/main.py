import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox



class Task:
    def __init__(self, ID, nombre, prioridad, fechaLimite, hecha):
        self.ID = ID
        self.nombre = nombre
        self.prioridad = prioridad
        self.fechaLimite = fechaLimite
        self.hecha = hecha


tarea_0 = Task(1, "Tarea Inglés", "Media", "23/04/2023", False)
tarea_1 = Task(2, "Tarea Tendencias", "ALta", "22/04/2023", False)
tarea_2 = Task(3, "Sacar el perro", "Media", "21/04/2023", False)
tarea_3 = Task(4, "Registrar CV", "Alta", "24/04/2023", False)

listado=(tarea_0,tarea_1,tarea_2,tarea_3)





def creartask():
    id=entryId.get()
    nombre = entryTarea.get()
    prioridad = entryPrioridad.get()
    fechaLimite = entryFecha.get()
    hecha=False

    tarea = Task(id,nombre, prioridad, fechaLimite, hecha)
    #id=tarea.ID
    """listaTareas.append([tarea.nombre,tarea.prioridad, tarea.fechaLimite, tarea.hecha])
    lista.insert('', 'end', text="1", values=(tarea.id,tarea.nombre, tarea.prioridad, tarea.fechaLimite, tarea.hecha), idd=id)"""
    #lista.insert('','end', text="1", values=(entryId.get(), entryTarea.get(), entryPrioridad.get(), entryFecha.get(), hecha))
    lista.insert('', 'end', text="1",
                 values=(id, nombre, prioridad, fechaLimite, hecha))

    clear()

def clear():
    entryId.delete(0, END)
    entryTarea.delete(0, END)
    entryPrioridad.delete(0, END)
    entryFecha.delete(0, END)
    entryId.focus()

def showinfo():
    treeview_children = lista.get_children()
    for x in treeview_children:
        print(x)
        print(lista.item(x))


def eliminartask():
    x = lista.selection()[0]
    lista.delete(x)


def eliminartodo():
    for record in lista.get_children():
        lista.delete(record)


def selecttask():
    #limpiar
    entryId.delete(0, END)
    entryTarea.delete(0, END)
    entryPrioridad.delete(0, END)
    entryFecha.delete(0, END)

    #Selecciona el numero de posicion
    selected = lista.focus()
    #Selecciona values
    values = lista.item(selected, 'values')

    #Output to entry boxes
    entryId.insert(0, values[0])
    entryTarea.insert(0, values[1])
    entryPrioridad.insert(0, values[2])
    entryFecha.insert(0, values[3])

    if (buttonCheck['state'] == tk.DISABLED):
        buttonCheck['state'] = tk.NORMAL





def modificartask():
    # Selecciona el numero de posicion
    selected = lista.focus()
    # Actualizar datos
    lista.item(selected, text='', values=(entryId.get(), entryTarea.get(), entryPrioridad.get(), entryFecha.get(), False))
    clear()

def marcarhecho():
    # Selecciona el numero de posicion
    selected = lista.focus()
    lista.item(selected, text='',values=(entryId.get(), entryTarea.get(), entryPrioridad.get(), entryFecha.get(), True))
    clear()



ventana = tk.Tk()
ventana.geometry('950x600')
ventana.title('Lista de que Hacer')

labeltitle = tk.Label(ventana, text='Agregar tareas')
labeltitle.pack(pady=10)

add_frame = Frame(ventana)
add_frame.pack(pady=10)



labelId = tk.Label(add_frame, text='ID: ')
labelId.grid(row=0, column=0)
#labelId.pack()

entryId = tk.Entry(add_frame, width=30)
entryId.grid(row=1, column=0)
#entryId.pack()

labelTarea = tk.Label(add_frame, text='Pendiente: ')
labelTarea.grid(row=0, column=1)
#labelTarea.pack()

entryTarea = tk.Entry(add_frame, width=30)
entryTarea.grid(row=1, column=1)
#entryTarea.pack()

labelPrioridad = tk.Label(add_frame, text='Prioridad')
labelPrioridad.grid(row=0, column=2)
#labelPrioridad.pack()

entryPrioridad = tk.Entry(add_frame, width=30)
entryPrioridad.grid(row=1, column=2)
#entryPrioridad.pack()

labelFecha = tk.Label(add_frame, text='Fecha')
labelFecha.grid(row=0, column=3)
#labelFecha.pack()

entryFecha = tk.Entry(add_frame, width=30)
entryFecha.grid(row=1, column=3)
#entryFecha.pack()

buttonAdd = tk.Button(ventana, text='Agregar', command=creartask)
#buttonAdd.grid(row=3, column=1)
buttonAdd.pack(pady=10)

"""buttonLimpiar = tk.Button(ventana, text='Limpiar', command=clear)
buttonLimpiar.pack(pady=10)"""

subTitle = tk.Label(ventana, text='Lista de tareas')
#subTitle.grid(row=4, column=1)
subTitle.pack(pady=10)

#Treeview Frame
lista_frame = Frame(ventana)
lista_frame.pack(pady=10)

#Treeview Scrollbar
Scrollbar = ttk.Scrollbar(lista_frame)
Scrollbar.pack(side=RIGHT, fill=Y)

lista = ttk.Treeview(lista_frame, columns=("c1","c2","c3","c4","c5"), show='headings', height=5)

lista.configure(yscrollcommand=Scrollbar.set)
Scrollbar.config(command=lista.yview)

lista.column("# 1", anchor=CENTER, width=100)
lista.heading("# 1", text="ID")
lista.column("# 2", anchor=CENTER, width=100)
lista.heading("# 2", text="Nombre")
lista.column("# 3", anchor=CENTER, width=100)
lista.heading("# 3", text="Prioridad")
lista.column("# 4", anchor=CENTER, width=100)
lista.heading("# 4", text="FechaLimite")
lista.column("# 5", anchor=CENTER, width=100)
lista.heading("# 5", text="Hecho")

#lista.grid(row=5, column=1)
lista.pack(pady=10)

for task in listado:
    lista.insert('', 'end', text="1", values=(task.ID, task.nombre, task.prioridad, task.fechaLimite, task.hecha))

buttonCheck = tk.Button(ventana, text='Marcar Hecho', command=marcarhecho, state=tk.DISABLED)
#buttonCheck.grid(row=6, column=0)
buttonCheck.pack(pady=10)

buttonDelete = tk.Button(ventana, text='Eliminar', command=eliminartask)
#buttonDelete.grid(row=6, column=1)
buttonDelete.pack(pady=10)

buttonDeleteAll = tk.Button(ventana, text='Eliminar todo', command=eliminartodo)
buttonDeleteAll.pack(pady=10)

buttonSelect = tk.Button(ventana, text='Seleccionar', command=selecttask)
buttonSelect.pack(pady=10)

buttonUpdate = tk.Button(ventana, text='Editar', command=modificartask)
#buttonEdit.grid(row=6, column=2)
buttonUpdate.pack(pady=10)

"""buttonInfo = tk.Button(ventana, text='Informacion', command=showinfo)
#buttonInfo.grid(row=6, column=3)
buttonInfo.pack()"""

ventana.mainloop()