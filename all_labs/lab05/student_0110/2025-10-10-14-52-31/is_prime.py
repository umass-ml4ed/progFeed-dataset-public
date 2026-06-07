# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def is_prime(number):
    test = 2
    while test <= int(number**0.5):
        if number%test == 0:
            return False
        test += 1
    return True

print(is_prime(15))
print(is_prime(17))
print(is_prime(25))
print(is_prime(26))
print(is_prime(97))