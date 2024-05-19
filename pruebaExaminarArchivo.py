import tkinter as tk
from tkinter import filedialog

def mostrarEmpleados(archivo_seleccionado):
    with open (archivo_seleccionado) as fileEmp:
        next(fileEmp)
        for file in fileEmp:
            file = file.split(";")
            print(file)

def seleccionar_archivo():
    archivo_seleccionado = filedialog.askopenfilename()
    mostrarEmpleados(archivo_seleccionado)

root = tk.Tk()
boton_seleccionar = tk.Button(root, text="Seleccionar archivo", command=seleccionar_archivo)
boton_seleccionar.pack()
root.mainloop()


    
