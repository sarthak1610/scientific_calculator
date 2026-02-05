import math

def square_root(x):
    if x < 0:
        raise ValueError("Negative input")
    return math.sqrt(x)

def power(a, b):
    return a ** b

def sine(x):
    return math.sin(x)
