# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    x=2
    
    while x<= int(n**0.5):
        if n%x ==0:
            return False
        else:
            x+=1
    return True
