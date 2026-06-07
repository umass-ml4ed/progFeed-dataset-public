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

def sum_lists_recursive(lst1, lst2):
    if not lst1 and not lst2:
        return []
    elif not lst1:
        return lst2
    elif not lst2:
        return lst1
    else:
        sum1 = lst1[0] + lst2[0]
        return [sum1] + sum_lists_recursive(lst1[1:], lst2[1:])
    
def funky(n):
    if n <= 0:
        return 0
    elif n % 2 == 0:
        return 2 * funky(n//2)
    else:
        return 1 + 2 * funky(n +1)
    
def permutations(lis):
    if len(lis)==1:
        return [lis] 
    retlist = []
    for i in range(len(lis)):
        front_item= lis[i]
        remaining = lis[:i] + lis[i+1:]
        for p in permutations(remaining):
            retlist.append([front_item]+p)
    return retlist

