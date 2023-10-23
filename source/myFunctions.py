def add(num1: int, num2: int) -> int:
    return num1 + num2


def divide(num1: float, num2: float) -> float:
    if num2 == 0:
        raise ValueError
    return num1 / num2
