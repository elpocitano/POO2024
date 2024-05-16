# -*- coding: utf-8 -*-
"""
Luna Juan Marcelo
DNI 24234578
@author: elpocitano@gmail.com
3. Una clase Gestor de reservas que almacene instancias de la clase Reserva. Cada una de estas
instancias se creará con los datos registrados en el archivo “Reservas.csv”. Este gestor debe
basarse en una lista Python.
"""
from reserva import Reserva
import csv


class GestorReservas:
    __lista_reservas: list

    def __init__(self):
        self.__lista_reservas = []

    def agregar_reserva(self, reserva):
        self.__lista_reservas.append(reserva)

    def cargar_archivo_reservas(self, csv_file="Reservas.csv"):
        with open(csv_file) as csv_handler:
            next(csv_handler)
            for fila in csv_handler:
                atributos_reserva = fila.replace(" ", "").replace('"', '').split(';')
                una_reserva = Reserva(*atributos_reserva)
                self.agregar_reserva(una_reserva)

    def listar_reservas(self):
        for reserva in self.__lista_reservas:
            print(reserva)

    def


if __name__ == "__main__":
    GR = GestorReservas()
    GR.cargar_archivo_reservas("Reservas.csv")
    GR.listar_reservas()

