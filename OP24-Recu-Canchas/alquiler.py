# -*- coding: utf-8 -*-
"""
Luna Juan Marcelo
DNI 24234578
@author: elpocitano@gmail.com
Cada Alquiler: nombre de la persona que alquiló, identificador de la cancha alquilada, hora y
minutos para la cual se alquiló (ejemplo: para las 15 hs y 30 minutos), duración de alquiler en
minutos (60, 90, 120).
"""


class Alquiler:
    __nomb_usuario: str
    __id_cancha: str
    __alq_hora: str
    __alq_minutos: str
    __durac_minutos: int
    def __init__(self, usuario, id_cancha, alq_hora, alq_minutos, durac_minutos):
        self.__nomb_usuario = usuario
        self.__id_cancha = id_cancha
        self.__alq_hora = alq_hora
        self.__alq_minutos = alq_minutos
        self.__durac_minutos = durac_minutos

    def __str__(self):
        return f'Alquiler de cancha: {self.__id_cancha} por {self.__nomb_usuario} a las {self.__alq_hora} durante {self.__durac_minutos} minutos.'

    def get_usuario(self):
        return self.__nomb_usuario

    def get_id_cancha(self):
        return self.__id_cancha

    def get_alqu_hora(self):
        return self.__alq_hora

    def get_alqu_duracion_minutos(self):
        return self.__durac_minutos

    def get_alqu_duracion_horas(self):
        horas_alqu: float
        horas_alqu = self.__durac_minutos / 60
        return horas_alqu

    def __gt__(self, other):
        return self.get_alqu_duracion_horas() > other.get_alqu_duracion_horas()


if __name__ == '__main__':
    alq01 = Alquiler("Marcelo Luna", "C", "13", '30', 60)
    print(alq01)
    print(f'Tiempo de alquiler en minutos: {alq01.get_alqu_duracion_minutos()} tipo dato: {type(alq01.get_alqu_duracion_minutos())}')
    print(f'Tiempo de alquiler en horas: {alq01.get_alqu_duracion_horas()} tipo dato: {type(alq01.get_alqu_duracion_horas())}')
    alq02 = Alquiler("Jorge Cortez", "A", "13", '45', 90)
    print(alq02)
    print(
        f'Tiempo de alquiler en minutos: {alq02.get_alqu_duracion_minutos()} tipo dato: {type(alq02.get_alqu_duracion_minutos())}')
    print(
        f'Tiempo de alquiler en horas: {alq02.get_alqu_duracion_horas()} tipo dato: {type(alq02.get_alqu_duracion_horas())}')

    print(alq01 > alq02)
    print(alq01 < alq02)