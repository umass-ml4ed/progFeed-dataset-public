# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_strings(lst,n):
    i=0
    for string in lst:
        if len(string)>=n:
            i+=1
    return i
