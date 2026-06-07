# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED

def is_prime(a):
    i = 2
    n = a**.5 + 1
    if a == 1:
        return (False)
    while i<n:
        b = a%i
        if b == 0:
            return (False)
        i = i+1
    return (True)

