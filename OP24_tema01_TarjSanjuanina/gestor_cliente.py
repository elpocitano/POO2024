# -*- coding: utf-8 -*-
"""
Luna Juan Marcelo
DNI 24234578
@author: elpocitano@gmail.com
"""
from cliente import Cliente


class MC:
    __clientes_lista: list

    def __init__(self):
        self.__clientes_lista = []

    def cargar_archivo_clientes(self, file):
        with open(file) as file_handler:
            next(file_handler)
            for fila in file_handler:
                atributos = fila.replace('"', '').split(';')
                nom, apel, dni, num_tarj, saldo_ant = atributos
                cliente = Cliente(nom, apel, dni, num_tarj, float(saldo_ant))
                self.__clientes_lista.append(cliente)
                print(f"Carga exitosa {cliente.get_nomb()} {cliente.get_apel()}")

    def listar_clientes(self):
        for cliente in self.__clientes_lista:
            print(f"{cliente.get_nomb()} {cliente.get_apel()} {cliente.get_dni()} {cliente.get_saldo_ant()}")


if __name__ == '__main__':
    mc = MC()
    mc.cargar_archivo_clientes("ClientesAbril2024.csv")
    mc.listar_clientes()
