import csv
from Cliente import Cliente


class GestorCliente:
    __clientes:list

    def __init__(self):
        self.__clientes =[]
        with open("ClientesFarmaCiudad.csv","r",newline="") as csvFile:
            reader = csv.reader(csvFile,delimiter=";")
            for i in reader:
                if i[0] != "nombre":
                    self.__clientes.append(Cliente(str(i[0]),str(i[1]),int(i[2]),int(i[3]),float(i[4])))

    def actSaldo(self,dni,gestorMov):
        i = 0
        while i < len(self.__clientes) and self.__clientes[i].getDni() != dni:
            i = i+1
        if i > len(self.__clientes):
            print("cliente no encontrado")
        elif(self.__clientes[i].getDni() == dni):
            nroCuenta = self.__clientes[i].getNrocuenta()
            saldoAntiguo = self.__clientes[i].getSaldoAntiguo()
            saldoNuevo= gestorMov.getSaldoNuevo(nroCuenta,saldoAntiguo)
            nombre = self.__clientes[i].getNombre()
            apellido = self.__clientes[i].getApellido()
            print(f"Cliente:{nombre} {apellido}")
            print("NroCuenta: ",nroCuenta)
            print("saldo anterior: ",saldoAntiguo)
            print("Movimientos: ")
            gestorMov.printMov(nroCuenta)
            print("saldo actualizado: ",saldoNuevo)
    def verificarMov(self,dni,gestorMov):
        i = 0
        while i < len(self.__clientes) and self.__clientes[i].getDni() != dni:
            i = i+1
        if i > len(self.__clientes):
            print("cliente no encontrado")
        elif self.__clientes[i].getDni() == dni and i < len(self.__clientes):
            numCuenta = self.__clientes[i].getNrocuenta()
            res = gestorMov.verificarMov(numCuenta)
            if res == True:
                print(f"Cliente que no tuvo Movimentos: {self.__clientes[i].getNombre()} {self.__clientes[i].getApellido()}")
            elif res == False:
                print("El dni ingresado tine Movimientos") 