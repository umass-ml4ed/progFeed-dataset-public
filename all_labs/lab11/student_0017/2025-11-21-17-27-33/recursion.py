# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    
    
    if len(lst) == 0:
        return 0
    
    
    if len(lst) == 1:
        return lst[0]
    
    
    return max(lst[0], max_recursive(lst[1:]))



def sum_lists_recursive(lst1, lst2):
    
    
    if len(lst1) == 0 and len(lst2) == 0:
        return 0
    
    
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])



def funky(n):
    
    
    if n == 0:
        return 1
    if n == 1 or n == -1:
        return 1
    
    
    if n > 0:
        return n*n + funky(n-2)
    else:
        return n*n + funky(n+2)



def permutations(lis):
    
    
    if len(lis) == 1:
        return [lis]
    
    retlis = []
    
    
    for i in range(len(lis)):
        front_item = lis[i]
        
        
        remaining = lis[:i] + lis[i+1:]
        
        
        subperms = permutations(remaining)
        
        
        for perm in subperms:
            retlis.append([front_item] + perm)
    
    return retlis
