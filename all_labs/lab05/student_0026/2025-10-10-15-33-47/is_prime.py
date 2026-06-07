# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    nsquareroot=int(n**0.5)
    divisor=2
    while divisor<=nsquareroot:
        if n % divisor == 0:
            num='not prime'
            break
        if n % divisor != 0:
            divisor+=1
            num='prime'    

    if num == 'not prime':
        return False
    if num == 'prime':
        return True

