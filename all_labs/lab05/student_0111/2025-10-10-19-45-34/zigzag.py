# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(lis):
    if len(lis)<3:
        return True
    for e in range(lis[1],lis[-2]):
        i=lis.index(e)-1
        n=lis.index(e)+1
        if e>i and e>n:
            return True
        else:
            return False
print(is_zigzag([1,3,2,4,5]))