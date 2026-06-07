# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

import math

def is_prime(n):
    index = 2
    prime = True #when you return, the loop stops
    while(index <= math.sqrt(n)):
        if(n%index == 0): #if n is divisible
            prime = False
        #else:
        #    prime = True
        index += 1
    return prime

print(is_prime(15))
print(is_prime(17))
print(is_prime(25))