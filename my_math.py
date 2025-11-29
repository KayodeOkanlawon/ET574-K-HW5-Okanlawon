# my_math.py
# Name: Kayode Okanlawon
# QCC ID: 24615461

def pow(x, y):
  
    if y == 0:
        return 1


    if y < 0:
        result = 1
        for _ in range(-y):
            result *= x
        return 1 / result

    result = 1
    for _ in range(y):
        result *= x
    return result

def factorial(n):
    """Returns n! (factorial of n)."""
    if n < 0:
        return "Error: factorial is not defined for negative numbers."

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def distance(x1, y1, x2, y2):
    """Returns the distance between two points (x1, y1) and (x2, y2)."""
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
