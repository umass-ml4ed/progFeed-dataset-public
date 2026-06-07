# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def pyramid(n):
    for i in range(n, 0, -1):
        new_line = " "
        for s in range(i, 0, -1):
            new_line += str(s)
            if s != 1:
                new_line += " "
        print(new_line)



def merge_dicts(d1, d2):
    merge = d1.copy()
    for k in d2:
        if k in merge:
            merge[k] = merge[k] + d2[k]
        else:
            merge[k] = d2[k]
    return merge