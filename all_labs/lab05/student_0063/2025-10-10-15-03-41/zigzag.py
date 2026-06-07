# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED


'''
Write a function, called is_prime, that takes an integer n as a parameter, 
and returns a boolean value representing whether it’s prime. 
Inside the function, you should write a while loop that iterates from 2 to int(n) 
inclusive on both ends and check if n is divisible by any of them 
(think about how to check if one integer is divisible by another). 
If so, you can directly return False (i.e., not a prime) in the loop. 
A return in a loop causes the loop to terminate immediately and causes the function to exit as well. 
After the loop, think about what one instruction you should put there.
Hint: this would be where the loop is done, and it didn’t find any divisor of integer n, 
which indicates n is a prime.

n = 20
i = 1         # initialize loop control variable i
while i<=n:   # loop condition
  print(i)    # print i
  i += 1      # increment loop control variable i
'''
def is_prime(n):
    i = 2
    while i < n:
        print(n)
        if n % i == 0:
            return False
        i += 1
    return n > 1



print(is_prime(15))     
print(is_prime(17))     
print(is_prime(25))      
print(is_prime(26))     
print(is_prime(97)) 
