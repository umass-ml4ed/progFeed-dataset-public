# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(list):
    if len(list) < 1:
        return 0
    if len(list) == 1:
        return list[0]
    if list[0] > list[len(list)-1]:
        return max_recursive(list[0:len(list)-1])
    else:
        return max_recursive(list[1:len(list)])
    
def sum_lists_recursive(lst1, lst2):
    if len(lst1) == 0:
        return 0
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])

def funky(i):
    if i == 1 or i == 0:
        return 1
    if i%2 == 0:
        return 2*funky(i//2)
    else:
        return 1+2*funky(i+1)