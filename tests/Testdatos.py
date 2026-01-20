import unittest
from src.logica.Datos import Datos


class TestDatos(unittest.TestCase):
    def test_conjunto_vacio_retornaNone(self):
        datos = Datos([])
        self.assertIsNone(datos.desviacion())

    def test_conjunto_unElemento_retornaValorZERO(self):
        datos = Datos([5])
        self.assertEqual(0, datos.desviacion())
