# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if not lst:
        return 0
    if len(lst) == 1:
        return lst[0]
    rest_max = max_recursive(lst[1:])
    return lst[0] if lst[0] > rest_max else rest_max
print(max_recursive([3, 10, 2, 8, 6]))
print(max_recursive([8, 6]))
print(max_recursive([]))

def sum_lists_recursive(lst1, lst2):
    if not len(lst1) and not len(lst2):
        return 0
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])
print(sum_lists_recursive([1, 2, 3], [4, 5, 6]))
print(sum_lists_recursive([3], [6]))
print(sum_lists_recursive([],[]))

def funky(n):
    if n == 0 or n == 1:
        return 1
    if n % 2 == 0:
        return 2 * funky(n // 2)
    return 1 + 2 * funky(n + 1)
print(funky(2))
print(funky(50))

def permutations(lis):
    if len(lis) == 1:
        return [lis]
    retlis = [] 
    for i in range(len(lis)):
        front_item = lis[i]
        remaining = lis[:i] + lis[i+1:]
        perms_of_remaining = permutations(remaining)
        for p in perms_of_remaining:
            retlis.append([front_item] + p)
    return retlis
print(permutations(['AA']))
print(permutations(['AA','BB']))
print(permutations(['AA','BB','CC']))