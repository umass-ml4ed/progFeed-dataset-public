# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    num = 2
    while 2 <= num <= int(n ** 0.5):
        if n % num == 0:
            return False
        num += 1
    else:
        return True

print(is_prime(15))
print(is_prime(17))
print(is_prime(25))
print(is_prime(26))
print(is_prime(97))