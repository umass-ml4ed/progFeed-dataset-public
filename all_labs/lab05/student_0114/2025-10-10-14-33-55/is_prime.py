# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    num = 2
    while num <= int(n**0.5):
        if n % num == 0:
            return False
        num += 1
    return True

print(is_prime(15))      #⇒ False
print(is_prime(17))      #⇒ True
print(is_prime(25))      #⇒ False
print(is_prime(26))      #⇒ False
print(is_prime(97))      #⇒ True
