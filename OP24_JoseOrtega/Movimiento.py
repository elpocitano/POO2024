class Movimieto:
    __numCuenta:int
    __fecha:str
    __desc:str
    __tipoMov:str
    __importe:float
    def __init__(self,num,fecha,desc,tipoMov,importe):
        self.__numCuenta = num
        self.__fecha = fecha
        self.__desc = desc
        self.__tipoMov = tipoMov
        self.__importe = importe
    def __It__(self,otro):
        return self.getNroCuenta() < otro.getNroCuenta()
    def getNroCuenta(self):
        return self.__numCuenta
    def getFecha(self):
        return self.__fecha
    def getDesc(self):
        return self.__desc
    def getTipoMov(self):
        return self.__tipoMov
    def getImporte(self):
        return self.__importe