# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
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

def merge_dicts(d1,d2):
    result = {}
    for keys in d1:
        result[keys] = d1[keys]
    
    for keys in d2:
        if keys in result:
            result[keys] += d2[keys]
        else :
            result[keys] = d2[keys]

    return result
    
print(pyramid(5))
print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
