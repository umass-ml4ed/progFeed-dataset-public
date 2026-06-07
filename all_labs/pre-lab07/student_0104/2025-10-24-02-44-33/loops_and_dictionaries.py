# Author    : REDACTED
# Email     : REDACTED
# Spire ID  : REDACTED

def pyramid(n):
    
    lst1 = []
    
    while n >= 1:
        lst1.append(n)
        
        n -= 1
    
    result = ""
    
    for i in range(len(lst1)):
        for x in lst1[i:]:
            result += str(x) + " "
        result += "\n"
    
    return result
    


def merge_dicts(d1, d2):
    result = d1.copy()  
    
    for key in d2:
        if key in result:
            result[key] += d2[key] 
        else:
            result[key] = d2[key]  
    return result