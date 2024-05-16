import numpy as np
import csv
from Movimiento import Movimieto
class GestorMovimiento:
    __movimientos:list
    def __init__(self):
        self.__movimientos = np.array([])
        with open("MovimientosAbril2024.csv","r",newline="") as csvFile:
            reader = csv.reader(csvFile,delimiter=";")
            for i in reader:
                if i[0] != "numCuenta":
                    newMov = Movimieto(int(i[0]),str(i[1]),str(i[2]),str(i[3]),float(i[4]))
                    self.__movimientos =np.append(self.__movimientos, newMov)
    def getSaldoNuevo(self,nroCuenta,saldoAnt):
        saldoAnt = saldoAnt
        i=0
        while i < len(self.__movimientos):
            if self.__movimientos[i].getNroCuenta() == nroCuenta:
                if self.__movimientos[i].getTipoMov() == "C":
                    saldoAnt = saldoAnt + self.__movimientos[i].getImporte()
                elif self.__movimientos[i].getTipoMov() == "P":
                    saldoAnt = saldoAnt - self.__movimientos[i].getImporte()
            i = i+1
        return saldoAnt
    def printMov(self,nroCuenta):
        i =0
        while i < len(self.__movimientos):
            mov = self.__movimientos[i]
            if mov.getNroCuenta() == nroCuenta:
                print(f"Fecha: {mov.getFecha()},Descripcion: {mov.getDesc()},Importe: {mov.getImporte()},Tipo de Movimiento: {mov.getTipoMov()}")
            i = i+1
    def verificarMov(self,numC):
        bandera = True
        i=0
        while i < len(self.__movimientos):
            if (numC == self.__movimientos[i].getNroCuenta()):
                bandera = False
            i = i+1
        return bandera