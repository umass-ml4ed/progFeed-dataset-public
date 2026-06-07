# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    n = int(n)
    a = round(n**0.5)
    m = 2
    while m <= a :
        if n%m == 0:
            return False
        else:
            m += 1
        if m == a and n%m != 0:
                return True

print (is_prime(15))
print (is_prime(17))
print (is_prime(25))
print (is_prime(26))
print (is_prime(97))