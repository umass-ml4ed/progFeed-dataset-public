# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
i=2
def is_prime(n):
    m=int(n**.5)
    while i<=m:
        if n%i==0 or n%m==0:
            return False
        else:
            return True
    else:
        return True
print(is_prime(3))    
print(is_prime(17))    
print(is_prime(25))     
print(is_prime(26))      
print(is_prime(97))      
