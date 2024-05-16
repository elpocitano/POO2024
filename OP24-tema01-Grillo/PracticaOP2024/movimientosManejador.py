from movimientosClass import movimiento

class manejadorMovimientos:
    def __init__(self):
        self.__listaMovimientos =  []

    def carga(self):
        with open("PracticaOP2024/MovimientosAbril2024.csv") as fileMov:
            next(fileMov)
            for file in fileMov:
                file = file.split(";")
                unMov = movimiento(file[0], file[1],file[2],file[3],float(file[4]))
                self.__listaMovimientos.append(unMov)
    
    def obtenerMovimientos(self, numTarjeta, saldoRestante):
        saldoNuevo = saldoRestante
        for i in range(len(self.__listaMovimientos)):
            if self.__listaMovimientos[i].getNum() == numTarjeta:
                self.__listaMovimientos[i].getMovimiento()
                if self.__listaMovimientos[i].getTipo() == 'P':
                    saldoNuevo -= self.__listaMovimientos[i].getImporte()
                if self.__listaMovimientos[i].getTipo() == 'C':
                    saldoNuevo += self.__listaMovimientos[i].getImporte()
        return saldoNuevo
    
    def movimientosAbril(self, numT):
        band = False
        i = 0

        while i < len(self.__listaMovimientos) and not band:
            if self.__listaMovimientos[i].getNum() == numT:
                fecha = self.__listaMovimientos[i].getFecha().split("/")
                if fecha[1] == '4' and fecha[2] == '2024':
                    band = True
            i += 1

        return band
    
    def ordenar(self):
        self.__listaMovimientos.sort()
        for i in range(len(self.__listaMovimientos)):
            print(self.__listaMovimientos[i].getNum())