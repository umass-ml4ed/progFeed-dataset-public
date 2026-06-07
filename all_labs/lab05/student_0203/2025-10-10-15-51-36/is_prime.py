# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
   i = 2
   m = int(n**0.5)
   while i <= m:
    if n % i == 0:
      return False
    else:
      i += 1
   return True

   
print(is_prime(15))   
