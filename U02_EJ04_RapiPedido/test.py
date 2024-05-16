# -*- coding: utf-8 -*-
"""
Luna Juan Marcelo
DNI 24234578
@author: elpocitano@gmail.com
"""
import unittest
from gestor_motos import GestorMotos
from gestor_pedidos import GestorPedidos
from moto import Moto
from pedido import Pedido


class TestGestorMotos(unittest.TestCase):
    # Crea una instancia de Moto, la agrega a la lista del gestor y comprueba el resultado
    def test_agregar_moto(self):
        gm = GestorMotos()
        moto = Moto("Honda", "ABC123", "Juan", "Perez", 100.0)
        gm.agregar_moto(moto)
        # Comprueba si el objeto moto se encuentra en la lista del manejador
        self.assertIn(moto, gm.lista_motos)

    def test_eliminar_moto_por_indice(self):
        gm = GestorMotos()
        moto = Moto("Honda", "ABC123", "Juan", "Perez", 100.0)
        gm.agregar_moto(moto)
        gm.eliminar_moto_por_indice(0)

        self.assertNotIn(moto, gm.lista_motos)

    def test_buscar_moto_por_patente(self):
        gm = GestorMotos()
        moto = Moto("Honda", "ABC123", "Juan", "Perez", 100.0)
        gm.agregar_moto(moto)
        indice = gm.buscar_moto_por_patente("ABC123")
        self.assertEqual(indice, 0)

    # Agrega más métodos de prueba para GestorMotos según sea necesario


class TestGestorPedidos(unittest.TestCase):
    def test_agregar_pedido(self):
        gp = GestorPedidos()
        pedido = Pedido("1", 2, 30, 150.0, "ABC123", 0)
        gp.agregar_pedido(pedido)
        self.assertIn(pedido, gp.lista_pedidos)

    def test_actualizar_tiempo_real(self):
        gp = GestorPedidos()
        pedido = Pedido("1", 2, 30, 150.0, "ABC123", 0)
        gp.agregar_pedido(pedido)
        gp.actualizar_tiempo_real(0, 40)
        self.assertEqual(gp.lista_pedidos[0].get_tiempo_entrega_real(), 40)

    # Agrega más métodos de prueba para GestorPedidos según sea necesario


class TestMoto(unittest.TestCase):
    def test_constructor_moto(self):
        moto = Moto("Honda", "ABC123", "Juan", "Perez", 100.0)
        self.assertEqual(moto.get_patente(), "ABC123")

    # Agrega más métodos de prueba para la clase Moto según sea necesario


class TestPedido(unittest.TestCase):
    def test_constructor_pedido(self):
        pedido = Pedido("1", 2, 30, 150.0, "ABC123", 0)
        self.assertEqual(pedido.get_id_pedido(), "1")

    # Agrega más métodos de prueba para la clase Pedido según sea necesario


if __name__ == '__main__':
    unittest.main()
