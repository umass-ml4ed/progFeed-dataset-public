# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_prime(x):
    if x <= 1:
        return False
    i = 2
    while i <= int(x**0.5):
        if x % i == 0:
            return False
        i += 1
    return True

