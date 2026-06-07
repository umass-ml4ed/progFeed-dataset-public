# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    x = 2
    while x <= int(n ** 0.5):
        if n % x == 0:
            return False
        x += 1
    return True

print(is_prime(15))
print(is_prime(17))
print(is_prime(25))
print(is_prime(26))
print(is_prime(97))
