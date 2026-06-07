 # Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    i = 2
    if n <= 1:
        return False
    while i < (n**.5)+1:
        if n % i ==0:
            return False
        i += 1
    return True

print(is_prime(15))
print(is_prime(17))
print(is_prime(25))
print(is_prime(26))
print(is_prime(97))


