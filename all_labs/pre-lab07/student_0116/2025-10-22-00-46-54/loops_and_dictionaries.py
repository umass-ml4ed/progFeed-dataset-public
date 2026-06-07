# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    for i in range(n, 0, -1):
        line = ""
        for x in range(i, 0, -1):
            line = line + str(x) + " "
        print(line.strip())
    
def merge_dicts(d1, d2):
    result = d1.copy()
    for key in d2:
        if key in result:
            result[key] = result[key] + d2[key]
        else:
            result[key] = d2[key]
    return result