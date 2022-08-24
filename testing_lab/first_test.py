import unittest
from unittest import TestCase


class FirstTest(TestCase):  # Test Suite
    def test_assertEqual(self):   # Test Case
        self.assertEqual(1, 1)

    def test_assertTrue(self):
        self.assertTrue(True)

    def test_assertListEqual(self):
        self.assertListEqual([1, 2, 3], [1, 2, 3])


if __name__ == '__main__':
    unittest.main()