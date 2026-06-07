# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_prime(n):
    i = 2
    while i < n ** 1/2:
        print(n)
        if n % i == 0:
            return False
        i += 1
    return n > 1

