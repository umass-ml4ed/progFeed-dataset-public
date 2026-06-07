# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def filter_positive(t):
    lst = []
    for item in t:
        if int(item)>0:
            lst.append(int(item))
        else:
            None
    return lst