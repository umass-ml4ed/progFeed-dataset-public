# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    i = 2 
    a = int((n)**0.5)
    while i <= a:
        if n % i ==0 or n % a == 0: 
            return False
        else: 
            return True


