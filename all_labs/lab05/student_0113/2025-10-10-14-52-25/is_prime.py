#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

def is_prime(n):
    check = 2 
    end = n ** (1/2)
    while check <= end:
        if (n %  check == 0) and (n != check): 
            return False
        else:
            check += 1
    return True 
    
print(is_prime(15))     
print(is_prime(17))     
print(is_prime(25))      
print(is_prime(26))      
print(is_prime(97))      
