# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_prime(n):
    if n < 2:
        return False
    div = 2
    while div <= int(n ** 0.5):
        if n % div == 0:
            return False
        div += 1
    return True

print(is_prime(15))  
print(is_prime(17))
print(is_prime(25))
print(is_prime(26))    
print(is_prime(97))  
