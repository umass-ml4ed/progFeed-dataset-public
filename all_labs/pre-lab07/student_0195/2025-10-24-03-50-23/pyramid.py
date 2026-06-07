# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramind(n):
    num = n
    result = ''
    for b in range (0,n):
        for a in range(num,0,-1):
            result += f'{a} '
        num -= 1
        if num == 0:
            continue
        else :
            result += ("\n")
    


    return result


    
print(pyramind(5))