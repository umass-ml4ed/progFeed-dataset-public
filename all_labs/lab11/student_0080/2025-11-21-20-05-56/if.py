# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]
    max_of_rest = max_recursive(lst[1:])
    return lst[0] if lst[0] > max_of_rest else max_of_rest


def sum_lists_recursive(lst1, lst2):
    if len(lst1) == 0:
        return 0
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])


def funky(n):
    if n == 0:
        return 2
    
    if n > 0:
        return 2 * funky(n - 1) - 3
    else:  
        return 3 * funky(n + 1) + 2

def permutations(lis):
    if len(lis) == 1:
        return [lis]
    
    retlis = []
    
    for i in range(len(lis)):
        front_item = lis[i]
        
        remaining = lis[:i] + lis[i+1:]
        for perm in permutations(remaining):
            retlis.append([front_item] + perm)
    
    return retlis




if __name__ == "__main__":  
    print(max_recursive([3, 10, 2, 8, 6]))  
    print(sum_lists_recursive([2, 3], [5, 6]))     
    print(funky(2))   
    print(funky(10))   
    print(permutations(['AA', 'BB', 'CC']))
   