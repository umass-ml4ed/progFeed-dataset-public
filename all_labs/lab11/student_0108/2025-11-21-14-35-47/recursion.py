# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if len(lst)==0:
        return 0
    elif len(lst)==1:
        return lst[0]
    elif(lst[0]<lst[1]):
        lst.pop(0)
    else:
        lst.pop(1)
    return max_recursive(lst)

def sum_lists_recursive(lst1, lst2):
    if len(lst1)==0 and len(lst2)==0:
        return 0
    else:
        return lst1[0]+lst2[0]+sum_lists_recursive(lst1[1:],lst2[1:])

def funky(n):
    if(n==0 or n==1):
        return 1
    elif(n%2==0):
        return 2*funky(n//2)
    else:
        return 1+2*funky(n+1)

print(max_recursive([3, 10, 2, 8, 6]))
print(max_recursive([])) 

print(sum_lists_recursive([1, 2, 3], [4, 5, 6]))
print(sum_lists_recursive([3], [6])) 

print(funky(50))
print(funky(2))