# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    pyramid = ""
    while n>0:
        for i in range(n,0,-1):
            pyramid += str(i)
            if i != 1:
                pyramid += " "
        pyramid += "\n"
        n -= 1
    return pyramid

print(pyramid(4))

def merge_dicts(d1, d2):
    result = d1.copy() 
    for key, value in d2.items(): 
        if key in result:
            result[key] += value
        else:
            result[key] = value 
    return result

