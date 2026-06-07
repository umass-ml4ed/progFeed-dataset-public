# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    for count in range(2, int(n**0.5) + 1):
        if n % count == 0:
            return True
        else:
            if count == int(n**0.5):
                return False
    '''
    count = 2
    prime = True
    while n % count != 0 and count <= int(n**0.5):
        if count == int(n**0.05):
            prime = False
        count += 1
    return prime
    '''

print(is_prime(15))
print(is_prime(17))
print(is_prime(25))
print(is_prime(26))
print(is_prime(97))