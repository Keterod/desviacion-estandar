import unittest
from src.logica.Datos import Datos


class TestDatos(unittest.TestCase):
    def test_conjunto_vacio_retornaNone(self):
        datos = Datos([])
        self.assertIsNone(datos.desviacion())

    def test_conjunto_unElemento_retornaValorZERO(self):
        datos = Datos([5])
        self.assertEqual(0, datos.desviacion())
    def test_conjunto_nElementos_retornaPromedioNElementos( self ):
        datos=Datos([2,4,6,8])
        media=(2+4+6+8)/4
        suma_cuad=(((2-media)**2)+((4-media)**2)+((6-media)**2)+((8-media)**2))
        desvi= (suma_cuad/4) **0.5
        self.assertEqual(desvi,datos.desviacion())