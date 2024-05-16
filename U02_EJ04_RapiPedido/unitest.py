# -*- coding: utf-8 -*-
"""
Luna Juan Marcelo
DNI 24234578
@author: elpocitano@gmail.com
"""

import unittest
from moto import Moto
from pedido import Pedido


# plantilla para los test
class TestMoto(unittest.TestCase):
    def setUp(self): # Configuracion del ambiente
        self.moto = Moto("Honda", "ABC123", "Juan", "Perez", 10000.0)

    def test_get_patente(self):
        self.assertEqual(self.moto.get_patente(), "ABC123")

    def test_get_nombre_conductor(self):
        self.assertEqual(self.moto.get_nombre(), "Juan")

    def test_get_apellido_conductor(self):
        self.assertEqual(self.moto.get_apellido(), "Perez")


class TestPedido(unittest.TestCase):
    def setUp(self):
        self.pedido = Pedido("ABC123", "5", 20, 3000.5, 50)

    def test_patente_moto(self):
        self.assertEqual(self.pedido.patente_moto, "ABC123")

    def test_id_pedido(self):
        self.assertEqual(self.pedido.id_pedido, "1")

    # Añade más métodos de prueba para otros atributos y métodos de la clase Pedido


if __name__ == '__main__':
    unittest.main()
