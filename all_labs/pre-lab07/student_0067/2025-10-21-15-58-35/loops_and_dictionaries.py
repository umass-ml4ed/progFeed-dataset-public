# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED



def pyramid(n):
    pyr = ""
    for i in range(n, 0, -1): 
        for j in range(i, 0, -1):  
            pyr += str(j)
            if i+1:
                pyr += " "
        
        pyr += "\n"  
    return pyr

        

def merge_dicts(d1:dict, d2:dict) -> dict:
    d3 = {}
    for key, value in d1.items():
        d3[key] = value

    for key,value in d2.items():
        if key in d3:
            d3[key] += value
        else:
            d3[key] = value

    return d3
        

