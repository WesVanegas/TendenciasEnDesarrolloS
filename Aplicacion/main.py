import os.path
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import datetime as dt


class Task:
    def __init__(self, ID, nombre, prioridad, fechaLimite, estado):
        self.ID = ID
        self.nombre = nombre
        self.prioridad = prioridad
        self.fechaLimite = fechaLimite
        self.estado = estado #Pendiente, En proceso, Terminada


tarea_0 = Task(1, "Tarea Inglés", "Media", "23/04/2023", "Pendiente")
tarea_1 = Task(2, "Tarea Tendencias", "ALta", "22/04/2023", "Pendiente")
tarea_2 = Task(3, "Sacar el perro", "Media", "21/04/2023", "Pendiente")
tarea_3 = Task(4, "Registrar CV", "Alta", "24/04/2023", "Pendiente")

listado=(tarea_0,tarea_1,tarea_2,tarea_3)

def creartask():
    id=entryId.get().strip()
    nombre = entryTarea.get()
    prioridad = entryPrioridad.get()
    fechaLimite = entryFecha.get()
    estado="Pendiente"
    l=[]
    for x in lista.get_children():
        l.append(str(lista.item(x)['values'][0]))
    if id in l:
        messagebox.showerror('Error', 'Ya se encuentra registrado el ID')
    elif id == '' or nombre == '' or prioridad == '' or fechaLimite == '':
        messagebox.showerror('error', 'No dejar campo en blanco')
    else:
        lista.insert('', 'end', text="1",values=(id, nombre, prioridad, fechaLimite, estado))
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


def deletetask():
    res = messagebox.askquestion('Advertencia', '¿Estas seguro de querer eliminar?')
    if res=='yes':
        x = lista.selection()[0]
        lista.delete(x)


def deleteall():
    res = messagebox.askquestion('Advertencia', '¿Estas seguro de querer eliminar Todo?')
    if res=='yes':
        for record in lista.get_children():
            lista.delete(record)


def selecttask():
    #limpiar
    clear()

    #Selecciona el numero de posicion
    selected = lista.focus()
    #Selecciona values
    values = lista.item(selected, 'values')

    #Muesta la informacion en los entry
    entryId.insert(0, values[0])
    entryTarea.insert(0, values[1])
    entryPrioridad.insert(0, values[2])
    entryFecha.insert(0, values[3])

    if (buttonUpdate['state']== tk.DISABLED):
        buttonUpdate['state'] = tk.NORMAL


def updatetask():
    # Selecciona el numero de posicion
    selected = lista.focus()
    # Actualizar datos
    lista.item(selected, text='', values=(entryId.get(), entryTarea.get(), entryPrioridad.get(), entryFecha.get(), 'Pendiente'))
    if (buttonUpdate['state']== tk.NORMAL):
        buttonUpdate['state'] = tk.DISABLED
    clear()



def cambiarEstado():
    """print(lista.selection()) #print id I001
    print(lista.item(lista.selection())) #print All
    print(lista.item(lista.selection())['values']) #print All values
    print(lista.item(lista.selection())['values'][1]) #print one value"""

    selected = lista.focus()
    temp = lista.item(selected, 'values')

    estado = lista.item(lista.selection())['values'][4]
    if estado == 'Pendiente':
        lista.item(selected, text='',
                   values=(temp[0], temp[1], temp[2], temp[3], 'En proceso'))
    elif estado == 'En proceso':
        lista.item(selected, text='',
                   values=(temp[0], temp[1], temp[2], temp[3], 'Terminada'))
    elif estado == 'Terminada':
        lista.item(selected, text='',
                   values=(temp[0], temp[1], temp[2], temp[3], 'Pendiente'))
    clear()


def exportar():
    contenido='\tLista de pendientes\n'
    treeview_children = lista.get_children()

    for info in treeview_children:
        contenido+=f"\n{lista.item(info)['values']}"

    ruta = './ListaPendientes.txt'
    archivo = open(ruta, 'w')
    archivo.write(contenido)
    archivo.close()

    ruta_absoluta=os.path.abspath(ruta)
    os.startfile(ruta_absoluta)


ventana = tk.Tk()
ventana.geometry('950x550')
ventana.title('Lista de que Hacer')
#ventana.configure(bg='blue')

#ventana['background']='#856ff8'
ventana['background']='lightcyan'

labeltitle = tk.Label(ventana, text='Agregar tareas', background='lightcyan')
labeltitle.pack(pady=5)

add_frame = Frame(ventana)
add_frame.pack(pady=5)
add_frame['background']='lightcyan'

labelId = tk.Label(add_frame, text='ID:', background='lightcyan')
labelId.grid(row=0, column=0)

entryId = tk.Entry(add_frame, width=30)
entryId.grid(row=1, column=0)

labelTarea = tk.Label(add_frame, text='Pendiente:', background='lightcyan')
labelTarea.grid(row=0, column=1)

entryTarea = tk.Entry(add_frame, width=30)
entryTarea.grid(row=1, column=1)

labelPrioridad = tk.Label(add_frame, text='Prioridad:', background='lightcyan')
labelPrioridad.grid(row=0, column=2)

entryPrioridad = tk.Entry(add_frame, width=30)
entryPrioridad.grid(row=1, column=2)

labelFecha = tk.Label(add_frame, text='Fecha', background='lightcyan')
labelFecha.grid(row=0, column=3)

entryFecha = tk.Entry(add_frame, width=30)
entryFecha.grid(row=1, column=3)

buttonAdd = tk.Button(ventana, text='Agregar', command=creartask, background='OliveDrab1')
buttonAdd.pack(pady=5)

"""buttonLimpiar = tk.Button(ventana, text='Limpiar', command=clear)
buttonLimpiar.pack(pady=10)"""

subTitle = tk.Label(ventana, text='Lista de tareas', background='lightcyan')
subTitle.pack(pady=5)

#Treeview Frame
lista_frame = Frame(ventana)
lista_frame.pack(pady=5)
lista_frame['background']='lightcyan'

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
lista.heading("# 5", text="Estado")

lista.pack(pady=5)

for task in listado:
    lista.insert('', 'end', text="1", values=(task.ID, task.nombre, task.prioridad, task.fechaLimite, task.estado))


date = dt.datetime.now()
# Create Label to display the Date
labelfechaahora = Label(ventana, text=f"{date:%A, %B %d, %Y}", font="Calibri, 10", background='lightcyan')
labelfechaahora.pack(pady=5)

"""state=tk.DISABLED"""
buttonSelect = tk.Button(ventana, text='Seleccionar', command=selecttask, background='plum1')
buttonSelect.pack(pady=5)

buttonCheck = tk.Button(ventana, text='Cambiar Estado', command=cambiarEstado, background='DarkOliveGreen1')
buttonCheck.pack(pady=5)

buttonUpdate = tk.Button(ventana, text='Editar', command=updatetask, state=tk.DISABLED, background='plum1')
buttonUpdate.pack(pady=5)

buttonDelete = tk.Button(ventana, text='Eliminar', command=deletetask, background='DarkOliveGreen1')
buttonDelete.pack(pady=5)

buttonDeleteAll = tk.Button(ventana, text='Eliminar todo', command=deleteall, background='plum1')
buttonDeleteAll.pack(pady=5)

buttonExport = tk.Button(ventana, text='Exportar', command=exportar, background='DarkOliveGreen1' )
buttonExport.pack(pady=5)


ventana.mainloop()