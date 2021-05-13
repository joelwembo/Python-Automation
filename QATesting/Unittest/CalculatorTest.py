class Calculator(object):
    def __init__(self):
        self._last_answer = 0.0

    @property
    def last_answer(self):
        return self._last_answer

    def add(self, a, b):
        self._last_answer = a + b
        return self.last_answer

    def subtract(self, a, b):
        self._last_answer = (a-b)
        return self.last_answer

    def multiply(self, a, b):
        self._last_answer = a * b
        return self.last_answer

    def divide(self, a, b):
        # automatically raises ZeroDivisionError
        self._last_answer = a * 1.0 / b
        return self.last_answer


import unittest
NUMBER_1 = 3.0
NUMBER_2 = 2.0
FAILURE = 'incorrect value'


class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_last_answer_init(self):
        value = self.calc.last_answer
        self.assertEqual(value, 0.0, FAILURE)

    def test_add(self):
        value = self.calc.add(NUMBER_1, NUMBER_2)
        self.assertEqual(value, 5.0, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    def test_subtract(self):
        value = self.calc.subtract(NUMBER_1, NUMBER_2)
        self.assertEqual(value, 1.0, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    def test_subtract_negative(self):
        value = self.calc.subtract(NUMBER_2, NUMBER_1)
        self.assertEqual(value, -1.0, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    def test_multiply(self):
        value = self.calc.multiply(NUMBER_1, NUMBER_2)
        self.assertEqual(value, 6.0, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    def test_divide(self):
        value = self.calc.divide(NUMBER_1, NUMBER_2)
        self.assertEqual(value, 1.5, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    def test_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, self.calc.divide, NUMBER_1, 0)
        