# -*- coding: utf-8 -*-
"""
Luna Juan Marcelo
DNI 24234578
@author: elpocitano@gmail.com
"""
from alquiler import Alquiler
import unittest


class GestorAlquileres:
    lista_alqu: list

    def __init__(self):
        self.lista_alqu = []

    def agregar_alqu(self, xalquiler):
        if isinstance(xalquiler, Alquiler):
            self.lista_alqu.append(xalquiler)
        else:
            print(f'No es un alquiler válido')

    def cargar_archivo_alqu(self, xfile):
        print(xfile)
        file = xfile
        try:
            with (open(file) as fhandler):
                next(fhandler)
                for fila in fhandler:
                    atributos = fila.replace('"', '').replace(" ", "").split(";")
                    usuario, id_cancha, alq_hora, alq_minutos, durac_minutos = atributos
                    un_alquiler = Alquiler(usuario, id_cancha, alq_hora, alq_minutos, int(durac_minutos))
                    self.agregar_alqu(un_alquiler)
        finally:
            print("Carga terminada.")

    def listar_alquileres(self):
        for alquiler in self.lista_alqu:
            print(alquiler)

    def ordenar_alquileres_duracion(self):
        self.lista_alqu.sort()

    def buscar_min_alqu_byidcancha(self, xid_cancha):
        encontrado = -1
        i = 0
        while encontrado == -1 and i < len(self.lista_alqu):
            un_alquiler = self.lista_alqu[i]
            if un_alquiler.get_id_cancha() == xid_cancha:
                encontrado = un_alquiler.get_alqu_duracion_minutos()
            else:
                i += 1
        return encontrado


