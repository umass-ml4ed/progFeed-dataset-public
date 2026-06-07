# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if lst == []:
        return 0
    maximum = max_recursive(lst[1:])
    if lst[0] > maximum:
        return lst[0]
    else:
        return maximum



def sum_lists_recursive(lst1, lst2):
    
    if lst1 == [] and lst2 == []:
        return 0
    summ = lst1[0]+lst2[0]
    nlst1 = lst1[1:]
    nlst2 = lst2[1:]

    return summ + sum_lists_recursive(nlst1,nlst2)

print(sum_lists_recursive([1, 2, 3], [4, 5, 6])) # returns 21
sum_lists_recursive([2, 3], [5, 6])       # returns 16
sum_lists_recursive([3], [6])             # returns 9
print(sum_lists_recursive([],[]))                # returns 0 -> base case



def funky(n):
    if n==0 or n==1:
        return 1
    if n%2 == 0:
        return 2* funky(n//2)
    else:
        return 1+2*funky(n+1)
    
print(funky(2))     # 2
print(funky(10))    # 74
print(funky(50))    # 554
print(funky(-10))   # 50
print(funky(-50))