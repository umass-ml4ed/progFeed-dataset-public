# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED

def is_prime(x):
    if x <= 1:
        return False

    n = 2
    while n * n <= x:
        if x % n == 0:
            return False
        n += 1
    return True

print(is_prime(25))  
print(is_prime(13))  
