# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    result=""
    for b in range(n,0,-1):
        s=" ".join(str(r) for r in range(b, 0, -1))
        result+=s+"\n"
    return result


def merge_dicts(d1,d2):
    merged=d1.copy()
    for a,b in d2.items():
        if a in merged:
            merged[a]+=b
        else:
            merged[a]=b 
    return merged