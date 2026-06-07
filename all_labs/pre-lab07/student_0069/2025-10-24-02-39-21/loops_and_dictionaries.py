# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def merge_dicts(d1, d2):
    result = {}  
    for key, value in d1.items():
        result[key] = value
    
    for key, value in d2.items():
        if key in result:
            result[key] += value  
        else:
            result[key] = value 
    return result  


def pyramid(n):
    result = ""
    for i in range(n, 0, -1):
       
        line = ""
        for j in range(i, 0, -1):
            line += str(j)
            if j > 1:  
                line += " "
        
       
        line += "\n"
        result += line
    
    return result