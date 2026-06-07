# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def pyramid(n):
    pyramid_dict = {}

    for i in range(n, 0, -1):
        line = " ".join(str(x) for x in range(i, 0, -1))
        pyramid_dict[n - i + 1] = line 
    
    for key in pyramid_dict:
        print(pyramid_dict[key])

def merge_dicts(d1, d2):
    result = d1.copy()
    for key, value in d2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value    
    return result