# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(a):
    b = 2
    while b <= (int(a)) ** .5:
        if a % b == 0:
            return False
        else: b += 1
    return True

