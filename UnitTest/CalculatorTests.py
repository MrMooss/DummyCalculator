import unittest
from Calculator.EasyOperations import *
from Calculator.HarderOperations import *


class CalculatorTest(unittest.TestCase):
    def test_add(self):
        """
        Test that the add is works correctly
        """
        num1, num2 = 2, 3
        result = Add.preform(self, num1, num2)

        self.assertEqual(result, 5)

    def test_subtract(self):
        """
        Test that the subtract is works correctly
        """
        num1, num2 = 5, 3
        result = Subtract.preform(self, num1, num2)

        self.assertEqual(result, 2)

    def test_divide(self):
        """
        Test that the divide works correctly
        """
        num1, num2 = 4, 2
        result = Divide.preform(self, num1, num2)

        self.assertEqual(result, 2)

    def test_multiply(self):
        """
        Test that the multiplication works correctly
        """
        num1, num2 = 2, 6
        result = Multiply.preform(self, num1, num2)

        self.assertEqual(result, 12)


if __name__ == '__main__':
    unittest.main()
