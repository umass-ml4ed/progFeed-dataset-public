# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
def is_zigzag(lst):
    if len(lst) < 3 : 
        return True
    else:
        i = 1
        for i in range (len(lst)-1):
            if not ((lst[i] > lst[i+1] and lst[i] >lst[i-1]) or (lst[i] < lst[i+1] and lst[i] < lst[i-1])):
                return False
        return True

