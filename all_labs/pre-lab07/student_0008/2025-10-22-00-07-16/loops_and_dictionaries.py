# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    while n > 0:
        i = n
        while i > 0:
            print(f"{i} ", end="")
            i -= 1
        print("")
        n -= 1

def merge_dicts(d1, d2):
    d11 = d1.copy()
    for key, value in d2.items():
        if key in d11:
            d11[key] += value
        else:
            d11[key] = value
    return d11