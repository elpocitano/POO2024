# -*- coding: utf-8 -*-
"""
Módulo Gestor de Reservas
Luna Juan Marcelo
DNI 24234578
elpocitano@gmail.com

Este módulo proporciona la clase GestorReservas, que se encarga de administrar
las reservas de cabañas para el complejo "El Soleado".

Funcionalidades:
- Carga las reservas desde un archivo CSV.
- Permite buscar reservas por número de cabaña.
- Lista las reservas para una fecha específica.

"""

from models.reserva import Reserva

class GestorReservas:
    """
    Clase para gestionar las reservas de cabañas.

    Atributos:
    __lista_reservas (list): Lista que almacena las instancias de la clase Reserva.

    Métodos:
    __init__(): Constructor de la clase GestorReservas.
    agregar_reserva(reserva): Agrega una reserva a la lista de reservas.
    cargar_archivo_reservas(csv_file): Carga las reservas desde un archivo CSV.
    listar_reservas(): Lista todas las reservas almacenadas.
    buscar_num_cab_reservas(num_cabania_consulta): Busca una reserva por número de cabaña.
    listar_reservas_fecha(fecha): Lista las reservas para una fecha específica.
    """

    def __init__(self):
        """Constructor de la clase GestorReservas."""
        self.__lista_reservas = []

    def agregar_reserva(self, reserva):
        """Agrega una reserva a la lista de reservas."""
        self.__lista_reservas.append(reserva)

    def cargar_archivo_reservas(self):
        """
        Carga las reservas desde un archivo CSV.

        Parámetros:
        csv_file (str): Ruta del archivo CSV que contiene los datos de las reservas.
        """
        csv_file = "../data/Reservas.csv"
        with open(csv_file) as csv_handler:
            next(csv_handler)
            for fila in csv_handler:
                atributos_reserva = fila.replace(" ", "").replace('"', '').split(';')
                una_reserva = Reserva(*atributos_reserva)
                self.agregar_reserva(una_reserva)

    def listar_reservas(self):
        """Lista todas las reservas almacenadas."""
        for reserva in self.__lista_reservas:
            print(reserva)

    def buscar_num_cab_reservas(self, num_cabania_consulta: int) -> int:
        """
        Busca una reserva por número de cabaña.

        Parámetros:
        num_cabania_consulta (int): Número de cabaña a buscar.

        Retorna:
        int: Índice de la reserva si se encuentra, -1 si no se encuentra.
        """
        encontrado = -1
        for i, reserva in enumerate(self.__lista_reservas):
            if int(reserva.get_num_cabania()) == num_cabania_consulta:
                encontrado = i
        return encontrado

    def listar_reservas_fecha(self, fecha: str) -> None:
        """
        Lista las reservas para una fecha específica.

        Parámetros:
        fecha (str): Fecha en formato 'dd/mm/yyyy' para buscar las reservas.
        """
        print(f"# Reservas para la fecha: {fecha} #")
        for res in self.__lista_reservas:
            if res.get_fecha() == fecha:
                print(f"""
            N° de cabaña             Importe diario              Cantidad días          Seña                      Importe a cobrar
            {res.get_num_reserva()}  {res.get_importe_diario()}  {res.get_cant_dias()}  {res.get_import_senia()}  {res.get_importe_cobrar()}""")

if __name__ == "__main__":
    GR = GestorReservas()
    GR.cargar_archivo_reservas()
    GR.listar_reservas()
    is_num_cabania_reservada = GR.buscar_num_cab_reservas(4)
    if GR.buscar_num_cab_reservas(4) == -1:
        print("Cabaña 4 esta libre.")
    else:
        print("La cabaña 3 esta reservada")
    is_num_cabania_reservada = GR.buscar_num_cab_reservas(3)
    if GR.buscar_num_cab_reservas(9) == -1:
        print("Cabaña 9 esta libre.")
    else:
        print("Cabaña 9 esta reservada.")