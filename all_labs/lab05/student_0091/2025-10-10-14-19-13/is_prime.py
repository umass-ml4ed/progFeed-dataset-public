# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n:int)->bool:
    i=2
    while i>= 2 and i<=int(n**0.5):
        if n % i == 0:
            return False
        elif n % i != 0:
            i +=1

    return True

print(is_prime(15))      #False
print(is_prime(17))      #True
print(is_prime(25))      #False
print(is_prime(26))      #False
print(is_prime(97))      #True
