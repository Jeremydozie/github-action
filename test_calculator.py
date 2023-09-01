
# test_calculator.py

# Import the functions to be tested
from calculator import add, subtract

# Define test functions
def test_add():
    result = add(2, 3)
    assert result == 5

def test_subtract():
    result = subtract(5, 2)
    assert result == 3
