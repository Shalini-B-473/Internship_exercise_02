# Code for factorial program using recursion
import math

def factorial(n):
    try:
        if isinstance(n, str):
            return "Factorial can only be computed for positive real numbers and zero"
        elif n < 0:
            return "Factorial for a negative number is not defined"
        elif type(n) == int:
            if n == 0:
                return 1
            else:
                return n * factorial(n - 1)
        elif type(n) == float:
            return math.gamma(float(n) + 1)
        else:
            return "Factorial can only be computed for positive real numbers and zero"
    except ValueError:
        return "Factorial can only be computed for positive real numbers and zero"
