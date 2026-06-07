# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    result = ""
    while n > 0:
        i = 0
        while i < n:
            result += str(n-i) + " " 
            i += 1
        result += "\n"     
        n -= 1
    return result

print(pyramid(4))

def merge_dicts(d1, d2):
    new = d1.copy()
    for i in d2:
        if i in new:
            new[i] += d2[i]
        else:
            new[i] = d2[i]
    return new

