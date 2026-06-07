# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    nsquareroot=int(n**0.5)
    divisor=2
    num=''
    if n<=3:
        num = 'prime'
    else:
        while divisor<=nsquareroot:
         if n % divisor == 0:
            num='not prime'
            break
         else:
            divisor+=1
            num='prime'    

    if num == 'not prime':
        return False
    if num == 'prime':
        return True

    
print(is_prime(3))
print(is_prime(17))
print(is_prime(25))
print(is_prime(26)) 
print(is_prime(97))
