# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def pyramid(n):
    res=''
    for num in range (n,0,-1):
        newline=''
        for numbers in range (num, 0, -1):
            newline+= str(numbers)
            if numbers!=1:
                newline+= " "
        res+=newline+"\n"
    return res
        
print(pyramid(4))

def merge_dicts(d1,d2):
    d3=d1.copy()
    for key in d2:
        if key in d3:
            d3[key]+=d2[key]
        else:
            d3[key]=d2[key]
    return d3



print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
# {'a': 1, 'b': 5, 'c': 4}

print(merge_dicts({'x': 10}, {'y': 20}))
# {'x': 10, 'y': 20}

print(merge_dicts({}, {'a': 5}))
# {'a': 5}

print(merge_dicts({'a': 1, 'b': 2, 'c': 3}, {'b': 5, 'd': 10}))
# {'a': 1, 'b': 7, 'c': 3, 'd': 10}
