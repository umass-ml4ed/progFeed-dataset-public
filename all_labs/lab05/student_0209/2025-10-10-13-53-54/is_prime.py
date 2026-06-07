# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def is_prime(n):
    while n>1:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
    return False

