from unittest import TestCase
from Matriz import matriz_randomica, multi_processo, sequencial, multi_processo
import numpy as np


class TestMatriz(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.matriz_1 = matriz_randomica(10, 10)
        cls.matriz_2 = matriz_randomica(10, 10)
        cls.resultado = np.dot(cls.matriz_1, cls.matriz_2)
        cls.shape = np.zeros(
            (np.shape(cls.matriz_1)[0], np.shape(cls.matriz_2)[1]), 
            dtype=int
        )
        

    def test_sequencial(self):
        np.testing.assert_array_equal(
            sequencial(self.matriz_1, self.matriz_2, self.shape), 
            self.resultado
        )

    def test_multi_processo(self):
        np.testing.assert_array_equal(
            multi_processo(self.matriz_1, self.matriz_2, self.shape), 
            self.resultado
        )
        
        