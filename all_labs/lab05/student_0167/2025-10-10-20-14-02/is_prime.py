# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    flag = True
    sqrt_of_int = n**0.5
    i = 2
    while i <= sqrt_of_int:
        if n % i == 0:
            flag = False
            return False
        i = i + 1
    if flag == True:
        return True
    


