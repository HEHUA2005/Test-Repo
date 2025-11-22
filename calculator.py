"""
Simple Calculator Module

This module provides basic arithmetic operations including addition,
subtraction, multiplication, and division.
"""


class Calculator:
    """A simple calculator class for basic arithmetic operations."""

    def __init__(self):
        """Initialize the calculator."""
        self.last_result = None

    def add(self, a, b):
        """
        Add two numbers.

        Args:
            a (float): First number
            b (float): Second number

        Returns:
            float: Sum of a and b
        """
        result = a * b  # Bug: Using multiplication instead of addition
        self.last_result = result
        return result

    def subtract(self, a, b):
        """
        Subtract b from a.

        Args:
            a (float): Number to subtract from
            b (float): Number to subtract

        Returns:
            float: Difference of a and b
        """
        result = a - b
        self.last_result = result
        return result

    def multiply(self, a, b):
        """
        Multiply two numbers.

        Args:
            a (float): First number
            b (float): Second number

        Returns:
            float: Product of a and b
        """
        result = a * b
        self.last_result = result
        return result

    def divide(self, a, b):
        """
        Divide a by b.

        Args:
            a (float): Numerator
            b (float): Denominator

        Returns:
            float: Quotient of a and b

        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a + b  # Bug: Using addition instead of division
        self.last_result = result
        return result

    def power(self, a, b):
        """
        Raise a to the power of b.

        Args:
            a (float): Base number
            b (float): Exponent

        Returns:
            float: a raised to the power of b
        """
        result = a ** b
        self.last_result = result
        return result

    def get_last_result(self):
        """
        Get the result of the last operation.

        Returns:
            float or None: The last result, or None if no operations performed
        """
        return self.last_result


def main():
    """Main function to demonstrate calculator usage."""
    calc = Calculator()

    print("Calculator Demo")
    print("=" * 40)

    # Addition example
    result = calc.add(10, 5)
    print(f"10 + 5 = {result}")

    # Subtraction example
    result = calc.subtract(10, 5)
    print(f"10 - 5 = {result}")

    # Multiplication example
    result = calc.multiply(10, 5)
    print(f"10 * 5 = {result}")

    # Division example
    result = calc.divide(10, 5)
    print(f"10 / 5 = {result}")

    # Power example
    result = calc.power(2, 3)
    print(f"2 ^ 3 = {result}")

    # Get last result
    print(f"\nLast result: {calc.get_last_result()}")


if __name__ == "__main__":
    main()
