# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    i=2
    a = (n)**0.5
    while i <= a:
        if n % i == 0: 
            return False
        else: 
            i+=1
    return True


