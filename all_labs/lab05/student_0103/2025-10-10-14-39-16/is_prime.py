# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    f = 2
    while f <= int(n ** 0.5):
        m = n % f
        f = f + 1
    return bool(m != 0)