# Author : REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_prime(n: int):   
    if n > 0:
        while n % 2 and n % 3 and n % 4 and int(n ** 0.5):
            return False
        else:
            return True
    else:
        return False

print(is_prime(15)) 
print(is_prime(17))
print(is_prime(25))
print(is_prime(26)) 
print(is_prime(97))