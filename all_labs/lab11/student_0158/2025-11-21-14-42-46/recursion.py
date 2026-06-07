# Authors   : REDACTED
# Emails    : REDACTED
# Spire ID REDACTED

def max_recursive(lst):
    if len(lst)==0:
        return 0
    elif len(lst)==1:
        return lst[0]
    if lst[0]>lst[1]:
        lst.pop(1)
    else:
        lst.pop(0)
    return max_recursive(lst)

def sum_lists_recursive(lst1, lst2):
    if not lst1 and not lst2:
        return 0
    else:
        s=lst1.pop(0)+lst2.pop(0)
        return s+sum_lists_recursive(lst1, lst2)
    
def funky(n):
    if n==0 or n==1:
        return 1
    elif n%2==0:
        return 2*funky(n//2)
    else:
        return 1+2*funky(n+1)
    
def permutations(lis):
    if len(lis)==1:
        return [lis]
    retlis=[]
    for i in range(len(lis)):
        front_item=lis[i]
        remaining=[j for j in lis if j!=front_item]
        perms = permutations(remaining)
        for p in perms:
            retlis.append([front_item]+p)
    return retlis