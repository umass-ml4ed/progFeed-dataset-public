# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    i=n
    while(i > 0):
        j=i
        while(j > 0):
            print(j, end=' ')
            j -= 1

        print("\n")
        i-=1

pyramid(4)

def merge_dicts(d1, d2):
    dict1=d1.copy()
    #new_dict={}
    for key1 in d1:
        for key2 in d2:
            if(key1==key2):
                dict1[key1]=d1[key1]+d2[key2]
            else:
                dict1[key2]=d2[key2]
    return dict1

print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))