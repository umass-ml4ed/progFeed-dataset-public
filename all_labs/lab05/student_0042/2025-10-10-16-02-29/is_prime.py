# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED



def is_prime(n):
    t = n**0.5
    b = 2
    while b<=t:
        if n % b == 0:
            return False
        else:
            b = b+1
    return True
    


