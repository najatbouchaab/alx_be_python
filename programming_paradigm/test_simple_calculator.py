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


if __name__ == '__main__':
    unittest.main()