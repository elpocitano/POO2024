class Cliente:
    __nombre:str
    __apellido:str
    __dni:int
    __numeroCuenta:int
    __saldoAnterior:float
    def __init__(self,nom,ap,dni,numC,saldo):
        self.__nombre = nom
        self.__apellido = ap
        self.__dni = dni
        self.__numeroCuenta = numC
        self.__saldoAnterior =saldo
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getDni(self):
        return self.__dni
    def getNrocuenta(self):
        return self.__numeroCuenta
    def getSaldoAntiguo(self):
        return self.__saldoAnterior