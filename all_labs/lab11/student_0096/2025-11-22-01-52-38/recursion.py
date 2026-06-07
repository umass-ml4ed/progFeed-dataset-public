# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def max_recursive(lst):
    if len(lst)==0:
        return lst[0]
    max=max_recursive(lst[1:])
    if lst[0]>=max_recursive(lst[1:]):
        return lst[0]
    else:
        return max

def sum_lists_recursive(lst1,lst2):
    if lst1 ==[] and lst2==[]:
         return 0
    sum1=sum_lists_recursive(lst1[1:],lst2[1:])
    sum2=lst1[0]+lst2[0]
    return sum1 + sum2
        

print(sum_lists_recursive([1, 2, 3], [4, 5, 6]))