import os
import sys
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Grados C/F')

def celsius_fahrenheit():
    celsius = float(entrada.get())
    fahrenheit = celsius*9/5+32
    fahrenheit = round(fahrenheit, 1)
    label3.config(text=fahrenheit)

def fahrenheit_celsius():
    fahrenheit = float(entrada.get())
    celsius = (fahrenheit-32)*5/9
    celsius = round(celsius, 1)
    label4.config(text=celsius)


def exportararchivo():
    fahrenheit = str(label3.cget('text'))
    celsius = str(label4.cget('text'))
    contenido = f'Grados celsius ingresados {entrada.get()}'
    contenido += f'\n El equivalente a grados fahrenheit es:{fahrenheit}'
    contenido += f'\nGrados fahrenheit ingresados {entrada.get()}'
    contenido += f'\n El equivalente a grados celsius es:{celsius}'

    ruta = './covertidor_grados.txt'
    archivo = open(ruta, 'w')
    archivo.write(contenido)
    archivo.close()

    mensaje1 = 'Datos exportados'
    messagebox.showinfo('Mensaje informativo', mensaje1)

    #Abrir el archivo despues de exportarlo
    ruta_absoluta=os.path.abspath(ruta)
    os.startfile(ruta_absoluta)


ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)
ventana.columnconfigure(2, weight=1)
ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)
ventana.rowconfigure(2, weight=1)
ventana.rowconfigure(3, weight=1)
ventana.rowconfigure(4, weight=1)
ventana.rowconfigure(5, weight=1)

titulo = tk.Label(ventana, text="Convertidor de grados")
titulo.grid(row=0, column=1)

entrada = tk.Entry(ventana, width=20)
entrada.grid(row=1, column=1)

boton1 = tk.Button(ventana, text="Convetir a fahrenheit", command=celsius_fahrenheit)
boton1.grid(row=2, column=0)

boton2 = tk.Button(ventana, text="Convetir a Celsius", command=fahrenheit_celsius)
boton2.grid(row=2, column=1)

boton3 = tk.Button(ventana, text="Exportar", command=exportararchivo)
boton3.grid(row=2, column=2)

label1 = tk.Label(ventana, text="Conversion a Fahrenheit")
label1.grid(row=3, column=0)

label2 = tk.Label(ventana, text="Conversion a Celsius")
label2.grid(row=4, column=0)

label3 = tk.Label(ventana, text="")
label3.grid(row=3, column=1)

label4 = tk.Label(ventana, text="")
label4.grid(row=4, column=1)

for i in range(3):
    ventana.columnconfigure(i, weight=1, minsize=100)
for i in range(66):
    ventana.rowconfigure(i, weight=1, minsize=50)


ventana.mainloop()
