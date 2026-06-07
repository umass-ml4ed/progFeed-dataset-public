# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    pyr = ""
    for i in range(n, 0, -1):
        string = " ".join(str(a) for a in range (i, 0, -1))
        pyr += string + "\n"
    pyr.rstrip()

def merge_dicts(d1, d2):
    d11 = d1.copy()
    for key, value in d2.items():
        if key in d11:
            d11[key] += value
        else:
            d11[key] = value
    return d11