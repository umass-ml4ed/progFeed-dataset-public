# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def pyramid(n):
    i=n
    result =""
    for i in range(n,0,-1):
        line=[str(i) for i in range(n,0,-1)]
        result= result + " ".join(line) + "\n"
        n = n- 1
    return(result)

print(pyramid(4))

def merge_dicts(d1, d2)->dict:
    combined_dicts=d1.copy()
    for key in d2:
        if key in combined_dicts:
            combined_dicts[key]=d2[key] + combined_dicts[key]
        elif key not in combined_dicts:
            combined_dicts[key]=d2[key]
    return combined_dicts


print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))









