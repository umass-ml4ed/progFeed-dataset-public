# Author : REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_prime(n: int):
    i = 2  
    if n > 1:
        while i <= int(n**0.5):
            if n % i == 0:
                return False
            i += 1
        return True
    else:
        return False

print(is_prime(15)) 
print(is_prime(17))
print(is_prime(25))
print(is_prime(26)) 
print(is_prime(97))