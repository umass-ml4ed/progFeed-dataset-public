# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    
    if lst == []:
        return 0
    
    
    if len(lst) == 1:
        return lst[0]
    
  
    max_rest = max_recursive(lst[1:])
    return lst[0] if lst[0] > max_rest else max_rest


def sum_lists_recursive(lst1, lst2):
    
    if lst1 == [] and lst2 == []:
        return 0
    
    
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])

def permutations(lis):
    
    if len(lis) == 1:
        return [lis]
    
    retlis = []
    
    for i in range(len(lis)):
        front_item = lis[i]
        remaining = lis[:i] + lis[i+1:]
        
        subperms = permutations(remaining)
        
        for p in subperms:
            retlis.append([front_item] + p)
    
    return retlis


funky(2) = 2
funky(10) = 74
funky(50) = 554
funky(-10) = 50
funky(-50) = 418
