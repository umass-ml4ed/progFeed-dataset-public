#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

def max_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    rest_max = max_recursive(lst[1:])
    return lst[0] if lst[0] > rest_max else rest_max
    
    
print(max_recursive([1,2,3,4, 8, 100, 90]))