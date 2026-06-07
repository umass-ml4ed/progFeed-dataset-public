# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def max_recursive(lst):
    if not lst:
        return 0
    if len(lst) == 1:
        return lst[0]
    
    rest_max = max_recursive(lst[1:])

    if lst[0] > rest_max:
        return lst[0]
    else:
        return rest_max
    
#print(max_recursive([3, 10, 2, 8, 6])) # returns 10
#print(max_recursive([1]))           # returns 1
#print(max_recursive([]))             # returns 0

def sum_lists_recursive(lst1,lst2):
    if not lst1 and not lst2:   
        return 0
    
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])

#print(sum_lists_recursive([1, 2, 3], [4, 5, 6])) # returns 21
#print(sum_lists_recursive([],[]) )               # returns 0

def funky(n):
    if n == 0 or n == 1:
        return 1
    elif n % 2 == 0:  
        return 2 * funky(n // 2)
    else:              
        return 1 + 2 * funky(n + 1)
    
#print(funky(2))
#print(funky(10))

def permutations(lis):
    if len(lis) == 1:
        return [lis]
    
    retlis = []
    
    for i in range(len(lis)):
        front_item = lis[i]
        remaining = lis[:i] + lis[i+1:]
        sub_permutations = permutations(remaining)
        
        for perm in sub_permutations:
            new_perm = [front_item] + perm
            retlis.append(new_perm)
            
    return retlis
