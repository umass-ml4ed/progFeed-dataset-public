# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_prime(i: int):
    if i <= 1:
        return False
    n = 2
    while n <= int(n ** 0.5):
        if i % n == 0:
            return False
        n += 1
    return True