import os
import sys
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Libreria')


def exportar():
    precio = float(entrada.get())
    precio = round(precio, 3)
    envio = str(labelRespuesta.cget('text'))
    contenido = f'Nombre libro: {entradanombre.get()}'
    contenido += f'\nID del libro: {entradaid.get()}'
    contenido += f'\nPrecio: {precio}'
    contenido += f'\nEnvio gratis: {envio}'

    ruta = './Información_libro.txt'
    archivo = open(ruta, 'w')
    archivo.write(contenido)
    archivo.close()

    #Abrir archivo despues de exportarlo
    ruta_absoluta=os.path.abspath(ruta)
    os.startfile(ruta_absoluta)


def calcular():
    precio = float(entrada.get())
    precio=round(precio, 3)
    mensaje1 = "Envio es gratuito"
    mensaje2 = "Envio no es gratuito"
    if precio >= 100000:
        envioGratuito = True
        labelRespuesta["text"]=str(envioGratuito)
        print(envioGratuito)
        messagebox.showinfo('Mensaje informativo ',mensaje1)
    else:
        envioGratuito = False
        labelRespuesta["text"]=str(envioGratuito)
        messagebox.showinfo('Mensaje informativo ',mensaje2)
        


labeltitle = tk.Label(ventana, text="Calculo Costo de envio libro")
labeltitle.grid(row=0, column=2, pady=20)

labelnombre = tk.Label(ventana, text="Nombre del libro: ")
labelnombre.grid(row=1, column=0, pady=5, padx=10)

entradanombre = tk.Entry(ventana,  width=20)
entradanombre.grid(row=1, column=1, pady=5, padx=10)


labelid = tk.Label(ventana, text="ID: ")
labelid.grid(row=2, column=0, pady=5, padx=10)

entradaid = tk.Entry(ventana,  width=20)
entradaid.grid(row=2, column=1, pady=5, padx=10)


label1 = tk.Label(ventana, text="Precio del libro:")
label1.grid(row=3, column=0, pady=5, padx=10)

entrada = tk.Entry(ventana,  width=20)
entrada.grid(row=3, column=1, pady=5, padx=10)

labelGratuito = tk.Label(ventana, text="Envio gratuito: ")
labelGratuito.grid(row=4, column=0, pady=5, padx=10)

labelRespuesta = tk.Label(ventana, text="ᓚᘏᗢ")
labelRespuesta.grid(row=4, column=1, pady=5, padx=10)

boton1 = tk.Button(ventana, text="Exportar", command=exportar)
boton1.grid(row=5, column=1, pady=5, padx=10)

boton2 = tk.Button(ventana, text="Calcular", command=calcular)
boton2.grid(row=3, column=2, padx=10, pady=5)

ventana.mainloop()