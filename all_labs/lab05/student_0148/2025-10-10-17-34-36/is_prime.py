 # Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    i = 2
    if n <= 1:
        return False
    while i <= (n**.5):
        if n % i ==0:
            return False
        i += 1
    return True




