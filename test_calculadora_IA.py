# test_calculadora_IA.py

import unittest

from calculadora import potencia


class TestCalculadora(unittest.TestCase):
    def test_potencia_inteiros_positivos(self):
        self.assertEqual(potencia(2, 3), 8)

    def test_potencia_expoente_um(self):
        self.assertEqual(potencia(7, 1), 7)

    def test_potencia_expoente_zero(self):
        self.assertEqual(potencia(5, 0), 1)

    def test_potencia_base_zero_expoente_positivo(self):
        self.assertEqual(potencia(0, 4), 0)

    def test_potencia_expoente_negativo(self):
        self.assertEqual(potencia(2, -2), 0.25)

    def test_potencia_base_negativa_expoente_impar(self):
        self.assertEqual(potencia(-2, 3), -8)

    def test_potencia_base_negativa_expoente_par(self):
        self.assertEqual(potencia(-2, 4), 16)

    def test_potencia_numeros_decimais(self):
        self.assertEqual(potencia(2.5, 2), 6.25)

    def test_potencia_zero_elevado_zero(self):
        self.assertEqual(potencia(0, 0), 1)

    def test_potencia_base_expoente_negativos(self):
        self.assertEqual(potencia(-2, -3), -0.125)