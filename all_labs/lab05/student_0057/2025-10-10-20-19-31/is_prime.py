# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i <= int(n**0.5):
        if n % i == 0:
            return False
        i += 1
    return True
print(is_prime(15))
print(is_prime(17))
print(is_prime(25)) 
print(is_prime(26))
print(is_prime(97))
a=1
b=97
count = 0                       # initialize the count variable
for number in range(a, b+1):    # note: b+1 as you want b to be included
  if is_prime(number):          # call is_prime to check if n is prime
    count += 1                  # if True, increment count
print(f'There are {count} prime numbers between [{a}, {b}]')
