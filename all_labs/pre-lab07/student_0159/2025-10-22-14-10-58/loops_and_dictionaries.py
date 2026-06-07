# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED



def pyramid(n):
    output = ""
    for i in range(n,0,-1):
        line= " ".join(str(x) for x in range(i,0,-1))
        output += line + "\n"
    return output
print(pyramid(4))

def merge_dicts(d1,d2):
    merge = d1.copy()
    for x,y in d2.items():
        if x in merge:
            merge[x] += y
        else:
            merge[x] = y
    return merge
