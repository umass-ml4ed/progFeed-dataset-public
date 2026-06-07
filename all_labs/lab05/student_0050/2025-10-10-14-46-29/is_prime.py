# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

import math 

def is_prime(n)->bool:
    num = 2
    while num<(math.sqrt(n)):
        if (n%num==0):
            return False
        num+=1
    return True