# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED


def is_prime(n):
    root = int(n**1/2)
    a = 2
    # print(root)
    while (a <= root):
        if (n % a == 0):
            # print(n%a)
            return False
        else :
            a += 1
            continue
    return True


print(is_prime(15))      
print(is_prime(17))       
print(is_prime(25))       
print(is_prime(26))       
print(is_prime(97))       
