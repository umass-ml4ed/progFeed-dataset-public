# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

#print('abc\ndef')

def pyramid(n):
    x=''
    for a in range(n, 0, -1) :
        for b in range(a, 0, -1):
            if b==1:
                x+=str(b)
            else:
                x+=str(b)+' '
        x+='\n'
    return(x)
print(pyramid(4))

def merge_dicts(d1, d2):
    d3=d1.copy()
    for a in d2:
        if a in d3:
            d3[a]+=d2[a]
        else:
            d3[a]=d2[a]
    return(d3)
print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
# {'a': 1, 'b': 5, 'c': 4}

print(merge_dicts({'x': 10}, {'y': 20}))
# {'x': 10, 'y': 20}

print(merge_dicts({}, {'a': 5}))
# {'a': 5}

print(merge_dicts({'a': 1, 'b': 2, 'c': 3}, {'b': 5, 'd': 10}))
# {'a': 1, 'b': 7, 'c': 3, 'd': 10}

    