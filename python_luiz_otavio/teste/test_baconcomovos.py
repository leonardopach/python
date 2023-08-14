import unittest
from baconcomovos import bacon_com_ovos


class TestBaconComOvos(unittest.TestCase):
    def test_bacon_com_ovos(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos("0")

    def test_bacon_com_ovos_deve_retornar_bacon_com_ovos_se_entrada_for_multiplo_de_3_e_5(
        self,
    ):
        entradas = (15, 30, 45, 60)
        saida = "Bacon com ovos"

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f'"{entrada}" não retornou "{saida}"',
                )

    def test_bacon_com_ovos_deve_retornar_passar_fome_se_entrada_nao_for_multiplo_de_3_e_5(
        self,
    ):
        entradas = (1, 2, 4, 7, 8)
        saida = "Passar fome"

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f'"{entrada}" não retornou "{saida}"',
                )


unittest.main(verbosity=2)
