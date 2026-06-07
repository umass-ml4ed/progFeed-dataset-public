# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    factor=2
    while factor<=int(n**.5):
        if n%factor !=0:
            factor+=1
        else:
            return False
    return True

print(is_prime(98))