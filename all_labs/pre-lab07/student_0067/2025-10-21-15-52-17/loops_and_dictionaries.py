# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED



def pyramid(n):
    pyr = ""
    while n > 0:
        

        for i in range(n, 0, -1):
            pyr += str(i)
            pyr += " "
        pyr += '\n'
        
        n -= 1
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
        

