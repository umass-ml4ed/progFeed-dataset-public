# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n): 
    m = int(n**0.5)
    prime = True
    for i in range(n,m+1): 
        if n % i == 0: 
            prime = False
            break
    return prime

