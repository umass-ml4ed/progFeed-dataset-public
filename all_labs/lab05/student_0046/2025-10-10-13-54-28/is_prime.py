# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n: int) -> bool:
    if n < 2: 
        return False
    d, m = 2, int(n ** 0.5)
    while d <= m:
        if n % d == 0:
            return False
        d += 1
    return True