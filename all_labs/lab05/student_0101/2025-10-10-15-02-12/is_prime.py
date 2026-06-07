# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    n = int(n)
    d = 2
    while d <= n**.5:
        if n%d == 0:
            return False
        else:
            d += 1
    if d > n**.5:
        return True
print(is_prime(15)) 
print(is_prime(17))
print(is_prime(25))
print(is_prime(26))
print(is_prime(97))

