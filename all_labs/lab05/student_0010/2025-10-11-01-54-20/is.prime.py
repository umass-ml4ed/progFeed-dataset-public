# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_prime(n):
        i = 2
        if n <= 1:
                return False
        while i <= float(n**0.5):
                if n % i == 0:
                        return False
                
                i = i + 1
        return True


