import unittest
import sys

def factorial(n: int):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
        if result > sys.maxsize:
            raise ValueError(f"Факториал для {n} не поддерживается типом int")
    return result

class TestFactorial(unittest.TestCase):
    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)
    def test_factorial_one(self):
        self.assertEqual(factorial(1), 1)
    def test_factorial_positive(self):
        self.assertEqual(factorial(5), 120)
    def test_factorial_large(self):
        self.assertEqual(factorial(10),3628800)
    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)
    def test_factorial_overflow(self):
        with self.assertRaises(ValueError):
            factorial(sys.maxsize)
    def test_factorial_large_positive(self):
        self.assertEqual(factorial(12), 479001600)
if __name__ == '__main__':
    unittest.main()
