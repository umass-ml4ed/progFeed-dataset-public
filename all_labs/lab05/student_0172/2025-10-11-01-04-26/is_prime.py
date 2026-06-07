# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i <= int(n ** 0.5):
        if n % i == False:
            return False
        i += 1

    return True
