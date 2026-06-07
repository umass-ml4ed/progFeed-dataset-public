# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
import math
def is_prime(n):
    i=2
    while(i<int(n**0.5)+1):
        if n%i==0:
            return False
        else: i+=1
    return True
