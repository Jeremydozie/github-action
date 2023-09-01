# Save this file as "test_example.py"

# Import the module or code you want to test
from my_module import add, subtract

# Define test functions using the "test_" prefix
# pytest will automatically discover and run these functions

def test_addition():
    result = add(2, 3)
    assert result == 5

def test_subtraction():
    result = subtract(5, 2)
    assert result == 3

def test_division_by_zero():
    # This test demonstrates how to use pytest's built-in assertion for exceptions
    with pytest.raises(ZeroDivisionError):
        result = divide(1, 0)

# You can also use fixtures for setup and teardown if needed
# Here's a simple fixture example:

import pytest

@pytest.fixture
def setup_example():
    print("Setup for test")
    # Any setup code can go here, and this fixture can be reused in multiple tests
    yield
    print("Teardown after test")
    # Any teardown code can go here

def test_example_with_fixture(setup_example):
    # The setup_example fixture will be automatically passed to this test function
    assert True  # You can replace this with your actual test logic

# To run these tests, simply execute "pytest" in the directory containing this test file:
# $ pytest

# pytest will discover and execute the test functions, reporting the results.

