# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    if n < 2:
        return False

    i = 2
    while i <= int(n):
        if n % i == 0 and i != n:
            return False
        i += 1
    
    return True
print(is_prime(15))