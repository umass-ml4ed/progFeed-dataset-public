# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    if n<=1:
        return False
    limit=int(n**0.5)
    i=2
    while i<=limit:
        if n%i==0:
            return False
        i+=1
    return True

print(is_prime(17))