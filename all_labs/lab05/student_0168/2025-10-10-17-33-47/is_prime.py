# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def is_prime(n):
    i=2
    m=int(n**.5)
    while i<=m:
        if n%i==0 or n%m==0:
            return False
        else:
            i=i+1
    else:
        return True

print(is_prime(773))    
print(is_prime(17))    
print(is_prime(25))     
print(is_prime(26))      
print(is_prime(97))      
