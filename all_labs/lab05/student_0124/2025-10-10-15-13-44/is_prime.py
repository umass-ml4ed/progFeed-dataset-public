# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_prime(n:int) -> bool:
    isprime = True
    i = 2
    while i <= int(n ** 0.5):
        if n % i == 0 or n == 1:
            isprime = False
            return isprime
        i += 1
    return isprime

