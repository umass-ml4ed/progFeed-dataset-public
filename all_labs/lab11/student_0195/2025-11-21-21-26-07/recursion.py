# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if len(lst) == 0:
        return 0
    else :
        elem1 = lst[0]
        rest = max_recursive(lst[1:0])
        if elem1 > rest:
            return elem1
        else:
            return rest
        

def sum_lists_recursive(lst1,lst2):
    if (len(lst1) == 0 and len(lst2) == 0):
        return 0
    else:
        csum = lst1[0]+lst2[0]
        return csum + sum_lists_recursive(lst1[1:],lst2[1:])
    

def funky(n):
    if (n == 0) or (n == 1):
        return 1
    elif (n%2 == 0):
        return (2*funky((n//2)))
    else:
        return (1 + (2* (funky((n+1)))))
    
