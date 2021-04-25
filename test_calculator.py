import unittest

from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_calculator_simple_count(self):
        self.assertEqual(self.calculator.calculate('300 + 500'), 800)
        self.assertEqual(self.calculator.calculate('100 - 599'), -499)
        self.assertEqual(self.calculator.calculate('30 * 50'), 1500)
        self.assertEqual(self.calculator.calculate('255 / 50'), 5.1)

    def test_calculator_float_negatives(self):
        self.assertEqual(self.calculator.calculate('-2.9'), -2.9)
        self.assertEqual(self.calculator.calculate('-2.9 * -45.6'), 132.24)
        self.assertEqual(self.calculator.calculate('-30 + 50 * 90 / 7.5 + -4.3'), 235.7)
        self.assertEqual(self.calculator.calculate('11 / 50 - -164 * 6.3 + 9 * 5'), 5217.93)
        self.assertEqual(self.calculator.calculate('.2 + -.5 * 4. / .3'), -4)

    def test_calculator_errors_validation(self):
        self.assertRaises(ValueError, self.calculator.calculate, 'a')
        self.assertRaises(ValueError, self.calculator.calculate, 'ab + 4')
        self.assertRaises(ValueError, self.calculator.calculate, '5 - 5t')
        self.assertRaises(ZeroDivisionError, self.calculator.calculate, '5 / 0')
        self.assertRaises(ValueError, self.calculator.calculate, ' - 4 + 5')
        self.assertRaises(ValueError, self.calculator.calculate, '1 --4 + 5')
        self.assertRaises(ValueError, self.calculator.calculate, '4 + 5 -')
        self.assertRaises(ValueError, self.calculator.calculate, '4 +- 5')
        self.assertRaises(ValueError, self.calculator.calculate, '4 + 5 - - 5')
        self.assertRaises(ValueError, self.calculator.calculate, '4..4 + 5')
        self.assertRaises(ValueError, self.calculator.calculate, '4 + .5.')
        self.assertRaises(ValueError, self.calculator.calculate, '4 5 + 5')
        self.assertIsNone(self.calculator.calculate(''))
        self.assertIsNone(self.calculator.calculate(' '))


if __name__ == "__main__":
    unittest.main()
