from math import floor, sqrt

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, floor(sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True