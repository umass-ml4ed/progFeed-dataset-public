# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED


def is_zigzag(l:list) -> bool:
    for i in l:
        if 0< i < len(l)-1:
            if (l[i-1] < l[i] and l[i] > l[i+1]) or (l[i-1] > l[i]and l[i] < l[i+1]):
                iszigzag = True
            else:
                iszigzag = False
                return iszigzag
        return iszigzag

