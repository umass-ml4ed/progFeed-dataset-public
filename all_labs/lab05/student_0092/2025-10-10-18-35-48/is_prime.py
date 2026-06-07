# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n: int) -> bool:
    i = 2
    while i <= int(n**(1/2)):
        if n % i == 0:
            return False
        i+=1
    return True