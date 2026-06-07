# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    if n <= 1:
        return False
    
    integer = 2
    while (integer <= int(n ** 0.5)):
        if n % integer == 0:
            return False
        integer += 1
    
    return True

            

        

    


print(is_prime(15))      
print(is_prime(17))      
print(is_prime(25))      
print(is_prime(26))      
print(is_prime(97))      





