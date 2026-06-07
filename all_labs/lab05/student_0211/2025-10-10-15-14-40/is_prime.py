# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n: int):
    i = 2
    while(i <= int(n**0.5)):
        if(n % i == 0):
            return False
        i += 1
    else :
        return True
    
print(is_prime(15))      #⇒ False
print(is_prime(17))      #⇒ True
print(is_prime(25))      #⇒ False
print(is_prime(26))      #⇒ False
print(is_prime(97))      #⇒ True

        


