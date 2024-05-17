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
    __importe_diario: float

    def __init__(self, num_re, nomb_per, num_cab, fecha_in, cant_huesp, cant_dias, importe_sen, importe_dia = 75000.00):
        self.__num_reserva = num_re
        self.__nomb_pers = nomb_per
        self.__num_cabania = num_cab
        self.__fecha_inicio = fecha_in
        self.__cant_huespedes = cant_huesp
        self.__cant_dias = cant_dias
        self.__importe_senia = importe_sen
        self.__importe_diario = importe_dia

    def __str__(self):
        return f"{self.__num_cabania} {self.__importe_diario} {self.__cant_dias} {self.__importe_senia} {self.get_importe_cobrar()}"

    def get_num_reserva(self) -> int:
        return self.__num_reserva

    def get_num_cabania(self) -> int:
        return self.__num_cabania

    def get_fecha(self) -> str:
        return self.__fecha_inicio

    def get_cant_dias(self) -> int:
        return self.__cant_dias

    def get_import_senia(self):
        return self.__importe_senia

    def get_importe_diario(self) -> float:
        return self.__importe_diario

    def get_importe_cobrar(self) -> float:
        importe_cobrar = (int(self.__cant_dias) * float(self.__importe_diario)) - float(self.__importe_senia)
        return importe_cobrar


if __name__ == '__main__':
    pass
