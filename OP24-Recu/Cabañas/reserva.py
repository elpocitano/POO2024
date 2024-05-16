# -*- coding: utf-8 -*-
"""
Luna Juan Marcelo
DNI 24234578
@author: elpocitano@gmail.com
Reserva: número de reserva, nombre de la persona que reservó, número de cabaña asignada,
fecha de inicio del hospedaje, cantidad de huéspedes, cantidad de días, importe de la seña.
"""


class Reserva:
    __num_reserva: int
    __nomb_pers: str
    __num_cabania: int
    __fecha_inicio: str
    __cant_huespedes: int
    __cant_dias: int
    __importe_senia: float

    def __init__(self, num_reserva, nomb_pers, num_cabania, fecha_inicio, cant_huespedes, cant_dias, importe_senia):
        self.__num_reserva = num_reserva
        self.__nomb_pers = nomb_pers
        self.__num_cabania = num_cabania
        self.__fecha_inicio = fecha_inicio
        self.__cant_huespedes = cant_huespedes
        self.__cant_dias = cant_dias
        self.__importe_senia = importe_senia

    def __str__(self):
        return f"{self.__num_reserva} {self.__nomb_pers} {self.__num_cabania} {self.__fecha_inicio} {self.__cant_huespedes} {self.__cant_dias} {self.__importe_senia}"

    def get_num_reserva(self):
        return self.__num_reserva

    def is_cabania_reservada(self, num_cabania):
        reservada = -1
        indice = 0
        while res

if __name__ == '__main__':
    pass
