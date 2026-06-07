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
    
    
def sum_lists_recursive(l1,l2):
    final_sum = 0
    if len(l1) == 0 and len(l2) == 0:
        return final_sum
   
    return l1[0] + l2[0] + sum_lists_recursive(l1[1:],l2[1:])



    
def funky(n):
    if n == 1 or n == 0:
        return 1
    elif n % 2 == 0:
        return 2 * funky(n//2)
    else:
        return 1 + 2 * funky(n+1)

