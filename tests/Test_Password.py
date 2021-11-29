import unittest
from src.Zad1.Password import *

class PasswordTest(unittest.TestCase):
    
    def setUp(self):
        self.temp = Password()

    def test_Password_Exceptions_None(self):
        self.assertRaises(Exception, self.temp.ValidPassword, None)
    def test_Password_Exceptions_Boolean(self):
        self.assertRaises(Exception, self.temp.ValidPassword, True)
    def test_Password_Exceptions_int(self):
        self.assertRaises(Exception, self.temp.ValidPassword, 2)
    def test_Password_Exceptions_float(self):
        self.assertRaises(Exception, self.temp.ValidPassword, 2.5)
    def test_Password_Exceptions_array(self):
        self.assertRaises(Exception, self.temp.ValidPassword, [1,2,3])
    def test_Password_Exceptions_object(self):
        self.assertRaises(Exception, self.temp.ValidPassword, {})
        
    def tearDown(self):
        self.temp = None 

if __name__ == '__main__':
    unittest.main()
