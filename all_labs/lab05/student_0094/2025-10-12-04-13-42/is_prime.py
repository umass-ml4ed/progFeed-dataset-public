# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    if n < 2:
        return False
    x = int(n**0.5)       
    num = 2
    while num <= x:
        if n % num == 0:     
            return False
        num += 1             
    return True              


print(is_prime(12)) 
print(is_prime(13))  

print(is_prime(12))

