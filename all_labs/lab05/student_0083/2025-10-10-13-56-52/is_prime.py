# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    i = 2
    n_root = int(n ** 0.5)
    while i < n_root:
        if n % i != 0:
            i += 1
            prime_check = True
        elif n % i == 0:
            return False
    if prime_check == True:
        return True

       

