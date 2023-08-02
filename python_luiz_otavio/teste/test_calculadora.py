import unittest

from calculadora import somar, subtrai


class TestCalculadora(unittest.TestCase):
    def test_soma_5_e_5_deve_retornar_10(self):
        self.assertEqual(somar(5, 5), 10)

    def test_subtrai_10_e_5_deve_retornar_5(self):
        self.assertEqual(subtrai(10, 5), 5)

    def test_somar_varias_entradas(self):
        x_y_saidas = (
            (10, 10, 20),
            (5, 10, 15),
            (1.5, 1.5, 3.0),
            (11, 21, 32),
            (-5, 5, 0),
            (100, 100, 200),
            (15, 15, 30),
        )
        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(somar(x, y), saida)

    def test_soma_x_nao_e_init_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            somar("11", 0)

    def test_soma_y_nao_e_init_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            somar(1, "11")


unittest.main(verbosity=2)
