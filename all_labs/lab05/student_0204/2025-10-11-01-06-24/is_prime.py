# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    i = 2
    max = int(n ** 0.5)
    while i <= max:
        if n % i == 0:
            return False
        else:
            i += 1
    return True
