# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

import math

def is_prime(n):
    check = 2
    for check in range(2,int(math.sqrt(n)) + 1):
        if n % check == 0:
            return False
        if n % check != 0:
            check += 1
    return True
    
print(is_prime(15))
print(is_prime(17))
print(is_prime(25))
print(is_prime(26))
print(is_prime(97))
