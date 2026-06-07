# Author : REDACTED
# Email : REDACTED
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
        
print(is_prime(17))
print(is_prime(14))
print(is_prime(15))


