# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if len(lst)==1:
        return lst[0]
    elif len(lst)==0:
        return 0
    else:
        if lst[0]>=lst[1]:
            lst.pop(1)
        elif lst[0]<lst[1]:
            lst.pop(0)
        return max_recursive(lst)
    
def sum_lists_recursive(lst1,lst2):
    if len(lst1)==1:
        return lst1[0]+lst2[0]
    elif len(lst1)==0:
        return 0
    else:
        sum=lst1[0]+lst2[0]
        lst1.pop(0)
        lst2.pop(0)
        return sum+sum_lists_recursive(lst1,lst2)

def funky(n):
    if n==0 or n==1:
        return 1
    elif n%2==0:
        return 2*funky(n//2)
    else:
        return 1+2*funky(n+1)

def permutations(lis):
    if len(lis)==0:
        return [lis]
    retlis=[]
    for i in range(len(lis)):
        front_item=lis[i]
        remaining=[lis[j] for j in range(len(lis)) if j!=i]
        p=permutations(remaining)
        for k in p:
            k.insert(0,front_item)
            retlis.append(k)
    return retlis

