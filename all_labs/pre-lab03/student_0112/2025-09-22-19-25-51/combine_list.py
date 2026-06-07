# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def combine_list (a,b):
    len_a = len(a)
    len_b = len(b)
    a.insert(0, b[0])
    a.append(b[-1])
    len_new_a = len(a)
    if (len_new_a & 1):
        a.pop((len_new_a)//2)
    return a

