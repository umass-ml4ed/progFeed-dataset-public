# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    a=2
    while a<=(n**0.5):
        if n%a==0:
            return False
        a+=1
    return True

print(is_prime(15))     
print(is_prime(17))      
print(is_prime(25))      
print(is_prime(26))      
print(is_prime(97))  
