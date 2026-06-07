# Author : REDACTED
# Email: REDACTED
# Spire ID: REDACTED

#Given a positive integer n, print n lines.
def pyramid(n):
    result = ""
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            result += str(j)
            if j != 1:
                result += " "
        if i != 1:
            result += "\n"
    return result

#Return a new dictionary that contains all keys from both d1 and d2.
def merge_dicts(d1, d2):
    result = d1.copy()
    
    for key in d2:
        if key in result:
            result[key] = result[key] + d2[key]
        else:
            result[key] = d2[key]
    return result