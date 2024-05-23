# -*- coding: utf-8 -*-
"""
Luna Juan Marcelo
DNI 24234578
@author: elpocitano@gmail.com

"""
from cancha import Cancha
from alquiler import Alquiler
from gestor_alquileres import GestorAlquileres
import numpy as np


# import csv


class GestorCanchas:
    arreglo_canchas: np.ndarray
    __dimension: int
    __indice: int
    __increment: int

    def __init__(self):
        self.__dimension = 6
        self.__indice = 0
        self.__increment = 1
        self.arreglo_canchas = np.empty(self.__dimension, dtype=Cancha)

    def agregar_cancha(self, xcancha):
        if self.__indice == self.__dimension:
            print(f'Va a agregar una nueva cancha al club')
            self.__dimension = self.__dimension + self.__increment
            self.arreglo_canchas.resize(self.__dimension)
        self.arreglo_canchas[self.__indice] = xcancha
        self.__indice += 1

    def listar_canchas(self):
        for cancha in self.arreglo_canchas:
            print(cancha)

    def cargar_archivo_canchas(self, file):
        try:
            with (open(file) as fhandler):
                next(fhandler)
                for fila in fhandler:
                    atributos = fila.replace(" ", "").replace('"', '').split(";")
                    id_cancha, tipo_piso, importe_hora = atributos
                    una_cancha = Cancha(id_cancha, tipo_piso, float(importe_hora))
                    self.agregar_cancha(una_cancha)
        finally:
            print("Carga terminada")

    def buscar_cancha_byid(self, xid_cancha):
        encontrado = -1
        i = 0
        while encontrado == -1 and i < self.__indice:
            una_Cancha = self.arreglo_canchas[i]
            if una_Cancha.get_id_cancha() == xid_cancha:
                encontrado = i
            else:
                i += 1
        return encontrado

    def mostrar_hs_alqu_byidcancha(self, xid_cancha, GA):
        print("Buscando cancha")
        indice = self.buscar_cancha_byid(xid_cancha)
        print("Indice cancha: ", indice)
        if indice == -1:
            hs_alquilada = indice
            print("Cancha no encontrada")
        print("Cancha encontrada")
        hs_alquilada = GA.buscar_hs_alqu_byidcancha(xid_cancha)
        print("Horas alquilada: ",hs_alquilada)
        print(f'Cancha {xid_cancha} estuvo alquilada: {hs_alquilada} horas.')
        return hs_alquilada

    def mostrar_min_alqu_byidcancha(self, xid_cancha, GA):
        indice = self.buscar_cancha_byid(xid_cancha)
        if indice == -1:
            hs_alquilada = indice
            print("Cancha no encontrada")
        min_alquilada = GA.buscar_min_alqu_byidcancha(xid_cancha)
        print(f'Cancha {xid_cancha} estuvo alquilada un total de {min_alquilada} minutos.')
        return min_alquilada


if __name__ == '__main__':
    archivo_canchas = "Canchas.csv"
    gc = GestorCanchas()
    gc.cargar_archivo_canchas(archivo_canchas)
    archivo_alquileres = "Alquiler.csv"
    ga = GestorAlquileres()
    ga.cargar_archivo_alqu(archivo_alquileres)

    # gc.listar_canchas()
    una_cancha = gc.arreglo_canchas[2]
    print(una_cancha.get_importe_hora())
    gc.mostrar_hs_alqu_byidcancha("B", ga)
"""
    def cargar_archivo_canchas(self, file):
        try:
            with open(file) as fhandler:
                csv_reader = csv.reader(fhandler, delimiter=';')
                next(csv_reader)  # Skip the header row
                for fila in csv_reader:
                    fila = [item.strip() for item in fila]  # Strip whitespace characters
                    id_cancha, tipo_piso, importe_hora = fila
                    una_cancha = Cancha(id_cancha, tipo_piso, float(importe_hora))
                    self.agregar_cancha(una_cancha)
        except FileNotFoundError:
            print(f"Error: El archivo {file} no se encontró.")
        except ValueError as e:
            print(f"Error: {e}")
        finally:
            print("Carga terminada.")
"""
