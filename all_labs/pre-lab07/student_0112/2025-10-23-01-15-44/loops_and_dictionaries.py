# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
def pyramid(n):
    py =""
    for i in range (n):
        index = n-i;
        while (index>0):
            py = py + str(index)
            index = index -1
            if (index == 0): break
            py = py + " "
        py= py+ "\n"
    return py
def merge_dicts(d1,d2):
    result =d1.copy()
    for key, value in d2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result
        


