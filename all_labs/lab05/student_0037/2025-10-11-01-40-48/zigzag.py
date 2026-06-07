# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(lis):
    if len(lis) < 3:
        return True
    else:
        for i in range(1, len(lis)-1 ):
            if  not ((lis[i] > lis[i - 1] and lis[i] > lis[i + 1]) or (lis[i] < lis[i - 1] and lis[i] < lis[i + 1])):
                return False
        return True



