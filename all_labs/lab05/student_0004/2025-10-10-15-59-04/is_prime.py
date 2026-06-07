# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(15))      #⇒ False
print(is_prime(17))      #⇒ True
print(is_prime(25))      #⇒ False
print(is_prime(26))      #⇒ False
print(is_prime(97))      #⇒ True
