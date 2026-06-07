#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

def max_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    rest_max = max_recursive(lst[1:])
    return lst[0] if lst[0] > rest_max else rest_max
    
    
print(max_recursive([1,2,3,4, 8, 100, 90]))

def sum_lists_recursive(lst1, lst2):
    if len(lst1)==0 and len(lst2)==0:
        return 0
    x = lst1[0]+lst2[0]
    res = sum_lists_recursive(lst1[1:], lst2[1:])
    return x +res
print(sum_lists_recursive([1, 2, 3], [4, 5, 6]))

def funky(x):
    if x ==0 or x == 1:
        return 1
    elif x %2==0:
        return 2*funky(x//2)
    else:
        return 1+2*funky(x+1)
    
print(funky(50))
    


    