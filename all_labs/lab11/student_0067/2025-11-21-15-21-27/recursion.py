# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]
    else:
        sub_list = max_recursive(lst[1:])
        
        return lst[0] if lst[0] > sub_list else sub_list
    
    
    
def funky(n):
    if n == 1 or n == 0:
        return 1
    elif n % 2 == 0:
        return 2 * funky(n//2)
    else:
        return 1 + 2 * funky(n+1)

