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
    __lista_reservas: list

    def __init__(self):
        self.__lista_reservas = []

    def agregar_reserva(self, reserva):
        self.__lista_reservas.append(reserva)

    def cargar_archivo_reservas(self, csv_file="Reservas.csv"):
        with open(csv_file) as csv_handler:
            next(csv_handler)
            for fila in csv_handler:
                atributos_reserva = fila.replace(" ", "").replace('"', '').split(';')
                una_reserva = Reserva(*atributos_reserva)
                self.agregar_reserva(una_reserva)

    def listar_reservas(self):
        for reserva in self.__lista_reservas:
            print(reserva)
    """
        # Busca el numero de cabaña en las reservas,
        # retorna indice de reserva also -1
        def buscar_num_cab_reservas(self, num_cabania_consulta) -> int:
            i = 0
            encontrado = -1
            while i < len(self.__lista_reservas) and encontrado == -1:
                reserva = self.__lista_reservas[i]
                num_cabania_reserv = int(reserva.get_num_cabania())
                if num_cabania_reserv == num_cabania_consulta:
                    encontrado = num_cabania_reserv
                i += 1
            return encontrado
    """
    def buscar_num_cab_reservas(self, num_cabania_consulta: int) -> int:
        encontrado = -1
        for i, reserva in enumerate(self.__lista_reservas):
            if int(reserva.get_num_cabania()) == num_cabania_consulta:
                encontrado = i
        return encontrado

    # Reservas para la fecha: xx/xx/xx
    # N° de cabaña   Importe diario    Cantidad días    Seña       Importe a cobrar
    def listar_reservas_fecha(self, fecha: str) -> None:
        print(f"# Reservas para la fecha: {fecha} #")
        for res in self.__lista_reservas:
            if res.get_fecha() == fecha:
                print(f"""
            N° de cabaña             Importe diario              Cantidad días          Seña                      Importe a cobrar
            {res.get_num_reserva()}  {res.get_importe_diario()}  {res.get_cant_dias()}  {res.get_import_senia()}  {res.get_importe_cobrar()}""")


if __name__ == "__main__":
    GR = GestorReservas()
    GR.cargar_archivo_reservas("Reservas.csv")
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

