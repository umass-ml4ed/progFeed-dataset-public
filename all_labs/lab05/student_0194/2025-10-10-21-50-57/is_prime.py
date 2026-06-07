# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

import math

def is_prime(n):
    count = 2
    while count <= int(math.sqrt(n)):
        if n % count == 0:
            return False
        else:
            count += 1
    return True




