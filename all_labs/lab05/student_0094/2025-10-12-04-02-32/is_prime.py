# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    x = int(n**0.5)
    num = 2
    while num<=x:
     if x>=num:
        if n%num == 0:
           return False
        else:
           if n%(num+1) == 0:
              return False
           else:
              return True
           
print(is_prime(12))

