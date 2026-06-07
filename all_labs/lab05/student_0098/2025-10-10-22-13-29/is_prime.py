# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 2

    return True

print(is_prime(15))
print(is_prime(17))
print(is_prime(25))
print(is_prime(26))
print(is_prime(97))


