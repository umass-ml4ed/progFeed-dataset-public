# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    count = 2
    squroot = int(n**0.5)
    while count<=(squroot):
        if(n%count == 0):
            return False
        else:
            count +=1
    return True
    
print(is_prime(15))      # False
print(is_prime(17))      #⇒ True
print(is_prime(25))     # ⇒ False
print(is_prime(26))     # ⇒ False
print(is_prime(97))     # ⇒ True
