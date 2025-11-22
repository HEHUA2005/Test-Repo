"""
Unit tests for the Calculator module.

This module contains comprehensive unit tests for all calculator operations.
"""

import pytest
from calculator import Calculator


class TestCalculator:
    """Test suite for Calculator class."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.calc = Calculator()

    def test_add_positive_numbers(self):
        """Test addition of two positive numbers."""
        result = self.calc.add(5, 3)
        assert result == 8, "5 + 3 should equal 8"

    def test_add_negative_numbers(self):
        """Test addition of two negative numbers."""
        result = self.calc.add(-5, -3)
        assert result == -8, "-5 + (-3) should equal -8"

    def test_add_mixed_numbers(self):
        """Test addition of positive and negative numbers."""
        result = self.calc.add(10, -3)
        assert result == 7, "10 + (-3) should equal 7"

    def test_add_zero(self):
        """Test addition with zero."""
        result = self.calc.add(5, 0)
        assert result == 5, "5 + 0 should equal 5"

    def test_add_floats(self):
        """Test addition of floating point numbers."""
        result = self.calc.add(2.5, 3.7)
        assert abs(result - 6.2) < 0.0001, "2.5 + 3.7 should equal 6.2"

    def test_subtract_positive_numbers(self):
        """Test subtraction of two positive numbers."""
        result = self.calc.subtract(10, 3)
        assert result == 7, "10 - 3 should equal 7"

    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        result = self.calc.subtract(5, -3)
        assert result == 8, "5 - (-3) should equal 8"

    def test_subtract_to_negative(self):
        """Test subtraction resulting in negative number."""
        result = self.calc.subtract(3, 10)
        assert result == -7, "3 - 10 should equal -7"

    def test_subtract_zero(self):
        """Test subtraction with zero."""
        result = self.calc.subtract(5, 0)
        assert result == 5, "5 - 0 should equal 5"

    def test_multiply_positive_numbers(self):
        """Test multiplication of two positive numbers."""
        result = self.calc.multiply(5, 3)
        assert result == 15, "5 * 3 should equal 15"

    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        result = self.calc.multiply(-5, 3)
        assert result == -15, "-5 * 3 should equal -15"

    def test_multiply_two_negative_numbers(self):
        """Test multiplication of two negative numbers."""
        result = self.calc.multiply(-5, -3)
        assert result == 15, "-5 * -3 should equal 15"

    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        result = self.calc.multiply(5, 0)
        assert result == 0, "5 * 0 should equal 0"

    def test_multiply_floats(self):
        """Test multiplication of floating point numbers."""
        result = self.calc.multiply(2.5, 4)
        assert result == 10.0, "2.5 * 4 should equal 10.0"

    def test_divide_positive_numbers(self):
        """Test division of two positive numbers."""
        result = self.calc.divide(10, 2)
        assert result == 5, "10 / 2 should equal 5"

    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        result = self.calc.divide(-10, 2)
        assert result == -5, "-10 / 2 should equal -5"

    def test_divide_to_float(self):
        """Test division resulting in floating point number."""
        result = self.calc.divide(7, 2)
        assert result == 3.5, "7 / 2 should equal 3.5"

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(10, 0)

    def test_divide_zero_by_number(self):
        """Test zero divided by a number."""
        result = self.calc.divide(0, 5)
        assert result == 0, "0 / 5 should equal 0"

    def test_power_positive_exponent(self):
        """Test power with positive exponent."""
        result = self.calc.power(2, 3)
        assert result == 8, "2 ^ 3 should equal 8"

    def test_power_zero_exponent(self):
        """Test power with zero exponent."""
        result = self.calc.power(5, 0)
        assert result == 1, "5 ^ 0 should equal 1"

    def test_power_negative_exponent(self):
        """Test power with negative exponent."""
        result = self.calc.power(2, -2)
        assert result == 0.25, "2 ^ -2 should equal 0.25"

    def test_power_fractional_exponent(self):
        """Test power with fractional exponent."""
        result = self.calc.power(4, 0.5)
        assert result == 2, "4 ^ 0.5 should equal 2"

    def test_last_result_tracking(self):
        """Test that last result is tracked correctly."""
        self.calc.add(5, 3)
        assert self.calc.get_last_result() == 8, "Last result should be 8"

        self.calc.multiply(2, 4)
        assert self.calc.get_last_result() == 8, "Last result should be updated to 8"

    def test_initial_last_result(self):
        """Test that initial last result is None."""
        assert self.calc.get_last_result() is None, "Initial last result should be None"

    def test_last_result_after_division(self):
        """Test last result after division operation."""
        self.calc.divide(10, 2)
        assert self.calc.get_last_result() == 5, "Last result should be 5"

    def test_chained_operations(self):
        """Test multiple chained operations."""
        result1 = self.calc.add(5, 3)
        result2 = self.calc.multiply(result1, 2)
        result3 = self.calc.subtract(result2, 4)
        assert result3 == 12, "((5 + 3) * 2) - 4 should equal 12"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
