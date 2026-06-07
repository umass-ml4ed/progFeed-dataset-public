# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    """"
    Checks if an integer n is a prime number.

    Args:
        n: An integer.

    Returns:
        True if n is prime, False otherwise.
    """
    if n < 2:  # Numbers less than 2 are not prime
        return False

    i = 2
    while i <= n:
        if n % i == 0:
            if i == n:
                return True
            else:  
                return False
        i += 1
    return True

print(is_prime(15))
print(is_prime(17))
print(is_prime(25))
print(is_prime(26))
print(is_prime(97))
