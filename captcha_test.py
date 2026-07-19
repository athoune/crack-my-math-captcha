import pytest
from captcha import to_text, operation, some_random_operation


def test_to_text_small_numbers():
    assert to_text(0) == "zero"
    assert to_text(1) == "one"
    assert to_text(10) == "ten"
    assert to_text(15) == "fifteen"
    assert to_text(20) == "twenty"


def test_to_text_compound_numbers():
    assert to_text(21) == "twenty one"
    assert to_text(42) == "forty two"
    assert to_text(99) == "ninety nine"


def test_to_text_round_tens():
    assert to_text(30) == "thirty"
    assert to_text(50) == "fifty"
    assert to_text(90) == "ninety"


def test_to_text_hundreds():
    assert to_text(100) == "one hundred"
    assert to_text(200) == "two hundred"
    assert to_text(999) == "nine hundred ninety nine"


def test_to_text_hundreds_with_remainder():
    assert to_text(101) == "one hundred one"
    assert to_text(123) == "one hundred twenty three"
    assert to_text(210) == "two hundred ten"


def test_to_text_invalid():
    with pytest.raises(AssertionError):
        to_text(-1)
    with pytest.raises(AssertionError):
        to_text(1000)
    with pytest.raises(AssertionError):
        to_text(3.14)


def test_operations_addition():
    assert operation(2, 3, "+") == ("two + three", 5)
    assert operation(0, 0, "+") == ("zero + zero", 0)


def test_operations_subtraction():
    assert operation(5, 3, "-") == ("five - three", 2)
    # Swapped: a < b becomes b - a
    assert operation(3, 5, "-") == ("five - three", 2)


def test_operations_multiplication():
    assert operation(2, 3, "*") == ("two * three", 6)
    assert operation(1, 7, "*") == ("one * seven", 7)


def test_operations_division():
    # Only integer divisions are produced (a = r * b)
    assert operation(6, 3, "/") == ("eighteen / three", 6)
    # Swapped: a < b becomes b / a
    assert operation(3, 6, "/") == ("eighteen / three", 6)


def test_some_random_operation_returns_valid():
    """Random operations always produce a solvable equation."""
    for _ in range(50):
        eq, result = some_random_operation(20)
        assert isinstance(eq, str)
        assert isinstance(result, int)
        assert result >= 0


def test_some_random_operation_default_bound():
    """Default upper_bound=100 still produces valid results."""
    for _ in range(50):
        eq, result = some_random_operation()
        assert isinstance(eq, str)
        assert isinstance(result, int)
