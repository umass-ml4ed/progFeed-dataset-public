#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

def is_prime(n):
    x=int(n**(1/2))
    z = 2
    while z<=x:
        if n%z==0:
            return False
        z = z+1
    return True
