# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    counter = 2
    square = int(n**0.5)
    while counter <= square:
        if (n % counter) == 0:
            return False
        else:
            counter += 1
    return True
