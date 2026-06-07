# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    upper_bound = n**0.5
    lower_bound = 2
    while lower_bound <= upper_bound:
        remainder = n%lower_bound
        if remainder == 0:
            Prime = False
            break
        else:
            lower_bound += 1
            Prime = True
    return Prime
