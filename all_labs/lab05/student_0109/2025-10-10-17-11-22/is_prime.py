#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

def is_prime(n):
    d = 2
    while d <= int(n**0.5):
        if n%d == 0:
            return False
        d += 1
    return True