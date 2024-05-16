class movimiento:
    __numTarjeta = str
    __fecha = str
    __descripcion = str
    __tipoMvto = str
    __importe = float

    def __init__(self, numTarjeta, fecha, descripcion, tipoMvto, importe):
        self.__numTarjeta = numTarjeta
        self.__fecha = fecha
        self.__descripcion = descripcion
        self.__tipoMvto = tipoMvto
        self.__importe = importe

    def getNum(self):
        return self.__numTarjeta

    def getMovimiento(self):
        print(f"Fecha {self.__fecha} Descripcion {self.__descripcion} Importe ${self.__importe} Tipo Mov {self.__tipoMvto}")

    def getImporte(self):
        return self.__importe
    
    def getTipo(self):
        return self.__tipoMvto
    
    def getFecha(self):
        return self.__fecha
    
    def __lt__(self, other):
        return self.__numTarjeta < other.getNum()