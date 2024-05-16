# -*- coding: utf-8 -*-
"""
propsd + TAB
Luna Juan Marcelo
DNI 24234578
@author: elpocitano@gmail.com
2. Escriba el código de un Gestor de Clientes, que permita almacenar los datos de todos los
Clientes de la farmacia, para el mes de abril del 2024. Este gestor debe basarse en una lista del
lenguaje Python.
4. Leer los datos del archivo “ClientesFarmaCiudad.csv”, y almacenarlos en el Gestor de Clientes.

"""

from cliente import Cliente


class GC:

    def __init__(self):
        self.clientes_lista = []

    def agregar_cliente(self, cliente: Cliente):
        self.clientes_lista.append(cliente)

    def listar_clientes(self):
        for cliente in self.clientes_lista:
            print(cliente.get_nomb())

    def get_indice_x_dni(self, dni):
        indice = 0
        encontrado = -1
        while (indice < len(self.clientes_lista)) and (encontrado == -1):
            if self.clientes_lista[indice].get_dni() == dni:
                encontrado = indice
            indice += 1
        return encontrado

    def get_num_cuenta_x_dni(self, dni):
        indice = 0
        encontrado = -1
        while (indice < len(self.clientes_lista)) and (encontrado == -1):
            cliente = self.clientes_lista[indice]
            if cliente.get_dni() == dni:
                encontrado = cliente.get_num_cta()
            indice += 1
        return encontrado

    def actualizar_saldo_x_dni(self, dni, balance):
        indice = 0
        encontrado = -1
        while (indice < len(self.clientes_lista)) and (encontrado == -1):
            cliente = self.clientes_lista[indice]
            if cliente.get_dni() == dni:
                encontrado = indice
                print(f"Saldo de cuenta: $ {cliente.get_saldo_anterior()}.")
                cliente.actualizar_saldo(balance)
                print(f"Nuevo saldo: $ {cliente.get_saldo_anterior()}.")
            indice += 1
        return encontrado

    def cargar_archivo_clientes(self, csv_file):
        with open(csv_file) as archivo:
            next(archivo)
            for linea in archivo:
                atributos = linea.replace(" ","").split(";")
                nomb, apel, dni, num_cta, saldo = atributos
                cliente = Cliente(nomb, apel, dni, num_cta, saldo)
                self.agregar_cliente(cliente)
                print("Carga exitosa")


if __name__ == "__main__":
    gc = GC()
    gc.cargar_archivo_clientes("ClientesFarmaCiudad.csv")
    gc.listar_clientes()
    gc.agregar_cliente(Cliente("Luna", "Juan", "24234578", 34245, 56500 ))
    gc.listar_clientes()
    dni = "44777888"
    print(f"Numero de cuenta del dni 44777888")
    num_cta = gc.get_num_cuenta_x_dni(dni)
    print(num_cta)
    print("Obtener indice del DNI 44777888.")
    indice_cuenta = gc.get_indice_x_dni(dni)
    print(indice_cuenta)
    balance = 54650.50
    gc.actualizar_saldo_x_dni(dni, balance)







