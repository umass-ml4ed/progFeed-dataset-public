# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    thing = int(n ** 0.5)
    i = 2
    while i <= thing:
        if n % i == 0:
            return False
        i += 1
    return True

