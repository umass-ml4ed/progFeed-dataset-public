# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if len(lst) == 0:
        return None  
    if len(lst) == 1:
        return lst[0]
    else:
        max_of_rest = max_recursive(lst[1:])
        return lst[0] if lst[0] > max_of_rest else max_of_rest
    

print(max_recursive([3, 10, 2, 8, 6]))
print(max_recursive([10, 2, 8, 6]))
print(max_recursive([2, 8, 6]))
print(max_recursive([8, 6]))
print(max_recursive([6]))
print(max_recursive([]))
