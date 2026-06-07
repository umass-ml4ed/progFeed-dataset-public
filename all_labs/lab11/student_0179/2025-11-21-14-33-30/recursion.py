# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    i = 0
    if len(lst) == i:
        return 
    i += 1

def sum_lists_recursive(lst1, lst2):
    i = 0
    if len(lst1[i:]) < 1:
        return 0
    return lst1[i] + lst2[i] + sum_lists_recursive(lst1[i + 1:],lst2[i + 1:])

print(sum_lists_recursive([1, 2, 3], [4, 5, 6]))
print(sum_lists_recursive([2, 3], [5, 6]))
print(sum_lists_recursive([3],[6]))
print(sum_lists_recursive([],[]))