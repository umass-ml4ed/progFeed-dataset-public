# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    result = ''
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            result += str(j) + ' '
        if i>1:  
            result += '\n'
    return result

def merge_dicts(d1, d2):
    d3=d1.copy()
    for i in d2:
        if i in d3:
            d3.update({i:d3[i]+d2[i]})
        else:
            d3.update({i:d2[i]})
    return d3

print(pyramid(4))
print(pyramid(5))
