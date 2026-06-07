# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    i = int(n**0.5)
    x = 2
    while x<=i:
        if n%x == 0:
            return False
        else:
            x+=1
    return True
