# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def combine_lists(a,b):
    a.insert(0,b[0])
    a.append(b[-1])
    a.pop(int(len(a)/2))
    return a

def classify_by_length(a):
    if len(a)/2==0:
        b="empty"
    elif len(a)%2==0:
        b="even_length"
    else:
        b="odd_length"
    return b
