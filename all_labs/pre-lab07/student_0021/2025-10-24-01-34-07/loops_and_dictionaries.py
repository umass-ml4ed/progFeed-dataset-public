# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def pyramid(n):
    """Print a pyramid pattern from n down to 1."""
    for i in range(n, 0, -1): 
        line = ""
        for j in range(i, 0, -1): 
            line += str(j) + " "
        print(line.strip()) 



def merge_dicts(d1, d2):
    """Merge two dictionaries, summing values for duplicate keys."""
    result = d1.copy() 
    for key in d2:
        if key in result:
            result[key] += d2[key] 
        else:
            result[key] = d2[key] 
    return result

