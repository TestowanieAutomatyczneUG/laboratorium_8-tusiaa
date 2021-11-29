import unittest
from src.Zad1.Password import *
from parameterized import parameterized, parameterized_class

class PasswordParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = Password()

    @parameterized.expand([
        ("Has1*", False),
        ("haslo.bez.duzej.litery123", False),
        ("Haslo.bez.liczby", False),
        ("HasloBezZnaku123", False),
    ])
    def test_one_parameterized(self, password, expected):
        self.assertEqual(self.tmp.ValidPassword(password), expected)


@parameterized_class(('password', 'expected'), [
    ("haslotylkozliczba123", False),
    ("HasloTylkoZDuzaLitera", False),
    ("haslo.tylko.z.znakiem", False),
    ("Prawidlowe.Haslo123", True),
])
class PasswordParameterizedPackage2(unittest.TestCase):
    def setUp(self):
        self.tmp = Password()

    def test_two_parameterized(self):
        self.assertEqual(self.tmp.ValidPassword(self.password), self.expected)


if __name__ == '__main__':
    unittest.main()
