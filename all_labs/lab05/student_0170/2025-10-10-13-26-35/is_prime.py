# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    soot = (n**0.5)
    divisor = 2
    while (divisor <= soot):
        if(n%divisor == 0):
            return False
        divisor += 1
    return True