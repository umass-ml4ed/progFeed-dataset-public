# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    i = 2
    while True:
        if n % i != 0:
           i += 1
        if n % i == 0:
            return False
        if i > int(n**0.5):
           break
        else:
            return True