# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    iterator = 2
    while iterator <= int(n*0.5):
        if n % iterator == 0:
            return False
        iterator += 1
    return True
