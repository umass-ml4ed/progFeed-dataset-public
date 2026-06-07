# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
def is_prime(n:int) :
    i=2
    check = True
    rootn = n**0.5
    while i<=rootn  :
        if n%i==0 :
            check = False
            break
        i=i+1
    return check

print(is_prime(15))      #⇒ False
print(is_prime(17))      #⇒ True
print(is_prime(25))      #⇒ False
print(is_prime(26))      #⇒ False
print(is_prime(97))      #⇒ True
