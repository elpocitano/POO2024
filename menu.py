# -*- coding: utf-8 -*-
"""
Luna Juan Marcelo
DNI 24234578
@author: elpocitano@gmail.com
"""
import sys

def menu():
    opcion = int(input("#### Menu de Opciones ####"))
    if opcion == 1:
        print('\n## CUENTAS ##\n')
        cuentas.mostrar()
    elif opcion == 2:
        print('\n## TRANSACCIONES ##\n')
        print(transacciones)
    elif opcion == 3:
        infoCliente()
    elif opcion == 4:
        modPorecentajeAnual()
    elif opcion == 5:
        actualizarSaldo()
    elif opcion == 6:
        guardarCuentas()
    elif opcion == 0:
        print("\n########\n Programa Terminado  \n#########\n")
        sys.exit()

if __name__ == '__main__':
    while True:
        menu()