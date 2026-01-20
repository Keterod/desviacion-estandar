import unittest
from src.logica.Datos import Datos


class TestDatos(unittest.TestCase):
    def test_conjunto_vacio_retornaNone(self):
        datos = Datos([])
        self.assertIsNone(Datos.desviacion(self))
