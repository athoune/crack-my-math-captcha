from operator import add, mul
import random

NUMBERS = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}


def to_text(n: int) -> str:
    """Convert an integer (0–999) to its English text representation."""
    assert isinstance(n, int)
    assert 0 <= n <= 999, f"Number out of supported range: {n}"
    if n <= 20:
        return NUMBERS[n]
    if n < 100:
        a, b = divmod(n, 10)
        if b == 0:
            return NUMBERS[a * 10]
        return NUMBERS[a * 10] + " " + NUMBERS[b]
    # n is 100–999
    hundreds, remainder = divmod(n, 100)
    result = NUMBERS[hundreds] + " hundred"
    if remainder == 0:
        return result
    return result + " " + to_text(remainder)


def some_random_operation(upper_bound: int = 100) -> tuple[str, int]:
    op = random.choice(["+", "-", "*", "/"])
    if op in "*/":
        upper_bound = int(upper_bound**0.5)
    a = random.randint(1, upper_bound)
    b = random.randint(1, upper_bound)
    return operation(a, b, op)


def operation(a: int, b: int, op: str) -> tuple[str, int]:
    r: int = 0
    if op in "-/" and a < b:
        b, a = a, b
    if op == "/":
        r = a
        a = r * b
    elif op == "*":
        r = mul(a, b)
    elif op == "+":
        r = add(a, b)
    elif op == "-":
        r = add(a, -b)

    eq = f"{to_text(a)} {op} {to_text(b)}"
    return eq, r
