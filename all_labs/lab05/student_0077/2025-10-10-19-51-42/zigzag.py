# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def is_zigzag(lst):
    if len(lst)<3:
        return True
    ans=False
    for i in range(1,len(lst)-1):
        if (lst[i]<lst[i-1] and lst[i]<lst[i+1] or lst[i]>lst[i-1] and lst[i]>lst[i+1]):
            ans = True
        else: 
            ans = False
    return ans