# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def is_prime(n):
    if n < 2:
        return False
    x = 2
    while x <= n ** 0.5:
        if n % x == 0:
            return False
        x += 1
    return True

