# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
import math

def is_prime(n):
    if n <= 1:
        return False 
    i = 2
    end = int(n * 0.5)
    while i <= end:
        if n % i == 0:
            return False  
        i += 1

    return True

