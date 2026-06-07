# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

#
def is_prime(n):
    if n > 0: 
        if n % 2 != 0 and n % 3 != 0:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
    elif n < 0:
        if n % 2 == 0 or n % 3 == 0:
            return False
    else:
        return False
    
print(is_prime(15))
print(is_prime(17))
print(is_prime(9))
print(is_prime(25))
print(is_prime(26))
print(is_prime(97))
