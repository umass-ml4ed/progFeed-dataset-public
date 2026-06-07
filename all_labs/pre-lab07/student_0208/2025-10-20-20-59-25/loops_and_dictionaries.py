# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    result = ""
    for i in range(n, 0, -1):          
        for j in range(i, 0, -1):     
            if j == 1:
                result += str(j)
            else:
                result += str(j) + " " 
        result += "\n"                 
    return result

print(pyramid(5))

def merge_dicts(d1, d2):
    new_dict=d1.copy()
    for key in d2:
        if key in new_dict:
            new_dict[key]+=d2[key]
        else:
            new_dict[key]=d2[key]
    return new_dict
print(merge_dicts({'a':1, 'b':2}, {'b':3, 'c':4}))