from captcha import to_text, operation


def test_to_text():
    assert to_text(0) == "zero"
    assert to_text(21) == "twenty one"
    assert to_text(10) == "ten"
    assert to_text(20) == "twenty"
    assert to_text(30) == "thirty"


def test_operations():
    assert operation(2, 3, "+") == ("two + three", 5)
    assert operation(5, 3, "-") == ("five - three", 2)
    assert operation(2, 3, "*") == ("two * three", 6)
    assert operation(6, 3, "/") == (
        "eighteen / three",
        2,
    )  # only integer division are cutes
