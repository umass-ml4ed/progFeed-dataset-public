# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    counter = 2
    while counter <= n**0.5:
        if n % counter == 0:
            counter += 1
            return False
        counter += 1
    return True


