# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    # print(lst)
    if len(lst) > 1 and lst[0] < lst[1]:
        return max_recursive(lst[1::])
    if len(lst) == 0:
        return 0
    return lst[0] + max_recursive[lst]

# g = [20 - i for i in range(10)]
# h = [15 - i for i in range(20) if i % 2 == 0]

# print(max_recursive([]))

def sum_lists_recursive(lst1, lst2):
    # print(lst1, lst2)
    if len(lst1) > 1 and len(lst2) > 1:
        return lst1[0] + lst2[0]+ sum_lists_recursive(lst1[1::], lst2[1::])
    return lst1[0] + lst2[0]

# print(sum(g) + sum(h))
# print(sum_lists_recursive([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))

def funky(n):
    if n == 1 or n == 0:
        return 1
    if n % 2 == 0:
        return 2 * funky(n // 2)
    return 1 + 2 * funky(n + 1)

# print(funky(-50))