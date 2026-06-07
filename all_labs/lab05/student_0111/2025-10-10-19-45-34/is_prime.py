# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    if n<=1:
        return False
    x=2
    while x<=int(n**0.5):
        if n%x==0:
            return False
        return True
print(is_prime(15))

