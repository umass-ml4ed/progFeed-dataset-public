# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

i = 2
def is_prime(n):
    i = 2
    e = int(n**.5)
    while i<=e:
        if n%i == 0:
            return False
        else:
            i += 1
    return True

print(is_prime(15))
print(is_prime(17))
print(is_prime(25))
print(is_prime(26))
print(is_prime(97))
