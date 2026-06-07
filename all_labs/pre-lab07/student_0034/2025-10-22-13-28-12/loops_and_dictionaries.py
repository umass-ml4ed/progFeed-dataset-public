# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    while n>= 1:
        for num in range(n, 0, -1):
            if num == 1:
                print(num,'\n')
            else:
                print(num,end=' ')
        n-= 1
    return

pyramid(4)

def merge_dicts(d1, d2):
    n1 = {}
    for key in d1:
        if key in d2:
            n1[key] = (d1[key]+d2[key])
        else:
            n1[key] = (d1[key])
    for key in d2:
        if key not in d1:
            n1[key] = (d2[key])
    return n1

