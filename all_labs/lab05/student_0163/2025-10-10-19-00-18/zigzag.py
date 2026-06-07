# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(l):
    c=0
    for n in range (1,len(l)-1):

        if (l[n] > l[n-1] and l[n] > l[n+1]) or (l[n] < l[n-1] and l[n] < l[n+1]):
            c+=1
        else:
            pass
    if c==len(l)-2 or len(l)==1:
        return True
    else:
        return False
    
