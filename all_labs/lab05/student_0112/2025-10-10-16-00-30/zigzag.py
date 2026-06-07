# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
def is_zigzag(lst):
    if len(lst) < 3 : 
        return True
    else:
        i = 1
        while i < (len(lst)-1):
            if not ((lst[i] > lst[i+1] and lst[i] > lst[i-1]) or (lst[i] < lst[i+1] and lst[i] < lst[i-1])):
                return False
            i+=1
        return True
print(is_zigzag([1, 3, 2, 4, 3]) )
