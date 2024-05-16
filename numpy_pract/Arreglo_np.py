# -*- coding: utf-8 -*-
"""
Luna Juan Marcelo
DNI 24234578
@author: elpocitano@gmail.com
"""
import csv
import numpy as np


class GestorListaNP:
    __cant_ocup: int
    __dimension: int
    __incremento: int
    __arre_objetos: np.ndarray

    def __init__(self):
        self.__cant_ocup = 0
        self.__dimension = 20
        self.__incremento = 5
        self.__arre_objetos = np.empty(self.__dimension, dtype=object)

    def agregar_objeto(self, objeto):
        if self.__cant_ocup == self.__dimension:
            self.__dimension += self.__incremento
            self.__arre_objetos.resize(self.__dimension)
        self.__arregloMovimientos[self.__cant_ocup] = objeto
        self.__cant_ocup += 1

    def carga_archivo(self):
        band: bool = False
        archivo = open("MovimientosAbril2024.csv")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            if band is False:
                band = True
            else:
                self.agregarMovimiento(Movimiento(int(fila[0]), fila[1], fila[2], fila[3], float(fila[4])))
        archivo.close()

    def existen_movimientos_porNumCuenta(self, numC):
        existe: bool = False
        i: int = 0
        while i < self.__cantidad and existe is False:
            if self.__arregloMovimientos[i].getNumCuenta() == numC:
                existe = True
            else:
                i += 1
        return existe

    def ordenarMovimientos(self):
        self.__arregloMovimientos = np.sort(self.__arregloMovimientos)
        print("Los movimientos fueron ordenados por numeros de cuenta!")

    def listarMovimientos(self):
        for unmovimiento in self.__arregloMovimientos:
            print(unmovimiento)
