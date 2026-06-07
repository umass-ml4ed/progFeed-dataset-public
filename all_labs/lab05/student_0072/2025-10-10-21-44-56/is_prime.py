# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    if n < 2:
        return False
    d = 2
    limit = int(n ** 0.5)
    while d <= limit:
        if n % d == 0:
            return False
        d += 1
    return True
