# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    if n < 2:
        return False

    i = 2
    n_root = int(n ** 0.5)
    while i <= n_root:
        if n % i == 0:
            return False
        i += 1
    return True

       

