import unittest
class Calculator:
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y
    
    

class CalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(11, self.calc.add(3, 7), "The addition is wrong")

    def test_subtract(self):
        self.assertEqual(12, self.calc.subtract(15, 3), "Subtraction is wrong")


if __name__ == '__main__':
    unittest.main()

   
