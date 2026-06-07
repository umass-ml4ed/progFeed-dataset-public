#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

def is_prime(n: int) -> bool:
    count = 2
    while count <= int(n**0.5):
        if n % count == 0:
            return False
        else:
            count += 1
    return True
            
    

