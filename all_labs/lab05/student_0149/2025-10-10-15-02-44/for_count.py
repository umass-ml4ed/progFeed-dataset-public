# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(list,n:int):
    count = 0
    for thing in list:
        if len(thing) >= n:
            count +=1
    return count