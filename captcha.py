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
    assert isinstance(n, int)
    a, b = divmod(n, 10)
    if n <= 20 or b == 0:
        return NUMBERS[n]
    return NUMBERS[a * 10] + " " + NUMBERS[b]


def some_random_operation(max: int = 100) -> tuple[str, int]:
    op = random.choice(["+", "-", "*", "/"])
    if op in "*/":
        max = int(max**0.5)
    a = random.randint(1, max)
    b = random.randint(1, max)
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
