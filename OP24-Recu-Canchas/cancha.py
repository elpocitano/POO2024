# -*- coding: utf-8 -*-
"""
Luna Juan Marcelo
DNI 24234578
@author: elpocitano@gmail.com
Cada Cancha: identificador, tipo de piso, importe por hora.
"""


class Cancha():
    __id_cancha : str
    __tipo_piso: str
    __importe_hora: float

    def __init__(self, id_cancha, tipo_piso, importe_hora):
        self.__id_cancha = id_cancha
        self.__tipo_piso = tipo_piso
        self.__importe_hora = importe_hora

    def __str__(self):
        return f'Cancha: {self.__id_cancha}, piso: {self.__tipo_piso}, precio hora: $ {self.__importe_hora} '

    def get_id_cancha(self):
        return self.__id_cancha

    def get_tipo_piso(self):
        return self.__tipo_piso

    def get_importe_hora(self):
        return self.__importe_hora


if __name__ == '__main__':
    una_cancha = Cancha("B", 'cesped', 6000.00)
    print(una_cancha.get_id_cancha())
    print(una_cancha.get_tipo_piso())
    print(f'Importe hora: $ {una_cancha.get_importe_hora()} tipo {type(una_cancha.get_importe_hora())}')
    print(una_cancha)

