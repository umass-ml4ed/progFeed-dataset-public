# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def max_recursive(lst):
    if not lst:
        return 0
    elif len(lst) == 1:
        return lst[0]
    else:
        max = max_recursive(lst[1:])
        if lst[0] > max:        
            return lst[0]       
        else:   
            return max

            
print(max_recursive([3, 10, 2, 8, 6])) # returns 10
