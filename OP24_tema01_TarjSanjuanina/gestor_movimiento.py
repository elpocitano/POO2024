# -*- coding: utf-8 -*-
"""
Luna Juan Marcelo
DNI 24234578
@author: elpocitano@gmail.com
"""

from movimiento import Movimiento as MV
import numpy as np


class GM:
    __movim_lista: np.ndarray
    __dimension: int
    __incremento: int
    __ctdad_ocup: int

    def __init__(self):
        self.__dimension = 20 # Definimos la variable para el tamaño
        self.__incremento = 5 # La ctdad de componentes que crece en cada redimensionamiento
        self.__ctdad_ocup = 0 # Este sera el contador que indica las componentes ocupadas
        self.__movim_lista = np.empty(self.__dimension, dtype=MV) # Declaramos el tamaño y el tipo de componentes del arreglo

    def cargar_archivo_movimientos(self, csv_file):
        with open(csv_file) as archivo_mgr:
            next(archivo_mgr)
            for fila in archivo_mgr:
                atributos = fila.replace(" ", "").replace('"', '').split(';')
                num_tarj, fecha, descrip, tipo_mov, importe = atributos
                movimiento = MV(num_tarj, fecha, descrip, tipo_mov, float(importe))
                gm.agregar_movimiento(movimiento)

    def agregar_movimiento(self, movimiento):
        if self.__dimension == self.__ctdad_ocup: # Primero comprobamos si el arreglo esta lleno
            self.__dimension += self.__incremento # El nuevo tamaño sera lo que tenia mas el incremento
            self.__movim_lista.resize(self.__dimension) # Redimensionamos al nuevo tamaño
            # self.__movim_lista = np.resize(self.__movim_lista, self.__dimension)
        self.__movim_lista[self.__ctdad_ocup] = movimiento # guardamos el objeto en la posicion libre
        self.__ctdad_ocup += 1 # se incrementa en uno la posicion libre para la proxima

    def ordenar_lista_movimientos(self):
        #Estos metodos de ordenamiento dan error cuando hay componentes nulas en el array,
        #el error salta en el metodo __lt__ del objeto
        #self.__movim_lista = np.sort(self.__movim_lista)
        #self.__movim_lista.sort()
        # Este metodo sort compara las componentes hasta cantidad ocupada de array. Evitando las nulas.
        self.__movim_lista[:self.__ctdad_ocup].sort() # Ordena la lista pero hasta el indice especificado, evita componentes nulas
    def listar_lista_movimientos(self):
        for i in range(len(self.__movim_lista)):
            if isinstance(self.__movim_lista[i], MV):
                print(f"Movimiento num: {i+1}.")
                print(self.__movim_lista[i].get_num_tarj(), " ", self.__movim_lista[i].get_importe())
            else:
                print(f"Componente del arreglo vacia.")


if __name__ == '__main__':
    gm = GM()
    csv_file = "MovimientosAbril2024.csv"
    gm.cargar_archivo_movimientos(csv_file)
    print("Listamos los movimientos")
    gm.listar_lista_movimientos()
    print("Ordenamos los movimientos por num de tarjeta")
    gm.ordenar_lista_movimientos()
    print("Listamos los movimientos")
    gm.listar_lista_movimientos()
