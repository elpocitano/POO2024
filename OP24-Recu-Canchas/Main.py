# -*- coding: utf-8 -*-
"""
Luna Juan Marcelo
DNI 24234578
@author: elpocitano@gmail.com
01 Emitir un listado ordenado por hora y minutos con todos los alquileres registrados y con el
siguiente formato:
02 b. Ingresar el identificador de una cancha y mostrar la cantidad total de minutos que estuvo
alquilada.
"""
from gestor_alquileres import GestorAlquileres
from gestor_canchas import GestorCanchas


def Menu():
    print("#############################################")
    print("#Complejo de canchas de fútbol Un partidito.#")
    print("#[1] Emitir listado de alquileres, ordenado.#")
    print("#[2] Ingresar Id cancha para ver cantidad   #")
    print("#    de horas que estuvo alquilada          #")
    print("#[3]                                        #")
    print("#############################################")
    print("#[0] Salir del programa.                    #")
    print("#############################################")


# [1] Emitir listado de alquileres, ordenado.
def listar_alquileres_ordenados_byhora(GA):
    GA.ordenar_alquileres_duracion()
    GA.listar_alquileres()


def mostrar_minutos_alqu_byidcancha(GA, GC):
    id_cancha = input("Ingrese Id de la cancha, Letras A a F").upper()
    GC.mostrar_min_alqu_byidcancha(id_cancha, GA)


if __name__ == '__main__':
    archivo_canchas = 'Canchas.csv'
    archivo_alquileres = 'Alquiler.csv'
    GC = GestorCanchas()
    GC.cargar_archivo_canchas(archivo_canchas)
    GA = GestorAlquileres()
    GA.cargar_archivo_alqu(archivo_alquileres)
    while True:
        Menu()
        opcion = input("Ingrese opcion deseada: >")
        match opcion:
            case '1':
                listar_alquileres_ordenados_byhora(GA)
            case '2':
                mostrar_minutos_alqu_byidcancha(GA, GC)
            case '0':
                break
            case _:
                print("Opción no válida. Por favor, intente nuevamente.")
