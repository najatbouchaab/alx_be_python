#!/usr/bin/env python3
"""
Unit tests for the SimpleCalculator class.
Tests all arithmetic operations with various scenarios including edge cases.
"""

import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Test cases for SimpleCalculator class."""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method with various scenarios."""
        # Test positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 5), 15)
        
        # Test negative numbers
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
        
        # Test zero values
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, 0), 0)
        
        # Test floating point numbers
        self.assertEqual(self.calc.add(2.5, 3.7), 6.2)
        self.assertEqual(self.calc.add(-1.5, 2.5), 1.0)

    def test_subtraction(self):
        """Test the subtraction method with various scenarios."""
        # Test positive numbers
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(10, 5), 5)
        
        # Test negative numbers
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        
        # Test zero values
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        
        # Test floating point numbers
        self.assertEqual(self.calc.subtract(5.5, 2.2), 3.3)
        self.assertEqual(self.calc.subtract(1.5, 2.5), -1.0)
        
        # Test larger from smaller
        self.assertEqual(self.calc.subtract(3, 10), -7)

    def test_multiplication(self):
        """Test the multiplication method with various scenarios."""
        # Test positive numbers
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(5, 4), 20)
        
        # Test negative numbers
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        
        # Test zero values
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)
        
        # Test floating point numbers
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)
        self.assertEqual(self.calc.multiply(1.5, 2.0), 3.0)
        
        # Test with one
        self.assertEqual(self.calc.multiply(1, 5), 5)
        self.assertEqual(self.calc.multiply(5, 1), 5)

    def test_division_normal_cases(self):
        """Test the division method with normal cases."""
        # Test exact division
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(9, 3), 3)
        
        # Test floating point results
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(1, 4), 0.25)
        
        # Test negative numbers
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(10, -2), -5)
        self.assertEqual(self.calc.divide(-10, -2), 5)
        
        # Test floating point inputs
        self.assertEqual(self.calc.divide(5.5, 2), 2.75)
        self.assertEqual(self.calc.divide(10.0, 4.0), 2.5)
        
        # Test division by one
        self.assertEqual(self.calc.divide(7, 1), 7)
        
        # Test division resulting in zero
        self.assertEqual(self.calc.divide(0, 5), 0)

    def test_division_by_zero(self):
        """Test the division method when dividing by zero."""
        # Test division by zero with positive numerator
        self.assertIsNone(self.calc.divide(5, 0))
        
        # Test division by zero with negative numerator
        self.assertIsNone(self.calc.divide(-5, 0))
        
        # Test division by zero with zero numerator
        self.assertIsNone(self.calc.divide(0, 0))
        
        # Test division by zero with floating point
        self.assertIsNone(self.calc.divide(5.5, 0))

    def test_division_precision(self):
        """Test division precision with repeating decimals and floating point."""
        # Test repeating decimals with almost equal assertion
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.3333333333333333, places=10)
        self.assertAlmostEqual(self.calc.divide(2, 3), 0.6666666666666666, places=10)
        
        # Test precise floating point division
        self.assertEqual(self.calc.divide(1.0, 8.0), 0.125)
        self.assertEqual(self.calc.divide(3.14159, 2), 1.570795)

    def test_division_large_numbers(self):
        """Test division with large numbers."""
        self.assertEqual(self.calc.divide(1000000, 1000), 1000)
        self.assertEqual(self.calc.divide(999999, 333333), 3.000003000003)
        
        # Test very small results
        self.assertEqual(self.calc.divide(1, 1000000), 0.000001)
        self.assertEqual(self.calc.divide(1, 1000000000), 1e-09)

    def test_division_edge_cases(self):
        """Test division edge cases."""
        # Test division by very small numbers
        self.assertEqual(self.calc.divide(1, 0.0001), 10000)
        self.assertEqual(self.calc.divide(5, 0.5), 10)
        
        # Test self-division
        self.assertEqual(self.calc.divide(5, 5), 1)
        self.assertEqual(self.calc.divide(-5, -5), 1)
        self.assertEqual(self.calc.divide(3.14, 3.14), 1)
        
        # Test division resulting in very large numbers
        self.assertEqual(self.calc.divide(1000000, 0.001), 1000000000)

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
        
        # Division of zero by non-zero
        result = self.calc.divide(0, 5)
        self.assertIsInstance(result, int)

    def test_division_comprehensive(self):
        """Comprehensive division test covering multiple scenarios."""
        # Test various division scenarios in one method
        test_cases = [
            (15, 3, 5),      # Simple division
            (7, 2, 3.5),     # Division with remainder
            (-8, 4, -2),     # Negative numerator
            (8, -4, -2),     # Negative denominator
            (-9, -3, 3),     # Both negative
            (0, 7, 0),       # Zero numerator
            (2.5, 0.5, 5),   # Decimal numbers
            (100, 10, 10),   # Large numbers
        ]
        
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b, expected=expected):
                self.assertEqual(self.calc.divide(a, b), expected)

    def test_operations_consistency(self):
        """Test that operations are consistent and work together."""
        # Test that addition and subtraction are inverse operations
        result_add = self.calc.add(5, 3)
        result_sub = self.calc.subtract(result_add, 3)
        self.assertEqual(result_sub, 5)
        
        # Test that multiplication and division are inverse operations
        result_mul = self.calc.multiply(4, 2)
        result_div = self.calc.divide(result_mul, 2)
        self.assertEqual(result_div, 4)
        
        # Test division and multiplication consistency
        original = 15
        divisor = 3
        result_div = self.calc.divide(original, divisor)
        result_mul = self.calc.multiply(result_div, divisor)
        self.assertEqual(result_mul, original)


if __name__ == '__main__':
    unittest.main()