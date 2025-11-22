# Calculator

A simple Python calculator library that provides basic arithmetic operations.

## Features

- Addition
- Subtraction
- Multiplication
- Division (with zero-division protection)
- Power/Exponentiation
- Last result tracking

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd Test-Repo
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### As a Library

```python
from calculator import Calculator

calc = Calculator()

# Perform operations
result = calc.add(10, 5)        # Addition
result = calc.subtract(10, 5)   # Subtraction
result = calc.multiply(10, 5)   # Multiplication
result = calc.divide(10, 5)     # Division
result = calc.power(2, 3)       # Power

# Get last result
last = calc.get_last_result()
```

### Running the Demo

```bash
python calculator.py
```

## Testing

Run the unit tests using pytest:

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run with coverage report
pytest --cov=calculator --cov-report=html
```

## API Reference

### Calculator Class

#### Methods

- `add(a, b)` - Returns the sum of a and b
- `subtract(a, b)` - Returns the difference of a and b
- `multiply(a, b)` - Returns the product of a and b
- `divide(a, b)` - Returns the quotient of a and b (raises ValueError if b is zero)
- `power(a, b)` - Returns a raised to the power of b
- `get_last_result()` - Returns the result of the last operation

## Requirements

- Python 3.7+
- pytest 7.4.0+ (for testing)
- pytest-cov 4.1.0+ (for coverage reports)

## License

MIT License
