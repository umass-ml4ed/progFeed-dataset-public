


def is_prime(a:int):
    cap = int(a ** 0.5)
    
    ans = True
    
    for i in range(2, cap + 1):
        if a % i == 0:
            ans = False
            break 
        
    return ans 

print(is_prime(15))      
print(is_prime(17))      
print(is_prime(25))      
print(is_prime(26))      
print(is_prime(97))
