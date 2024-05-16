from gestorClientes import GestorCliente
from gestorMovimientos import GestorMovimiento
class Menu:
    __gestorCliente: GestorCliente
    __gestorMovimiento: GestorMovimiento
    __opcionesDict:dict
    __opcionesList:list
    def __init__(self):
        self.__gestorCliente = GestorCliente()
        self.__gestorMovimiento = GestorMovimiento()
        self.__opcionesDict = dict(a=self.opcionA,b=self.opcionB,c=self.opcionC)
        self.__opcionesList = ["a)Actualizar Saldo(ingrese a)","b)Verificar si tiene movimientos(ingrese b)"]
    def opcionA(self):
        dni = input("ingrese dni")
        self.__gestorCliente.actSaldo(int(dni),self.__gestorMovimiento)
        self.showMenu()
    def opcionB(self):
        dni = input("ingrese dni")
        self.__gestorCliente.verificarMov(int(dni),self.__gestorMovimiento)
        self.showMenu()
    def showMenu(self):
        for i in self.__opcionesList:
            print(i)
        opcion = input("ingrese opcion a realizar")
        self.__opcionesDict[opcion]()
if __name__ == "__main__":
    menu = Menu()
    menu.showMenu()