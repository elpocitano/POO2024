# -*- coding: utf-8 -*-
"""
Luna Juan Marcelo
DNI 24234578
@author: elpocitano@gmail.com
"""
import csv
import numpy as np
from movimiento import Movimiento


class GMnp:
    __ctdad_ocupada: int
    __dimension: int
    __incremento: int
    __arre_movi: np.ndarray

    def __init__(self):
        print("Instancia de la clase")
        self.__dimension = 20
        self.__ctdad_ocupada = 0
        self.__incremento = 5
        self.__arre_movi = np.empty(self.__dimension, dtype=Movimiento)

    def agregar_movimiento(self, movimiento):
        print("agregar movimiento")
        if self.__ctdad_ocupada == self.__dimension:
            self.__dimension += self.__incremento
            self.__arre_movi.resize(self.__dimension)
        self.__arre_movi[self.__ctdad_ocupada] = movimiento
        self.__ctdad_ocupada += 1

    def cargar_archivo_movimientos(self, csv_file):
        print("cargar movimiento desde archivo")
        try:
            with open(csv_file) as gestor_archivo:
                next(gestor_archivo)
                for linea in gestor_archivo:
                    atributos = linea.replace(" ", "").split(";")
                    num_cta, fecha, descrip, tipo_mov, importe = atributos
                    movimiento = Movimiento(num_cta, fecha, descrip, tipo_mov, importe)
                    self.agregar_movimiento(movimiento)
        except:
            print("Error en la carga del  archivo.")

    def cargar_archivo_movimientos_b(self, csv_file):
        print("Cargar movimientos desde archivo")
        try:
            with open(csv_file, newline='') as gestor_archivo:
                lector_csv = csv.reader(gestor_archivo, delimiter=';')
                next(lector_csv)  # Saltar la primera fila (encabezados)
                for fila in lector_csv:
                    num_cta, fecha, descrip, tipo_mov, importe = fila
                    movimiento = Movimiento(num_cta, fecha, descrip, tipo_mov, importe)
                    self.agregar_movimiento(movimiento)
        except Exception as e:
            print("Error en la carga del archivo:", e)

    def listar_arre_movimientos(self):
        print("listado de arreglo")
        i = 0
        while i < self.__ctdad_ocupada:
            movimiento = self.__arre_movi[i]
            print(f"{movimiento.get_num_cta()} ")
            i += 1


if __name__ == '__main__':
    print("Instanciar clase")
    GM = GMnp()
    print("Cargar archivo")
    csv_file = "MovimientosAbril2024.csv"
    print("Listar archivos")
    GM.cargar_archivo_movimientos(csv_file)
    GM.listar_arre_movimientos()
