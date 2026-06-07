# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if len(lst) == 0:
        return 0  
    if len(lst) == 1:
        return lst[0]
    else:
        max_of_rest = max_recursive(lst[1:])
        return lst[0] if lst[0] > max_of_rest else max_of_rest
    

def sum_lists_recursive(lst1, lst2):
    if len(lst1) == 0 and len(lst2) == 0:
        return 0
    val1 = lst1[0] if len(lst1) > 0 else 0
    val2 = lst2[0] if len(lst2) > 0 else 0
    return val1 + val2 + sum_lists_recursive(lst1[1:] if len(lst1) > 0 else [], lst2[1:] if len(lst2) > 0 else [])


def funky(n):
    if n <= 1:
        return 1
    elif n % 2 == 0:
        return (2 * funky(n // 2))
    else:
        return (1 +2 * funky(n + 1))

# print(max_recursive([3, 10, 2, 8, 6]))
# print(max_recursive([10, 2, 8, 6]))
# print(max_recursive([2, 8, 6]))
# print(max_recursive([8, 6]))
# print(max_recursive([6]))
# print(max_recursive([]))

# print(sum_lists_recursive([1, 2, 3], [4, 5, 6])) 
# print(sum_lists_recursive([2, 3], [5, 6]))     
# print(sum_lists_recursive([3], [6]))           
# print(sum_lists_recursive([],[]))             
print(funky(2)) 
print(funky(10))
# , funky(50)=554, funky(-10)=50, funky(-50)=418

