#!/usr/bin/env python3
"""
Focused unit tests for the divide method of SimpleCalculator class.
Comprehensive testing of division operations including edge cases.
"""

import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculatorDivide(unittest.TestCase):
    """Test cases specifically for the divide method of SimpleCalculator class."""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_division_positive_numbers(self):
        """Test division with positive numbers."""
        # Test exact division
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(15, 3), 5)
        self.assertEqual(self.calc.divide(100, 10), 10)
        
        # Test division with remainder (should return float)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        self.assertEqual(self.calc.divide(1, 2), 0.5)
        self.assertEqual(self.calc.divide(3, 4), 0.75)

    def test_division_negative_numbers(self):
        """Test division with negative numbers."""
        # Test negative numerator
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(-15, 3), -5)
        self.assertEqual(self.calc.divide(-7, 2), -3.5)
        
        # Test negative denominator
        self.assertEqual(self.calc.divide(10, -2), -5)
        self.assertEqual(self.calc.divide(15, -3), -5)
        self.assertEqual(self.calc.divide(7, -2), -3.5)
        
        # Test both negative
        self.assertEqual(self.calc.divide(-10, -2), 5)
        self.assertEqual(self.calc.divide(-15, -3), 5)
        self.assertEqual(self.calc.divide(-7, -2), 3.5)

    def test_division_zero_numerator(self):
        """Test division when numerator is zero."""
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertEqual(self.calc.divide(0, -5), 0)
        self.assertEqual(self.calc.divide(0, 100), 0)
        self.assertEqual(self.calc.divide(0, 0.5), 0)

    def test_division_by_zero(self):
        """Test division by zero returns None."""
        # Test division by zero with positive numerator
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(100, 0))
        
        # Test division by zero with negative numerator
        self.assertIsNone(self.calc.divide(-5, 0))
        self.assertIsNone(self.calc.divide(-10, 0))
        self.assertIsNone(self.calc.divide(-100, 0))
        
        # Test division by zero with zero numerator
        self.assertIsNone(self.calc.divide(0, 0))
        
        # Test division by zero with floating point numerator
        self.assertIsNone(self.calc.divide(5.5, 0))
        self.assertIsNone(self.calc.divide(-3.14, 0))

    def test_division_floating_point(self):
        """Test division with floating point numbers."""
        # Test float division
        self.assertEqual(self.calc.divide(5.5, 2), 2.75)
        self.assertEqual(self.calc.divide(10.0, 4.0), 2.5)
        self.assertEqual(self.calc.divide(7.5, 2.5), 3.0)
        
        # Test float division with negative numbers
        self.assertEqual(self.calc.divide(-5.5, 2), -2.75)
        self.assertEqual(self.calc.divide(5.5, -2), -2.75)
        
        # Test very small numbers
        self.assertEqual(self.calc.divide(0.1, 10), 0.01)
        self.assertEqual(self.calc.divide(0.001, 1000), 0.000001)

    def test_division_large_numbers(self):
        """Test division with large numbers."""
        self.assertEqual(self.calc.divide(1000000, 1000), 1000)
        self.assertEqual(self.calc.divide(999999, 333333), 3.000003000003)
        
        # Test very small results
        self.assertEqual(self.calc.divide(1, 1000000), 0.000001)

    def test_division_by_one(self):
        """Test division by one."""
        self.assertEqual(self.calc.divide(5, 1), 5)
        self.assertEqual(self.calc.divide(-5, 1), -5)
        self.assertEqual(self.calc.divide(0, 1), 0)
        self.assertEqual(self.calc.divide(3.14, 1), 3.14)

    def test_division_self_division(self):
        """Test division of a number by itself."""
        self.assertEqual(self.calc.divide(5, 5), 1)
        self.assertEqual(self.calc.divide(-5, -5), 1)
        self.assertEqual(self.calc.divide(3.14, 3.14), 1)
        self.assertEqual(self.calc.divide(0, 0), None)  # This should be None due to division by zero

    def test_division_precision(self):
        """Test division precision with repeating decimals."""
        # Test repeating decimals
        result = self.calc.divide(1, 3)
        self.assertAlmostEqual(result, 0.3333333333333333, places=10)
        
        result = self.calc.divide(2, 3)
        self.assertAlmostEqual(result, 0.6666666666666666, places=10)

    def test_division_type_consistency(self):
        """Test that division returns appropriate types."""
        # Integer division that results in integer
        result = self.calc.divide(10, 2)
        self.assertIsInstance(result, int)
        
        # Integer division that results in float
        result = self.calc.divide(10, 3)
        self.assertIsInstance(result, float)
        
        # Float division
        result = self.calc.divide(5.5, 2)
        self.assertIsInstance(result, float)
        
        # Division by zero
        result = self.calc.divide(5, 0)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()