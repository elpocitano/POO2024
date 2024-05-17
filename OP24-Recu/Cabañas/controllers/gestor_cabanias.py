# -*- coding: utf-8 -*-
"""
Luna Juan Marcelo
DNI 24234578
@author: elpocitano@gmail.com
2. Una clase Gestor de cabañas que almacene instancias de la clase Cabaña. Cada una de estas
instancias se creará con los datos registrados en el archivo “Cabañas.csv”. Este gestor debe
basarse en un arreglo Numpy teniendo en cuenta que el complejo tiene 10 cabañas.

"""
from models.cabania import Cabania
from controllers.gestor_reservas import GestorReservas
import numpy as np


class GestorCabanias:
    __arre_cabanias: np.ndarray
    __dimension: int
    __incremento: int
    __cantidad: int

    def __init__(self):
        self.__dimension = 10
        self.__incremento = 0
        self.__cantidad = 0
        self.__arre_cabanias = np.empty(self.__dimension, dtype=Cabania)

    def agregar_cabania(self, cabania):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arre_cabanias.resize(self.__dimension)
        self.__arre_cabanias[self.__cantidad] = cabania
        self.__cantidad += 1

    def cargar_archivo_cabanias(self):
        csv_file="../data/Cabañas.csv"
        with open(csv_file) as csv_handler:
            next(csv_handler)
            for fila in csv_handler:
                atributos_cabania = fila.replace(" ", "").replace('"', '').split(';')
                num, ctdad_hab, camas_gdes, camas_chicas, imp_dia = atributos_cabania
                # cabania = Cabania(num, ctdad_hab, camas_gdes, camas_chicas, imp_dia)
                cabania01 = Cabania(*atributos_cabania)
                self.agregar_cabania(cabania01)

    def ordenar_lista_cabanias(self):
        self.__arre_cabanias[:self.__cantidad].sort()

    def listar_cabanias(self):
        for i in range(self.__cantidad):
            print(self.__arre_cabanias[i])

    def listar_cabanias_libres_x_capacidad(self, num_huespedes, GR):
        for cabania in self.__arre_cabanias[:self.__cantidad]:
            if cabania >= num_huespedes:
                num_cabania = int(cabania.get_num())
                if GR.buscar_num_cab_reservas(num_cabania) == -1:
                    print(f"Cabaña num {cabania.get_num()} capacidad {cabania.get_capacidad()} disponible.")


if __name__ == "__main__":
    GR = GestorReservas()
    GR.cargar_archivo_reservas()

    GC = GestorCabanias()
    GC.cargar_archivo_cabanias()
    GC.listar_cabanias()

    print("Ordena la lista")
    GC.ordenar_lista_cabanias()
    GC.listar_cabanias()
    print("listar_cabanias_libres_x_capacidad(4).")
    GC.listar_cabanias_libres_x_capacidad(4, GR)
    #GC.listar_cabanias_libres_x_capacidad(4, GR)