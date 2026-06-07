# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    upper_bound = int(n**0.5)
    lower_bound = 2
    while lower_bound <= upper_bound:
        if n % lower_bound == 0:
            return False
        lower_bound += 1
    return True

