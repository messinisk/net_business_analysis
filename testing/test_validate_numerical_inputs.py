import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from net_analysis.setting.return_func_error import validate_numerical_inputs

class TestValidation(unittest.TestCase):
    class DummyClass:
        @validate_numerical_inputs
        def divide(self, a, b):
            return a / b

    def setUp(self):
        self.dummy = self.DummyClass()

    def test_valid_numbers(self):
        self.assertEqual(self.dummy.divide(10, 2), 5)
        self.assertEqual(self.dummy.divide(3.5, 1.4), 2.5)

    def test_string_numbers(self):
        self.assertEqual(self.dummy.divide("10", "2"), 5)
        self.assertEqual(self.dummy.divide("3.5", "1.4"), 2.5)

    def test_mixed_valid_inputs(self):
        self.assertEqual(self.dummy.divide("10", 2), 5)
        self.assertEqual(self.dummy.divide(3.5, "1.4"), 2.5)

    def test_invalid_string(self):
        self.assertEqual(self.dummy.divide("abc", 2), 0.0)
        self.assertEqual(self.dummy.divide(3, "xyz"), 0.0)

    def test_non_numeric_inputs(self):
        self.assertEqual(self.dummy.divide([10], 2), 0.0)
        self.assertEqual(self.dummy.divide(3, {1: "one"}), 0.0)

    def test_division_by_zero(self):
        self.assertEqual(self.dummy.divide(10, 0), float("inf"))
        self.assertEqual(self.dummy.divide("10", "0"), float("inf"))

if __name__ == "__main__":
    unittest.main()