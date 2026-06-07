# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_zigzag(ints):
    if(len(ints)< 3):
        return True
    elif True:
        for x in range(1, (len(ints)-1)):
            if not ((ints[x] > ints[x-1]) and (ints[x] > ints[x+1]) or (ints[x] < ints[x-1] and ints[x]< ints[x+1])):
                return False
        return True