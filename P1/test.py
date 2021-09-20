from Calculator import Calculator
import unittest


class TestCalculator(unittest.TestCase):
    def test_addition(self):
        add = Calculator(12.5, 8, '+')
        self.assertEqual(add.operation(), 20.5)
    def test_subtraction(self):
        sub = Calculator(12.5, 8, '-')
        self.assertEqual(sub.operation(), 4.5)
    def test_multiplication(self):
        mul = Calculator(12.5, 8, '*')
        self.assertEqual(mul.operation(), 100.0)
    def test_division(self):
        div = Calculator(12.5, 8, '/')
        self.assertEqual(div.operation(), 1.5625)
    def test_unknown_operation(self):
        pow = Calculator(12.5, 8, '^')
        self.assertEqual(pow.operation(), 'Unknown operation')
    def test_arithmetic_error(self):
        err = Calculator(12.5, 0, '/')
        self.assertEqual(err.operation(), 'Divide by Zero')
        self.assertRaises(ArithmeticError)

if __name__ == '__main__':
    unittest.main()