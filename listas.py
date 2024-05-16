# -*- coding: utf-8 -*-
"""
Luna Juan Marcelo
DNI 24234578
@author: elpocitano@gmail.com
"""

if __name__ == '__main__':
    lista = [3, 6, 9, 2 , 10, 34, 21, 56, 33, 75]
    print('Lista original: ', lista)

    # Agregar un elemento al final de la lista
    lista.append(80)
    print('Lista.append(80): ', lista)

    # Elimina un elemento por indice y lo retorna
    pop = lista.pop(3)
    print(format('Lista.pop(3): {} y eliminado {}'.format(lista, pop)))
    print(f'Lista.pop(3): {lista} y eliminado {pop}')

    # Remover un elemento por valor
    lista.remove(9)
    print('Lista.remove(9): ', lista)

    # Retorna indice de un valor en lista
    lista.index(33)
    print('Lista.index(33): ', lista.index(33))

    # metodos de listas
    print('# metodos de listas')
    x = list()
    dir(x)
    print(dir(x))
    print(lista.count(34))
    lista.append(34)
    print(lista.count(34))
    print(lista.__contains__(10))
    print(23 in lista)
