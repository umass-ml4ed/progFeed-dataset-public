# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    if n<=1:
        return False
    np=int(n**0.5)
    i=2
    while i<=np:
        if n%i==0:
            return False
        i+=1
    return True

print(is_prime(36))