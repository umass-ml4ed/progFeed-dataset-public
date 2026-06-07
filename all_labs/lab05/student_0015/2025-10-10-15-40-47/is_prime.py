# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

# Description: This program defines a function is_prime(n) that checks
#              whether a given integer n is a prime number or not.


def is_prime(n):
    # Prime numbers are greater than 1
    if n <= 1:
        return False  # 0, 1, and negative numbers are not prime

    # Start checking divisibility from 2 up to the square root of n
    i = 2  # Initialize the loop variable

    # Loop continues as long as i is less than or equal to sqrt(n)
    # Using int(n**0.5) ensures we only check up to the square root
    while i <= int(n**0.5):
        # Check if n is divisible by i
        if n % i == 0:
            # If divisible, n is NOT a prime
            return False  # Immediately exit the function
        # Increment i to test the next number
        i += 1

    # If the loop completes without finding a divisor,
    # then n is a prime number
    return True


''' # ------------------ Example Test Calls ------------------
# These print statements are just for testing purposes.

print(is_prime(15))   # Expected output: False (15 = 3 × 5)
print(is_prime(17))   # Expected output: True  (only divisible by 1 and 17)
print(is_prime(25))   # Expected output: False (25 = 5 × 5)
print(is_prime(26))   # Expected output: False (26 = 2 × 13)
print(is_prime(97))   # Expected output: True  (prime number)'''
