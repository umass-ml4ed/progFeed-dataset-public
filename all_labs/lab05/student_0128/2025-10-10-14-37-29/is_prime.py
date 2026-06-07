# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_prime(candidate):
    dividing = 0
    for i in range(2, int(candidate ** 0.5) + 1):
        if candidate % i == 0:
            dividing += 1
    return not bool(dividing)