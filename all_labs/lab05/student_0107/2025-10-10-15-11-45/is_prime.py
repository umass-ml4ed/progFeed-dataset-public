# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_prime(x):
    i = 2
    statement = True 
    while i <= x-1:
        if x%i == 0:
            statement = False 
            return statement
        else:
            statement = True
        i+=1 
    return statement 

print(is_prime(15))      #⇒ False
print(is_prime(17))      #⇒ True
print(is_prime(25))      #⇒ False
print(is_prime(26))      #⇒ False
print(is_prime(97))      #⇒ True


    


