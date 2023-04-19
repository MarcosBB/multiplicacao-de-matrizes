from unittest import TestCase
from Matriz import matriz_randomica, multi_processo, sequencial, multi_processo
import numpy


class TestMatriz(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.matriz_1 = matriz_randomica(10, 10)
        cls.matriz_2 = matriz_randomica(10, 10)
        cls.resultado = np.dot(cls.matriz_1, cls.matriz_2)
        cls.shape = [[0 for j in range(len(cls.matriz_2[0]))] for i in range(len(cls.matriz_1))]

    def test_sequencial(self):
        numpy.testing.assert_array_equal(
            sequencial(self.matriz_1, self.matriz_2, self.shape), 
            self.resultado
        )

    def test_multi_processo(self):
        numpy.testing.assert_array_equal(
            multi_processo(self.matriz_1, self.matriz_2, self.shape), 
            self.resultado
        )
        
        