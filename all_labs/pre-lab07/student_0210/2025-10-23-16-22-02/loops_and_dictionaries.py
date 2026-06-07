# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def pyramid(n):
    for i in range(n, 0, -1):         
        for j in range(i, 0, -1):     
            print(j, end=' ')         
        print()                        

def merge_dicts(d1,d2):
    Result = {}
    for i in d1:
        Result[i] = d1[i]
    
    for i in d2:
        if i in Result:
            Result[i] += d2[i]
        else:
            Result[i] = d2[i]

    return Result
 
