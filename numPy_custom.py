# -*- coding: utf-8 -*-
"""
Luna Juan Marcelo
DNI 24234578
@author: elpocitano@gmail.com
"""
import numpy as np


class NpCustom:
    def __init__(self, data):
        self.data = np.array(data)

    # Sobrecargamos el metodo suma para que en vez de sumar cada componente de los arreglos
    # concatene un arreglo con otro. Si bien ya existe esa funcion es a fines practicos
    def __add__(self, other):
        new_data = np.concatenate((self.data, other.data))
        return NpCustom(new_data)

    def __repr__(self):
        return repr(self.data)


if __name__ == '__main__':
    lista01 = [3, 2, 5, 6]
    print('Lista 01:', lista01)
    lista02 = [5, 7, 8, 9]
    print('Lista 02:', lista02)

    arre_np01 = NpCustom(lista01)
    print('Arreglo np01:', arre_np01)
    arre_np02 = NpCustom(lista02)
    print('Arreglo np02:', arre_np02)

    arre_np03 = arre_np01 + arre_np02
    print('np01 + np02:', arre_np03)

    arre_np04 = np.concatenate((arre_np01.data, arre_np02.data))
    print(arre_np04)
