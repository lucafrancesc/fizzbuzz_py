import unittest
from fizzbuzz import fizz_buzz

class TestFizzBuzz(unittest.TestCase):

    def test_return_number(self):
        self.assertEqual(fizz_buzz(-1), -1)
        self.assertEqual(fizz_buzz(0), 0)
        self.assertEqual(fizz_buzz(1), 1)
        self.assertEqual(fizz_buzz(2), 2)
        self.assertEqual(fizz_buzz(4), 4)

    def test_15_is_buzz(self):
        self.assertEqual(fizz_buzz(15), 'FizzBuzz')
        self.assertEqual(fizz_buzz(30), 'FizzBuzz')
        self.assertEqual(fizz_buzz(-45), 'FizzBuzz')

    def test_5_is_buzz(self):
        self.assertEqual(fizz_buzz(5), 'Buzz')
        self.assertEqual(fizz_buzz(-5), 'Buzz')
        self.assertEqual(fizz_buzz(10), 'Buzz')


    def test_3_is_fizz(self):
        self.assertEqual(fizz_buzz(3), 'Fizz')
        self.assertEqual(fizz_buzz(6), 'Fizz')
        self.assertEqual(fizz_buzz(-6), 'Fizz')

unittest.main()
