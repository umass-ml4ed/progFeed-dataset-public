# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    stringy = ""
    i = n
    t = n
    while i>0:
        while t in range (1,i+1):
            stringy += f"{t} "
            t -= 1
        stringy += "\n"
        i -= 1
        t = i
    return stringy

print(pyramid(5))

def merge_dicts(d1, d2):
    empty_dict = {}
    for key in d1:
        if key in d2:
            empty_dict[key] = d1[key] + d2[key]
            continue
        else:
            empty_dict[key] = d1[key]
            continue
    for key in d2:
        if key in d1:
            continue
        else:
            empty_dict[key] = d2[key]
            continue
    return empty_dict