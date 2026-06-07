# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
   
    if len(lst) == 0:
        return 0
    
    if len(lst) == 1:
        return lst[0]
    
    max_rest = max_recursive(lst[1:])
    if lst[0] > max_rest:
        return lst[0]
    else:
        return max_rest
    

def sum_lists_recursive(lst1,lst2):
    if lst1 == lst2 == []:
        return 0
    else:
        return lst1[0]+lst2[0]+ sum_lists_recursive(lst1[1:],lst2[1:])   



def funky(n):
    if n == 0 or n ==1:
        return 1
    elif n%2 == 0:
        return 2*funky(n//2)
    else:
        return 1+ 2*funky(n+1)
    
def permutations(lis):
    if len(lis) == 1 or len(lis) == 0:
        return [lis]
    retlis = []
    for i in range(len(lis)):
        front_item = lis[i]
        remaining = [ lis[j] for j in range(len(lis)) if j != i ] 
        for item in permutations(remaining):
            item.insert(0,front_item)
            retlis.append(item)
    return retlis







