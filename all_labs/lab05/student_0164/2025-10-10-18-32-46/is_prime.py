# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED
def is_prime(n):
    i = 1
    while i<=n:
        if n % 2 == 0:
            return True 
        if n % 2 != 0:
            return False
        if n % 3 ==0:
            return True 
        if n % 3!= 0:
            return False 
        if n % 4 ==0:
            return True
        if n % 4 != 0:
            return False 
print(is_prime(17))



