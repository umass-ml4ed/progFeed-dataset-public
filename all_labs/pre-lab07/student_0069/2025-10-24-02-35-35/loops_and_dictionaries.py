# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def pyramid(n):
    for i in range(n, 0, -1):          
        for j in range(i, 0, -1):      
            print(j, end=' ')         
        print()     


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