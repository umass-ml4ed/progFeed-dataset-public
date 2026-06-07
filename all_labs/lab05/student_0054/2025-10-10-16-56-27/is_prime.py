# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED


""" Given an integer n, one way to check whether 
it is prime is to check if it is divisible by any integer
from 2 to root square n (inclusive on both ends)"""
def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i <= int(n ** 0.5):
        if n % i == 0:
            return False
        i += 1
    
    return True