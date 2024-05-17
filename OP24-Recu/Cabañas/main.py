# -*- coding: utf-8 -*-
"""
Luna Juan Marcelo
DNI 24234578
@author: elpocitano@gmail.com
 a. Ingresar por teclado una cantidad de huéspedes y mostrar el o los números de las cabañas
que tienen una capacidad igual o mayor a la cantidad ingresada y no tienen ninguna reserva
registrada.
    Reglas:
           Para esta funcionalidad debe definir la sobrecarga del operador __ge__ en la clase
Cabaña y usar la sobrecarga definida.
           La capacidad de una cabaña se calcula como:
capacidad de una cabaña = cantidad de camas grandes * 2 + cantidad de camas chicas.
"""
import os
from controllers.gestor_cabanias import GestorCabanias
from controllers.gestor_reservas import GestorReservas


def menu():
    print("### Gestion de cabañas y reservas complejo “El soleado”     ###")
    print("1. Cabañas libres con capacidad para ctdad huespedes ingresada.")
    print("2. Listar reservas para la fecha ingresada (formato 1/7/2024). ")
    print("0. Para salir.")


def opcion01(GC, GR):
    ctdad_huespedes = int(input("Ingrese cantidad de huespedes a alojar: "))
    GC.listar_cabanias_libres_x_capacidad(ctdad_huespedes, GR)


def opcion02(GC, GR):
    """b. Ingresar una fecha y emitir un listado con las reservas cuya fecha de inicio del hospedaje sea
igual a la ingresada"""
    fecha = input("Ingrese fecha para consultar reservas (formato 1/7/2024): ")
    GR.listar_reservas_fecha(fecha)


if __name__ == "__main__":
    """
    # Obtener la ruta del directorio del script actual
    current_dir = os.path.dirname(__file__)
    
    # Construir la ruta a los archivos CSV utilizando el directorio actual o raiz
    archivo_cabania = os.path.join(current_dir, "../data/Cabaña.csv")
    archivo_reserva = os.path.join(current_dir, "../data/Reserva.csv")
    """

    GC = GestorCabanias()
    GC.cargar_archivo_cabanias()
    GR = GestorReservas()
    GR.cargar_archivo_reservas()

    while True:
        menu()
        opcion: int
        opcion = int(input("Ingrese opcion > "))
        if opcion == 0:
            break
        elif opcion == 1:
            opcion01(GC, GR)
        elif opcion == 2:
            opcion02(GC, GR)
        else:
            print("Opcion invalida, ingrese nuevamente")