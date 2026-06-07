# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
        u = 2
        while u <= int(n ** 0.5):
             if n % u == 0:
                  return False
             else:
                  u += 1
        return True

print(is_prime(7))


        