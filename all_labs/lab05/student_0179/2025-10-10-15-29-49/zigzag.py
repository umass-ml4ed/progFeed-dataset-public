# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(a):
    if len(a) <= 2:
        return True
    else:
        n = 0
        for b in a[n+1:len(a)-1]:
            if  (b > a[n] and b > a[n+2]) or (b < a[n] and b < a[n+2]):
                n = n + 1
            else:
                return False
        return True


print(is_zigzag([1, 3, 2, 4, 3]))
print(is_zigzag([1, 4, 2, 5, 3])) 
print(is_zigzag([1, 2, 3, 4]))
print(is_zigzag([10]))  
print(is_zigzag([1, 3, 2, 4, 5])) 
#range(len(a))