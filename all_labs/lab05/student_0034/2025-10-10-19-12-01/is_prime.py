# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n: int)-> bool:
    it = 2
    while it <= int(n**0.5):
        if n % it == 0:
            return False
        it += 1
    return True
