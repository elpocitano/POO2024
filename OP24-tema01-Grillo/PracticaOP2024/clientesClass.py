class cliente:
    __nombre = str
    __apellido = str
    __dni = str
    __numTarjeta = str
    __saldoAnterior = float

    def __init__(self, nombre, apellido, dni, numTarjeta, saldoAnterior):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__numTarjeta = numTarjeta
        self.__saldoAnterior = saldoAnterior

    def getSaldo(self):
        return self.__saldoAnterior
    
    def getNombre(self):
        return (self.__apellido + ' ' + self.__nombre)
    
    def getNum(self):
        return self.__numTarjeta
    
    def getDNI(self):
        return self.__dni
    
    def actualizarSaldo(self, saldoNuevo):
        self.__saldoAnterior = saldoNuevo