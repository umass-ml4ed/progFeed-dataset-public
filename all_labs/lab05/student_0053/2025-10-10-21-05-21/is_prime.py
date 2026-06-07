# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n: int) -> int:
    '''This function will check whether a number is a prime number'''
    i = 2
    while 2 <= i <= int(n**0.5):
        if n % i == 0:
            return False
        i += 1
    else:
        return True
    
