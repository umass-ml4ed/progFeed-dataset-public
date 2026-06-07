def is_prime(n: bool):
    i=2
    while i<=int(n**.5):
        if n%i==0:
            return False
        else:
            if i<int(n**.5):
                i+=1
                continue
            else:
                return True
            
print(is_prime(15))      # False
print(is_prime(17))      # True
print(is_prime(25))      # False
print(is_prime(26))      # False
print(is_prime(97))      # True
