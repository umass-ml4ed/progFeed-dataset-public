# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def sum_lists_recursive(lst1,lst2):
    if lst1==[] and lst2==[]:
        return 0
    sum1=sum_lists_recursive(lst1[1:],lst2[1:])
    sum2=lst1[0]+lst2[0]
    return sum1 + sum2
        



def funky(n):
    if n==0 or n==1 or n==-1:
        return 1
    if n%2==0:
        return 2*funky(n//2)
    else:
        return 1+2*funky(n+1)




  
