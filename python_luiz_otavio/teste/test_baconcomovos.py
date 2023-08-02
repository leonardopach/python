import unittest
from baconcomovos import bacon_com_ovos


class TestBaconComOvos(unittest.TestCase):
    def test_bacon_com_ovos(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos("0")


unittest.main(verbosity=2)
