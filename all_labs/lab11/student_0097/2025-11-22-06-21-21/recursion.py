# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

'''
list1 = [1,2,4,5,7,9]
def max_recursive(lst):
    if lst == 0:
        return 0
    new_case = lst > lst(range(0,10))
#Would it be better to reduce each number till we only have the "Highest" left
#Or should we work through the len. Or both? 
    return max_recursive(new_case)

print(max_recursive(list1))

#need to be recursion only. NO loops.
#integers or floats only. all positive

def sum_lists_recursive(lst1, lst2):
'''

def max_recursive(lst):
    # Base case: empty list → return 0
    if len(lst) == 0:
        return 0
    
    # Base case: one element → return it
    if len(lst) == 1:
        return lst[0]
    
    # Recursive step:
    max_rest = max_recursive(lst[1:])
    return lst[0] if lst[0] > max_rest else max_rest

def sum_lists_recursive(lst1, lst2):
    # Base case: both empty
    if len(lst1) == 0 and len(lst2) == 0:
        return 0
    
    # Recursive step
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])

def funky(n):
    # base case
    if n == 0:
        return 1
    
    # positive side
    if n > 0:
        if n == 1:
            return 1
        return funky(n - 1) + (2 * n - 3)
    
    # negative side
    if n == -1:
        return 1
    
    return funky(n + 1) + (-2 * n - 3)
    
def permutations(lis):
    # Base case
    if len(lis) == 1:
        return [lis[:]]  # list of lists
    
    retlis = []
    
    for i in range(len(lis)):
        front_item = lis[i]
        
        # Remaining items (everything except index i)
        remaining = lis[:i] + lis[i+1:]
        
        # Recursively get permutations of the smaller list
        sub_perms = permutations(remaining)
        
        # Add front_item to the front of each permutation
        for p in sub_perms:
            retlis.append([front_item] + p)
    
    return retlis
