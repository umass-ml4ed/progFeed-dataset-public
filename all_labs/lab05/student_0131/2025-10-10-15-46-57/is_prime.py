# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def is_prime(n):
    # A prime number must be greater than 1
    if n <= 1:
        return False

    # Start checking divisors from 2 up to √n
    i = 2
    while i <= int(n ** 0.5):
        # If n is divisible by i, then it's not a prime
        if n % i == 0:
            return False
        i += 1  # move to the next possible divisor

    # If the loop finishes without finding a divisor, it's prime
    return True


# Test cases
print(is_prime(15))   # False
print(is_prime(17))   # True
print(is_prime(25))   # False
print(is_prime(26))   # False
print(is_prime(97))   # True