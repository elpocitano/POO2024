# -*- coding: utf-8 -*-
"""
propsd + TAB
Luna Juan Marcelo
DNI 24234578
@author: elpocitano@gmail.com
Los Movimientos:
número de cuenta, fecha, descripción, tipo de movimiento (‘C’ – Crédito, ‘P’-Pago), importe
"""


class Movimiento:
    __num_cta: int
    __fecha: str
    __descrip: str
    __tipo_mov: str
    __importe: float

    def __init__(self, num_cta, fecha, descrip, tipo_mov, importe : float):
        self.__num_cta = num_cta
        self.__fecha = fecha
        self.__descrip = descrip
        self.__tipo_mov = tipo_mov
        self.__importe = importe

    def get_num_cta(self):
        return self.__num_cta

    def get_tipo_mov(self):
        return self.__tipo_mov

    def get_importe(self):
        return self.__importe

    def get_fecha(self):
        return self.__fecha

    def get_descrip(self):
        return self.__descrip

    def __lt__(self, other):
        return str(self.__num_cta) < str(other.__num_cta)
