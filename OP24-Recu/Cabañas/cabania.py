# -*- coding: utf-8 -*-
"""
Luna Juan Marcelo
DNI 24234578
@author: elpocitano@gmail.com
complejo de cabañas “El soleado”
Cada Cabaña: número, cantidad de habitaciones, cantidad de camas grandes, cantidad de camas chicas e importe por día.
"""


class Cabania:
    __num: int
    __ctdad_hab: int
    __camas_gdes: int
    __camas_chicas: int
    __imp_dia: float

    def __init__(self, num, ctdad_hab, camas_gdes, camas_chicas, imp_dia):
        self.__num = num
        self.__ctdad_hab = ctdad_hab
        self.__camas_gdes = camas_gdes
        self.__camas_chicas = camas_chicas
        self.__imp_dia = imp_dia

    def __str__(self):
        return f"{self.__num} {self.__ctdad_hab} {self.__camas_gdes} {self.__camas_chicas} {self.__imp_dia}"

    def get_num(self):
        return self.__num

    def get_imp_dia(self):
        return self.__imp_dia

    def __lt__(self, other):
        return self.__num < other.get_num()  # Ordena por número de cabaña

    def get_capacidad(self):
        capacidad = ((self.__camas_gdes * 2) + self.__camas_chicas)
        return capacidad

    def __ge__(self, other):
        return self.get_capacidad() >= other.get_capacidad()


if __name__ == "__main__":
    pass
