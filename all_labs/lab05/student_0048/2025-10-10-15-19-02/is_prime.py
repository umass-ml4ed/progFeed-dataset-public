# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED


def is_prime(n):
    num = n
    i = 1
    while i <= num**0.5:
        i += 1
        if num%i == 0:
            return False
    return True

print(is_prime(15))
print(is_prime(17))
print(is_prime(25))
print(is_prime(26))
print(is_prime(97)) 
    