import unittest
from Zad1.Password import *

class PasswordParameterizedFile(unittest.TestCase):

    def test_from_file(self):
      fileTest = open("data/password_data_test")
      tmpPassword = Password()
      for line in fileTest:
        if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
            continue
        else:
            data = line.split(" ")
            password, result = data[0], data[1].strip("\n")
            self.assertEqual(tmpPassword.ValidPassword(password), result)
      fileTest.close()


if __name__ == '__main__':
    unittest.main()
