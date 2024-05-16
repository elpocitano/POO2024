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
from cabania import Cabania
from reserva import Reserva
from gestor_reservas import GestorReservas as GR
from gestor_cabanias import GestorCabanias as GC


    def menu():
        print("### Gestion de cabañas y reservas ###")
        print("1. Cabañas libres con capacidad para ctdad huespedes ingresada.")
        print("0. Para salir.")

    def opcion01():
        ctdad_huespedes = int(input("Ingrese cantidad de huespedes a alojar"))
        GC.

if __name__ == "__main__":
    menu()
    opcion : int
    opcion = int(input("Ingrese opcion > "))
    match opcion:
        case 1:
            opcion01()
        case 2:
            opcion02()

