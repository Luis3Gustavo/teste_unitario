# test_calculadora.py

import unittest

from calculadora import (
    somar,
    subtrair,
    multiplicar,
    dividir,
    potencia,
    calcular_media,
)


class TestCalculadora(unittest.TestCase):

    def test_somar_com_varios_casos(self):
        casos = [
            (2, 3, 5),
            (-1, 1, 0),
            (0, 0, 0),
        ]

        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                self.assertEqual(somar(a, b), esperado)

    def test_subtrair_com_varios_casos(self):
        casos = [
            (10, 5, 5),
            (5, 10, -5),
            (0, 0, 0),
        ]

        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                self.assertEqual(subtrair(a, b), esperado)

    def test_multiplicar_com_varios_casos(self):
        casos = [
            (3, 4, 12),
            (5, 0, 0),
            (-2, 3, -6),
        ]

        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                self.assertEqual(multiplicar(a, b), esperado)

    def test_dividir_com_varios_casos(self):
        casos = [
            (10, 2, 5),
            (9, 3, 3),
            (5, 2, 2.5),
            (7, 2, 3.5),
            (-10, 2, -5.0),
            (10, -2, -5.0),
            (-10, -2, 5.0),
            (0, 5, 0.0),
            (8, 1, 8.0),
        ]

        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                self.assertEqual(dividir(a, b), esperado)

    def test_dividir_por_zero(self):
        with self.assertRaises(ZeroDivisionError):
            dividir(10, 0)

    def test_potencia_com_varios_casos(self):
        casos = [
            (2, 3, 8),
            (5, 0, 1),
            (10, 2, 100),
            (0, 4, 0),
            (0, 0, 1),
            (2, -2, 0.25),
            (-2, 3, -8),
            (-2, 4, 16),
            (2.5, 2, 6.25),
        ]

        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                self.assertEqual(potencia(a, b), esperado)

    def test_potencia_base_texto(self):
        with self.assertRaises(TypeError):
            potencia("abc", 2)

    def test_potencia_expoente_texto(self):
        with self.assertRaises(TypeError):
            potencia(2, "abc")

    def test_calcular_media_com_varios_casos(self):
        casos = [
            ([10, 20, 30, 40], 25),
            ([1.5, 6.5, 2.5, 4.5], 3.75),
            ([10], 10),
        ]

        for lista, esperado in casos:
            with self.subTest(lista=lista):
                self.assertEqual(calcular_media(lista), esperado)

    def test_calcular_media_lista_vazia(self):
        with self.assertRaises(ValueError):
            calcular_media([])


if __name__ == "__main__":
    unittest.main()