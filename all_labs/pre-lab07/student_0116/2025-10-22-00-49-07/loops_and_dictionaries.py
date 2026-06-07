# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    result = ""
    for i in range(n, 0, -1):
        for x in range(i, 0, -1):
            result = result + str(x)
            if x != 1:
                result = result + " "
        result = result + "\n"
    return result
    
def merge_dicts(d1, d2):
    result = d1.copy()
    for key in d2:
        if key in result:
            result[key] = result[key] + d2[key]
        else:
            result[key] = d2[key]
    return result 