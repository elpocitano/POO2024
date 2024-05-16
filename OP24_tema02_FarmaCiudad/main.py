# -*- coding: utf-8 -*-
"""
propsd + TAB
Luna Juan Marcelo
DNI 24234578
@author: elpocitano@gmail.com
a. Leer por teclado el dni de un Cliente, y actualice el saldo del cliente, sumando los créditos y
restando los pagos realizados, éstos últimos datos, obtenidos del Gestor de Movimientos,
emitiendo el siguiente listado:
   6.
   Cliente: (apellido y nombre)   Número de Cuenta: xxxx-xxxx      Saldo anterior: xxxxxxxx.xx
   Movimientos
   Fecha        Descripción         Importe     Tipo de movimiento
   xx/xx/xx xx  xxxxxxxxxxxxxxxxx   xxxxxx.xx   x
   xx/xx/xx xx  xxxxxxxxxxxxxxxxx   xxxxxx.xx   x
   xx/xx/xx xx  xxxxxxxxxxxxxxxxx   xxxxxx.xx   x
   Saldo actualizado: xxxxxxxx.xx
"""
from gestor_cliente import GC
from gestor_movimiento import GM
from cliente import Cliente
from movimiento import Movimiento

# Menu opciones de usuario


def menu():
    op : int
    op = int(input("""###### Menu Principal ######
                       Ingrese la opcion deseada:
                       1 : Ingrese el DNI para pagar los movimientos y ajustar saldo.
                       2 : Ingrese el DNI para informar movimientos en abril.
                       3 : Ordenar lista de movimientos por número de cuenta.
                       4 : Listar Movimientos.
                       5 : Listar Clientes.
                       0 : Salir.
                       -> """))
    return op


# a. Leer por teclado el dni de un Cliente, y actualice el saldo del cliente, sumando los créditos y
# restando los pagos realizados, éstos últimos datos, obtenidos del Gestor de Movimientos,
# emitiendo el siguiente listado:
def actualizar_saldo_anterior_x_dni(xdni : str):
    print("gc.get_num_cuenta_x_dni(xdni)")
    num_cta = gc.get_num_cuenta_x_dni(xdni)
    print(f"Numero de cuenta : {num_cta}")
    if num_cta != -1:
        print("gc.get_indice_x_dni(xdni)")
        indice_cliente = gc.get_indice_x_dni(xdni)
        print("gc.clientes_lista[indice_cliente]")
        cliente = gc.clientes_lista[indice_cliente]
        print("gm.mostrar_movi_x_num_cta(num_cta)")
        gm.mostrar_movi_x_num_cta(num_cta)
        print("gm.get_balance_x_num_cta(num_cta)")
        balance_movi_num_cta = gm.get_balance_x_num_cta(num_cta)
        print(f"Movimientos del num cta: $ {balance_movi_num_cta}")
        print(f"Saldo original del cliente : $ {cliente.get_saldo_anterior()}")
        print("cliente.actualizar_saldo(balance_movi_num_cta)")
        gc.actualizar_saldo_x_dni(xdni, balance_movi_num_cta)
        # cliente.actualizar_saldo(balance_movi_num_cta)
        print(f"Nuevo saldo del cliente: $ {cliente.get_saldo_anterior()}")
    else:
        print("DNI no encontrado.")


# b. Leer por teclado un dni, e informar por pantalla apellido y nombre del Cliente, si este, no tuvo
# movimientos durante el mes de abril 2024.
def movimientos_x_dni(xdni):
    indice_client = gc.get_indice_x_dni(xdni)
    if indice_client != -1:
        client = gc.clientes_lista[indice_client]
        ctdad_movi_client = gm.ctdad_mov_x_num_cta(client.get_num_cta())
        if ctdad_movi_client != -1:
            gm.mostrar_movi_x_num_cta(client.get_num_cta())
        else:
            print(f"El cliente {client.get_apel()} {client.get_nomb()} no registra movimientos en abril")
    else:
        print(f"DNI {xdni} no encontrado")


# c. Ordenar el Gestor de Movimientos por número de cuenta,
# para facilitar el procesamiento del punto a.
def ordenar_lista_movimientos():
    gm.ordenar_movi_x_num_cuenta()


if __name__ == "__main__":
    gc = GC()
    gm = GM()
    csv_file_clientes : str = "ClientesFarmaCiudad.csv"
    csv_file_movimientos : str = "MovimientosAbril2024.csv"
    print("Carga de archivo clientes.")
    gc.cargar_archivo_clientes(csv_file_clientes)
    print("Carga de archivo movimientos.")
    gm.cargar_archivo_movimientos(csv_file_movimientos)
    opcion : int
    print("Ingreso al menu.")
    opcion = menu()
    while opcion != 0:
        match opcion:
            case 1: # Ingrese el DNI para pagar los movimientos y ajustar saldo.
                dni = input("Ingrese el DNI del cliente.")
                actualizar_saldo_anterior_x_dni(dni)
            case 2: # Ingrese el DNI para informar movimientos en abril.
                dni = input("Ingrese el DNI del cliente.")
                movimientos_x_dni(dni)
            case 3: # Ordenar lista de movimientos por número de cuenta.
                ordenar_lista_movimientos()
            case 4: # Listar Movimientos.
                gm.listar_movimientos()
            case 5: # Listar Clientes.
                gc.listar_clientes()
            case _:
                print("Opcion invalida.")
        opcion = menu()
