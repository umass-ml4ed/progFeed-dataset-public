# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    i = 2
    while i <= (n ** 0.5):
        if n % i == 0:
            return False
        else:
            i += 1
    return True


