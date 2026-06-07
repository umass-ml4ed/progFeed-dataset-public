# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    n = int(n)
    if n < 2:
        return False
    i = 2
    while i <= int(n ** 0.5):
        if n % i == 0:
            return False
        i += 1
    return True
