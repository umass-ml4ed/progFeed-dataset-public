# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(lis)->bool:
    if len(lis)<=3:
        return True
    checker = True
    for i in range(1, len(lis)-1):
        if (lis[i-1]>lis[i] and lis[i+1]>lis[i]):
            checker=True
        elif(lis[i-1]<lis[i] and lis[i+1]<lis[i]):
            checker=True
        else:
            return False
    return checker
