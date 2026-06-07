# Author    : REDACTED
# Email     : REDACTED
# Spire ID  : REDACTED


def is_prime(n)->int:
    if n <= 1:
        return False 
    a = 2
    while a<=int((n**0.5)):
        if n % a == 0:
            return False
        a += 1
    return True 
    

print(is_prime(15))      # False
print(is_prime(17))      # True
print(is_prime(25))      # False
print(is_prime(26))      # False
print(is_prime(97))      # True
