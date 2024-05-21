import unittest
import string
import random
from main import PassGen, Poor, Average, Advance, Value, Choice

class TestPassGen(unittest.TestCase):

    def setUp(self):
        self.poor_chars = set(Poor)
        self.average_chars = set(Average)
        self.advance_chars = set(Advance)

    def test_poor_password(self):
        Choice.set(1)
        Value.set(10)
        password = PassGen()
        self.assertEqual(len(password), 10)
        self.assertTrue(set(password).issubset(self.poor_chars))

    def test_average_password(self):
        Choice.set(2)
        Value.set(12)
        password = PassGen()
        self.assertEqual(len(password), 12)
        self.assertTrue(set(password).issubset(self.average_chars))

    def test_advance_password(self):
        Choice.set(3)
        Value.set(15)
        password = PassGen()
        self.assertEqual(len(password), 15)
        self.assertTrue(set(password).issubset(self.advance_chars))

    def test_invalid_choice(self):
        Choice.set(4)
        Value.set(20)
        with self.assertRaises(ValueError):
            PassGen()

    def test_password_length(self):
        Choice.set(2)
        Value.set(0)
        with self.assertRaises(ValueError):
            PassGen()

if __name__ == '__main__':
    unittest.main()
