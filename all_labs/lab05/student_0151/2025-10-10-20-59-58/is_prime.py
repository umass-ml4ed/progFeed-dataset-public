# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
import math

def is_prime(n):

  i = 2
  while i < int(math.sqrt(n)) + 1:
    if n % i == 0:
      return False
    
    i += 1
  
  return True