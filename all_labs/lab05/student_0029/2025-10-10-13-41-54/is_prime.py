# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    n = 20 
    i = 2
    while i <= n // 2:
        if n % i == 0:
            return False
        i += 1
    return True
