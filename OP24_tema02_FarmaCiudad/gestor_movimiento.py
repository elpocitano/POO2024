# -*- coding: utf-8 -*-
"""
Luna Juan Marcelo
DNI 24234578
@author: elpocitano@gmail.com
3. Escriba el código de un Gestor de Movimientos, que permita leer y almacenar los datos de
todos los Movimientos de las cuentas de los Clientes, para el mes de abril del 2024. Este gestor
debe basarse en un arreglo Numpy.
tipo de movimiento (‘C’ – Crédito, ‘P’-Pago)
5. Leer los datos del archivo “MovimientosAbril2024.csv”, y almacenarlos en el Gestor de Movimientos.
número de cuenta, fecha, descripción, tipo de movimiento (‘C’ – Crédito, ‘P’-Pago), importe
"""
import numpy as np
from movimiento import Movimiento


class GM:
    def __init__(self):
        self.movi_lista = np.array([])

    def agregar_movimiento(self, xmovi):
        self.movi_lista = np.append(self.movi_lista, xmovi)

    def listar_movimientos(self):
        for movim in self.movi_lista:
            print(movim.get_num_cta())

    def get_balance_x_num_cta(self, num_cta):
        pago: float
        pago = 0
        credito: float
        credito = 0
        for mov in self.movi_lista:
            if mov.get_num_cta() == num_cta:
                if mov.get_tipo_mov() == "C":
                    credito += float(mov.get_importe())
                elif mov.get_tipo_mov() == "D":
                    pago += float(mov.get_importe())
                else:
                    print("Tipo de pago no contemplado")
        balance = credito - pago
        return balance

    def mostrar_movi_x_num_cta(self, num_cta):
        print("Fecha        Descripción         Importe     Tipo de movimiento")
        for mov in self.movi_lista:
            if mov.get_num_cta() == num_cta:
                print(f"{mov.get_fecha()} {mov.get_descrip()} {mov.get_importe()} {mov.get_tipo_mov()}")

    def ctdad_mov_x_num_cta(self, num_cta):
        ctdad_movim = 0
        for movim in self.movi_lista:
            if movim.get_num_cta() == num_cta:
                ctdad_movim += 1
        return ctdad_movim

    def cargar_archivo_movimientos(self, csv_file):  # csv es una cadena con el nombre o el path del archivo
        # quisiera implementar un try que cargue el archivo o un excepcion que avise que no se encontro
        with open(csv_file) as archivo:
            next(archivo)
            for linea in archivo:
                atributos = linea.replace('"', '').replace(" ", "").split(";")
                num_cta, fecha, descr, tipo_mov, importe = atributos
                movimiento = Movimiento(num_cta, fecha, descr, tipo_mov, importe)
                print(f"{movimiento.get_num_cta()} {movimiento.get_importe()}")
                self.agregar_movimiento(movimiento)
                # tambien se podria usar gm.agregar_movi(movimiento), no se que convenga
                print("Carga exitosa")

    # Ordenar lista por num cuenta
    def ordenar_movi_x_num_cuenta(self):
        self.movi_lista.sort()


if __name__ == "__main__":
    gm = GM()
    # csv = input("Ingrese el nombre del archivo")
    csv_file = "MovimientosAbril2024.csv"
    gm.cargar_archivo_movimientos(csv_file)
    movi = Movimiento(410, "12/03/2023", "Venta Antibiotico", 'P', 9850)
    gm.listar_movimientos()
    gm.agregar_movimiento(movi)
    gm.listar_movimientos()
    print("Numero de cuenta 304.")
    num_cta = "304"
    print("Balance de movimientos de la cuenta:")
    balance = gm.get_balance_x_num_cta(num_cta)
    print(balance)
    print("Movimintos de esa cuenta")
    gm.mostrar_movi_x_num_cta(num_cta)
    print("Cantidad de movimientos de la cuenta")
    gm.ctdad_mov_x_num_cta(num_cta)
    print("Ordenar lista de movimientos.")
    gm.ordenar_movi_x_num_cuenta()
    gm.listar_movimientos()
