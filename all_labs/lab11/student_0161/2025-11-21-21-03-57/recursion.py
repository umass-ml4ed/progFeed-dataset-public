# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def max_recursive(lst, j=0, n=0):
    
    if len(lst)==0:
        return None
    if len(lst) ==1:
        return lst[0]

    rest_max = max_recursive(lst[1:])
    return lst[0] if lst[0] > rest_max else rest_max

'''print(max_recursive([3, 10, 2, 8, 6])) # returns 10
print(max_recursive([10, 2, 8, 6])  )  # returns 10
print(max_recursive([2, 8, 6])   )     # returns 8
max_recursive([8, 6])           # returns 8
max_recursive([6])  '''


def sum_lists_recursive(lst1,lst2, sums=0, n=0):
    if len(lst1)==n:
        return sums
    sums+=lst1[n]+lst2[n]
    n+=1
    return sum_lists_recursive(lst1,lst2,sums,n)

'''print(sum_lists_recursive([1, 2, 3], [4, 5, 6])) # returns 21
print(sum_lists_recursive([2, 3], [5, 6]))       # returns 16
sum_lists_recursive([3], [6])             # returns 9
sum_lists_recursive([],[]) '''  


def funky(n):
    if n==0 or n == 1:
        return 1
    elif n % 2 == 0:
        return 2* funky(n//2)
    else:
        return 1+2*funky(n+1)