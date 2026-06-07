# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(intlist):
    if len(intlist) < 3:
        return(True)
    for int in range(1, len(intlist) - 1):
        if not ((intlist[int] > intlist[int - 1] and intlist[int] > intlist[int + 1]) or (intlist[int] < intlist[int - 1] and intlist[int] < intlist[int + 1])):
            return(False)
    return(True)