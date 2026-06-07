# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    test_int = 2
    while test_int <= int(n ** 0.5):
        if n % test_int == 0:
            return False
        else:
            test_int += 1
    return True
