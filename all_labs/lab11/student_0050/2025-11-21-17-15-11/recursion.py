# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lis):
    if len(lis) ==0:
        return 0 
    if len(lis)==1:
        return lis[0]
    return max(lis[0], max_recursive((lis[1:])))

def sum_lists_recursive(*lis):
    if len(lis)==0:
        return 0
    return sum(lis[0])+sum_lists_recursive(*lis[1:])

def funky(n):
    if n==0 or n ==1:
        return 1
    if n%2==0:
        return 2 + funky(n//2)
    else:
        return 1+2*(funky(n+1))

def permutations(lis):
    if len(lis)==1:
        return [lis[:]]
    retlis=[]
    for i in range(len(lis)):
        front_item = lis[i]
        remaining =lis[:i]+lis[i+1:]
        perms=permutations(remaining)
        for j in perms:
            retlis.append([front_item]+j)
    return retlis
        

