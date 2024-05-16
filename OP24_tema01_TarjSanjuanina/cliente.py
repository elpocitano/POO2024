# -*- coding: utf-8 -*-
"""
Luna Juan Marcelo
DNI 24234578
@author: elpocitano@gmail.com
Los Clientes: nombre, apellido, dni, número de tarjeta, saldo anterior.
"""


class Cliente:
    __nombre: str
    __apellido: str
    __dni: str
    __num_tarj: str
    __saldo_anterior: float

    def __init__(self, nom, apel, dni, num_tarj, saldo_ant):
        self.__nombre = nom
        self.__apellido = apel
        self.__dni = dni
        self.__num_tarj = num_tarj
        self.__saldo_anterior = saldo_ant

    def get_nomb(self):
        return self.__nombre

    def get_apel(self):
        return self.__apellido

    def get_dni(self):
        return self.__dni

    def get_num_tarj(self):
        return self.__num_tarj

    def get_saldo_ant(self):
        return self.__saldo_anterior

    def __lt__(self, other):
        return self.__dni < other.__dni


if __name__ == '__main':
    pass
