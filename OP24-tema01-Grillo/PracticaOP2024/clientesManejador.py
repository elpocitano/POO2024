from clientesClass import cliente
from movimientosManejador import manejadorMovimientos
mMov = manejadorMovimientos()
mMov.carga()

class manejadorClientes:
    def __init__(self):
        self.__listaClientes = []

    def carga(self):
        with open("PracticaOP2024\ClientesAbril2024.csv") as fileClientes:
            next(fileClientes)
            for file in fileClientes:
                file = file.split(";")
                unCliente = cliente(file[0], file[1], file[2], file[3], float(file[4]))
                self.__listaClientes.append(unCliente)

    def modulo1(self):
        band = False
        xDNI = input("Ingrese DNI para actualizar saldo > ")
        i = 0

        while i<len(self.__listaClientes) and not band:
            if (self.__listaClientes[i].getDNI()==xDNI):
                print(f"Cliente {self.__listaClientes[i].getNombre()} - Numero Tarjeta {self.__listaClientes[i].getNum()} \n Saldo ${self.__listaClientes[i].getSaldo()}")
                saldoNuevo = self.__listaClientes[i].getSaldo()               
                saldoNuevo = mMov.obtenerMovimientos(self.__listaClientes[i].getNum(), self.__listaClientes[i].getSaldo())
                self.__listaClientes[i].actualizarSaldo(saldoNuevo)
                print(f"Saldo actualizado > ${self.__listaClientes[i].getSaldo()}")
                band = True
            i += 1

            
    def modulo2(self):
        numT = input("Ingrese numero de tarjeta > ")
        band = False
        i = 0

        while not band and i < len(self.__listaClientes):
            if self.__listaClientes[i].getNum() == numT:
                
                if not mMov.movimientosAbril(self.__listaClientes[i].getNum()):
                    print(self.__listaClientes[i].getNombre())
                if mMov.movimientosAbril(self.__listaClientes[i].getNum()):
                    print("El cliente si tuvo movimientos en Abril 2024.")
                band = True
            
            i += 1