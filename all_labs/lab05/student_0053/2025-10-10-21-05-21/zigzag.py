# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(l: list) -> bool:
    '''This function will check if the list is zigzag'''
    if len(l) < 3:
        return True
    else: 
        for i in range(1, len(l)-1):
            bool1 = l[i-1] < l[i] > l[i+1]
            bool2 = l[i-1] > l[i] < l[i+1]
            if not bool1 and not bool2:
                return False
        return True


