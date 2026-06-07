# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def max_recursive(lst):
    if lst == []:
        return 0
    if len(lst) == 1:
        return lst[0]

    first = lst[0]
    max_rest = max_recursive(lst[1:])
    if first >= max_rest:
        return first
    else:
        return max_rest
    
print(max_recursive([3, 10, 2, 8, 6])) #10
print(max_recursive([10, 2, 8, 6]))   #10
print(max_recursive([2, 8, 6]))  #8

def sum_lists_recursive(lst1, lst2):
    if lst1 == [] and lst2 == []:
        return 0

    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])

print(sum_lists_recursive([1, 2, 3], [4, 5, 6]))  # 21
print(sum_lists_recursive([2, 3], [5, 6]))   # 16
print(sum_lists_recursive([3], [6]))     # 9


def funky(n):
    if n == 0 or n == 1:
        return 1
    elif n % 2 == 0:  
        return 2 * funky(n // 2)
    else:             
        return 1 + 2 * funky(n + 1)
    
print(funky(2))    # 2
print(funky(10))   # 74
print(funky(50))   # 554

def permutations(lis):
    if len(lis) == 1:
        return [lis[:]]  

    result = []
    for i in range(len(lis)):
        front = lis[i]
        remaining = lis[:i] + lis[i+1:]
        perms = permutations(remaining)
        for p in perms:
            result.append([front] + p)
    return result
print(permutations(['AA']))                   # [['AA']]
print(permutations(['AA', 'BB']))            # [['AA','BB'], ['BB','AA']]
print(permutations(['AA', 'BB', 'CC']))  