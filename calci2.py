import unittest
class Calculator:
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        if y == 0:
            raise ValueError("Division by zero is not allowed")
        return x / y

class CalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_multiply(self):
        self.assertEqual(30, self.calc.multiply(5, 6), "Multiplication is wrong")

    def test_divide(self):
        self.assertEqual(3, self.calc.divide(6, 2), "Division is wrong")

if __name__ == '__main__':
    unittest.main()

   
