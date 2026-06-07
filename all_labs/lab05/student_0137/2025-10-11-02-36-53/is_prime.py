# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def is_prime(n):
    """Return True if n is a prime number, otherwise False."""
    if n <= 1:
        return False

    divisor = 2
    while divisor <= int(n ** 0.5):
        if n % divisor == 0:
            return False
        divisor += 1

    return True

print(is_prime(15))  
print(is_prime(17))  
print(is_prime(25))