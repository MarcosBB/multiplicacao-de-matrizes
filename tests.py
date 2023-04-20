from unittest import TestCase
from matriz import multi_processo, sequencial, multi_thread
from utils import matriz_randomica, divide_linhas_por_partes
import numpy


class TestMatriz(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.matriz_1 = matriz_randomica(10, 10)
        cls.matriz_2 = matriz_randomica(10, 10)
        cls.resultado = numpy.dot(cls.matriz_1, cls.matriz_2)
        cls.shape = [[0 for j in range(len(cls.matriz_2[0]))] for i in range(len(cls.matriz_1))]

    def test_sequencial(self):
        numpy.testing.assert_array_equal(
            sequencial(self.matriz_1, self.matriz_2), 
            self.resultado
        )

    def test_multi_processo(self):
        numpy.testing.assert_array_equal(
            multi_processo(self.matriz_1, self.matriz_2, 5), 
            self.resultado
        )
        
    def test_multi_processo_com_divisao_em_partes_nao_exatas(self):
        numpy.testing.assert_array_equal(
            multi_processo(self.matriz_1, self.matriz_2, 4), 
            self.resultado
        )

    def test_multi_thread(self):
        numpy.testing.assert_array_equal(
            multi_thread(self.matriz_1, self.matriz_2, 5), 
            self.resultado
        )

    def test_multi_thread_com_divisao_em_partes_nao_exatas(self):
        numpy.testing.assert_array_equal(
            multi_thread(self.matriz_1, self.matriz_2, 4), 
            self.resultado
        )


class TestDivideLinhas(TestCase):
    def test_divide_linhas_por_partes_iguais(self):
        self.assertEqual(
            divide_linhas_por_partes(10, 5),
            [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]
        )

    def test_divide_linhas_por_partes_iguais_2(self):
        self.assertEqual(
            divide_linhas_por_partes(10, 2),
            [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
        )

    def test_divide_linhas_por_partes_iguais_3(self):
        self.assertEqual(
            divide_linhas_por_partes(10, 1),
            [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
        )

    def test_divide_linhas_por_partes_nao_iguais(self):
        self.assertEqual(
            divide_linhas_por_partes(10, 4),
            [[0, 1, 8], [2, 3, 9], [4, 5], [6, 7]]
        )
    
    def test_divide_linhas_por_partes_nao_iguais_2(self):
        self.assertEqual(
            divide_linhas_por_partes(10, 3),
            [[0, 1, 2, 9], [3, 4, 5], [6, 7, 8]]
        )
    